from flask import Flask, render_template, redirect, request
import biomall as bm

import json
app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        Title = request.form['Title']
        # companies = request.form.getlist('Loba Chemle')
        # print("bgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",companies)
        bm.BIOMALL(query=Title)

        # -------------------
        with open('./dataBiomall.json') as f:
            d = json.load(f)
        with open('empty.txt', 'w') as json_file:
            json.dump({}, json_file)
        # print("dddddd", d)
        d = d['Products']
        # print("FINAL!!", d)

        task, Title, allData = [1, Title, d] 

    return render_template('recommend.html', Title=Title, allData=allData)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
