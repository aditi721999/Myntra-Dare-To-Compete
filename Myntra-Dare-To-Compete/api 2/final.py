from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import  random
import speech_recognition as sr


cluster = MongoClient("mongodb+srv://ashita:ashita18@cluster0.ieflc.mongodb.net/MyntraImages?retryWrites=true&w=majority")
db = cluster["MyntraImages"]
collection = db["Wishlist"]
Site = db["Myntra"]
app = Flask(__name__)
#toaster=win10toast.ToastNotifier()


@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/bodytype',methods=['GET'])
def bt():
		return render_template('bodytype.html')
	

@app.route('/calculate',methods=['POST'])
def cal():
		shoulder=int(request.form['shoulder'])
		hips=int(request.form['hips'])
		waist=int(request.form['waist'])
		if(hips-shoulder>=3.6 and hips-waist<9):
			return "Triangle"
		elif(hips-shoulder<3.6 and hips-waist>9):
			return "Inverted Triangle"
		else:
			return "Rectangle"


@app.route('/mixnmatch')
def dressup():
    return render_template('mixnmatch.html')

@app.route('/voice')
def do():
	return render_template('index.html')


@app.route('/voicesearch',methods=['POST'])
def search():
	f = request.files['audio_data']
	with open('audio.wav', 'wb') as audio:
		f.save(audio)
	recog = sr.Recognizer()
	sample_audio = sr.AudioFile('audio.wav')
	with sample_audio as audio_file:
		audio_content = recog.record(audio_file)
	print(audio_content)

	s=recog.recognize_google(audio_content)
 
	number = "-".join(s.split()).replace(' ','-')
	url='https://www.myntra.com/'+number
	return redirect(url)


@app.route('/trendbox')
def trendy():
    return render_template('trend.html')

@app.route('/qa')
def qa():
    return render_template('myntra.html')


@app.route('/wishlist')
def wishlist():
    data=[]
    data = collection.find({})
    return render_template('wishlist.html', content=data)


@app.route('/stylebox', methods=['POST'])
def style():
    celeb = str(request.form['celeb'])
    if celeb=='kiara':
    	return render_template('kiara.html')
    else:
    	return render_template('sona.html')

 


@app.route('/wishlist/form')
def wishlistnew():
    return render_template('add.html')


@app.route('/wishlist/new', methods=['POST'])
def add_image():
    _img = request.form['img']
    _price = request.form['price']
    user_size = request.form['size']
    collection.insert_one({'img':_img,'price':_price, 'size':user_size,'id':collection.count()+1})
    data = collection.find({})
    return render_template('wishlist.html', content=data)

@app.route('/wishlist/sale')
def sale():
#	toaster.show_toast('Myntra','Your wishlisted item just went on sale',duration =20)
	for i in range(3):
		sel=random.randint(1,collection.count())
		item=collection.find_one({'id':sel})['price']
		k=int(item)
		collection.update_one({"id": sel},{"$set":{"price":k-10}})
	data = collection.find({})
	return render_template('wishlist.html', content=data)



@app.route('/qa/result', methods=['POST'])
def getvalue():
    gender = request.form['gender']
    occasion = request.form['occasion']
    body = request.form['body']
    skin = request.form['skin']
    color = request.form['color']
    category = request.form['category']
    return redirect(questions(gender, occasion, body, skin, color, category))


list_of_questions = ['Gender :',
                     'Occasion?',
                     'Which among the following is most close to your body type?',
                     'Which among the following is most close to your skin complexion ?',
                     'Any preferred color ?',
                     'Any preferred category?',
                     ]

lists_of_answers = [['A:Woman', 'B:Man'],
                    ['A:Casual Wear', 'B:Party Wear', 'C:Festive Wear'],
                    ['A:Triangle', 'B:Inverted Triangle', 'C:Rectangle', 'D: Prefer Not To Answer'],
                    ['A:Dark Brown', 'B:Medium Brown', 'C:Light Brown', 'D:Prefer Not To Answer'],
                    ['A:None ', 'B:White ', 'C:Navy-Blue ', 'D:Red ', 'E:Blue ', 'F:Lavender', 'G:Purple ', 'H:Green ',
                     'I:Teal ', 'J:Orange ', 'K:Black '],
                    ['A:None', 'B:Kurta-Sets/Suits', 'C:Kurtas', 'D:Shirt/Top', 'E:Jeans']]


def questions(g, o, b, s, c, cat):
    print('Welcome, I am your personal assistant for today')
    print('Please answer few of my questions')
    count = 1
    occasion = ''
    occ = ''
    gender = ''
    color = ''
    category = ''
    co = ''
    gen = ''
    url1 = ''
    for each_question, each_answer in zip(list_of_questions, lists_of_answers):
        print(each_question + '\n' + ' '.join(each_answer))
        if count == 1:
            gen = g
            if g == 'A':
                gender = 'Gender%3Amen%20women%2Cwomen'
            elif g == 'B':
                gender = 'Gender%3Amen%2Cmen'
        elif count == 2:
            occ = o
            if o == 'A':
                occasion = 'casual-wear?'
            elif o == 'B':
                occasion = 'party-wear?'
            elif o == 'C':
                occasion = 'festive-wear?'
        elif count == 3:
            category = b
            if b == 'A':
                url1 = 'https://www.myntra.com/long-coat?'
            elif b == 'B':
                url1 = 'https://www.myntra.com/boots?'
            elif b == 'C':
                url1 = 'https://www.myntra.com/belt?'
        elif count == 4:
            if s == 'A':
                color = 'Color%3ABlack_36454f%2COlive_3D9970%2CPeach_ffe5b4%2CPurple_800080'
            elif s == 'B':
                color = 'Color%3AOrange_f28d20%2CRose_dd2f86%2CTeal_008080%2CWhite_f2f2f2'
            elif s == 'C':
                color = 'Color%3ABlue_0074D9%2CLavender_d6d6e5%2CPink_f1a9c4%2CRed_d34b56'

        elif count == 5:
            if c == 'K':
                color = 'Color%3ABlack_36454f'
            elif c == 'B':
                color = 'Color%3AWhite_f2f2f2'
            elif c == 'C':
                color = 'Color%3ANavy Blue_3c4477'
            elif c == 'D':
                color = 'Color%3ARed_d34b56'
            elif c == 'E':
                color = 'Color%3ABlue_0074D9'
            elif c == 'F':
                color = 'Color%3ALavender_d6d6e5'
            elif c == 'G':
                color = 'Color%3APurple_800080'
            elif c == 'H':
                color = 'Color%3AGreen_5eb160'
            elif c == 'I':
                color = 'Color%3ATeal_008080'
            elif c == 'J':
                color = 'Color%3AOrange_f28d20'

        elif count == 6:
            temp = cat
            cat = category
            category = temp
            if cat == 'A':
                if category == 'A':
                    if occ != 'C' and gen == 'B':
                        co = 'Categories%3ANehru%20Jackets'
                    else:
                        co = 'Categories%3AKurtas'
                elif category == 'B':
                    if occ != 'C' and gen == 'B':
                        co = 'Categories%3ANehru%20Jackets'
                    else:
                        co = 'Categories%3AKurta Sets'
                elif category == 'C':
                    if occ != 'C' and gen == 'B':
                        co = 'Categories%3ANehru%20Jackets'
                    else:
                        co = 'Categories%3AKurtas'
                elif category == 'D':
                    if gen == 'B':
                        co = 'Categories%3AShirts%3A%3APattern%3AChecked'
                    else:
                        if occ == 'C':
                            co = 'Categories%3ASaree%20Blouse'
                        else:
                            co = 'Categories%3ATops%3A%3ASleeve'
                elif category == 'E':
                    if occ == 'C':
                        occasion = 'jeans?'
                        co = ''
                    else:
                        co = 'Categories%3AJeans%3A%3AFit%3ABootcut'

            elif cat == 'B':
                if category == 'A':
                    if occ != 'C' and gen == 'B':
                        co = 'Categories%3ABlazers'
                    else:
                        co = 'Categories%3AKurtas%3A%3ANeck%3AV-Neck'
                elif category == 'B':
                    if gen == 'B':
                        occasion = 'kurta Sets?'
                        co = ''
                    else:
                        co = 'Categories%3AKurta Sets%3A%3ATop Shape%3AAnarkali'
                elif category == 'C':
                    if occ != 'C' and gen == 'B':
                        occasion = 'kurtas?'
                        co = ''
                    else:
                        co = 'Categories%3AKurtas%3A%3ANeck%3AV-Neck'
                elif category == 'D':
                    if gen == 'B':
                        co = 'Categories%3AShirts%3A%3AFit%3ASkinny%20Fit%2CSlim%20Fit'
                    else:
                        if occ == 'C':
                            co = 'Categories%3ASaree%20Blouse'
                        else:
                            co = 'Categories%3ATops%3A%3AType%3APeplum%2CWrap'
                elif category == 'E':
                    if occ == 'C':
                        occasion = 'jeans?'
                        co = ''
                    else:
                        co = 'Categories%3AJeans%3A%3AWaist Rise%3AHigh-Rise'

            elif cat == 'C':
                if category == 'A':
                    if occ != 'A':
                        co = 'Categories%3ASweatshirts'
                    else:
                        c = 'Categories%3AJeans%3A%3AFit%3ABoyfriend Fit%2CStraight Fit'
                elif category == 'B':
                    if gen == 'A':
                        co = 'Categories%3AKurta Sets%3A%3ATop Shape%3AAnarkali'
                    else:
                        occasion = 'Kurta Sets?'
                        co = ''
                elif category == 'C':
                    if occ != 'C' and gen == 'B':
                        occasion = '?'
                        co = ''
                    else:
                        co = 'Categories%3AKurtas%3A%3ANeck%3ARound Neck%2CShirt Collar%2CV-Neck'
                elif category == 'D':
                    if gen == 'A':
                        if occ == 'C':
                            co = 'Categories%3ASaree%20Blouse'
                        else:
                            co = 'Categories%3ATops%3A%3ANeck%3AScoop Neck'
                    else:
                        co = 'Categories%3AShirts%3A%3APattern%3AStriped'
                elif category == 'E':
                    if occ == 'C':
                        occasion = 'jeans?'
                        co = ''
                    else:
                        co = 'Categories%3AJeans%3A%3AFit%3ABoyfriend Fit%2CStraight Fit'

        count = count + 1

    print('THANK YOU FOR YOUR PATIENCE')
    print('Here are your customized suggestions :')
    if co == '' and color == '':
        url = 'https://www.myntra.com/' + occasion + 'f=' + gender
    elif co == '':
        url = 'https://www.myntra.com/' + occasion + 'f=' + color + '%3A%3A' + gender
    elif color == '':
        url = 'https://www.myntra.com/' + occasion + 'f=' + co + '%3A%3A' + gender
    else:
        url = 'https://www.myntra.com/' + occasion + 'f=' + co + '%3A%3A' + color + '%3A%3A' + gender
    print(url)
    return url


if __name__ == '__main__':
    app.run()