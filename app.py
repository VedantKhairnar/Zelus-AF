from flask import Flask, render_template, redirect, request
import recommender as rc

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        Title = request.form['Title']
        # task, Title, allData = rc.supreme(Title)

        task, Title, allData = [1, "MacBook", [{'title': 'Apple MacBook Pro',
                                                'url': 'https://images-na.ssl-images-amazon.com/images/I/71L2iBSyyOL._SL1500_.jpg',
                                                'popularity': '₹1,42,990', 'release_date': '2015-12-15',
                                                'overview': 'Apple MacBook Pro with Touch Bar Core i5 8th Gen - (8 GB/512 GB SSD/Mac OS Catalina) MXK52HN/A  (13 inch, Space Grey, 1.4 kg)',
                                                'genres': 'Amazon', 'vote_average': 7.4}, {'title': 'Apple MacBook Air',
                                                                                           'url': 'https://rukminim1.flixcart.com/image/312/312/jsnjbm80/computer/j/8/c/apple-na-thin-and-light-laptop-original-imafe6f78hur4jbh.jpeg?q=70',
                                                                                           'popularity': '₹69,990',
                                                                                           'release_date': '2015-12-15',
                                                                                           'overview': 'Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466  (13.3 inch, Silver, 1.35 kg)',
                                                                                           'genres': 'Amazon',
                                                                                           'vote_average': 7.4},
                                               {'title': 'Apple MacBook Air',
                                                'url': 'https://rukminim1.flixcart.com/image/312/312/jsnjbm80/computer/j/8/c/apple-na-thin-and-light-laptop-original-imafe6f78hur4jbh.jpeg?q=70',
                                                'popularity': '₹69,990',
                                                'release_date': '2015-12-15',
                                                'overview': 'Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466  (13.3 inch, Silver, 1.35 kg)',
                                                'genres': 'Flipkart',
                                                'vote_average': 7.4}, {'title': 'Apple MacBook Pro',
                                                                       'url': 'https://rukminim1.flixcart.com/image/416/416/kamtsi80/computer/k/a/v/apple-na-thin-and-light-laptop-original-imafs5nmg3kxcqnz.jpeg?q=70',
                                                                       'popularity': '₹1,74,900',
                                                                       'release_date': '2015-12-15',
                                                                       'overview': 'Apple MacBook Pro with Touch Bar Core i5 10th Gen - (16 GB/512 GB SSD/Mac OS Catalina) MWP42HN/A  (13 inch, Space Grey, 1.4 kg)',
                                                                       'genres': 'Flipkart',
                                                                       'vote_average': 7.4},{'title': 'Apple MacBook Pro',
                                                'url': 'https://images-na.ssl-images-amazon.com/images/I/71L2iBSyyOL._SL1500_.jpg',
                                                'popularity': '₹1,42,990', 'release_date': '2015-12-15',
                                                'overview': 'Apple MacBook Pro with Touch Bar Core i5 8th Gen - (8 GB/512 GB SSD/Mac OS Catalina) MXK52HN/A  (13 inch, Space Grey, 1.4 kg)',
                                                'genres': 'Amazon', 'vote_average': 7.4}, {'title': 'Apple MacBook Air',
                                                                                           'url': 'https://rukminim1.flixcart.com/image/312/312/jsnjbm80/computer/j/8/c/apple-na-thin-and-light-laptop-original-imafe6f78hur4jbh.jpeg?q=70',
                                                                                           'popularity': '₹69,990',
                                                                                           'release_date': '2015-12-15',
                                                                                           'overview': 'Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466  (13.3 inch, Silver, 1.35 kg)',
                                                                                           'genres': 'Amazon',
                                                                                           'vote_average': 7.4},
                                               {'title': 'Apple MacBook Air',
                                                'url': 'https://rukminim1.flixcart.com/image/312/312/jsnjbm80/computer/j/8/c/apple-na-thin-and-light-laptop-original-imafe6f78hur4jbh.jpeg?q=70',
                                                'popularity': '₹69,990',
                                                'release_date': '2015-12-15',
                                                'overview': 'Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466  (13.3 inch, Silver, 1.35 kg)',
                                                'genres': 'Flipkart',
                                                'vote_average': 7.4}, {'title': 'Apple MacBook Pro',
                                                                       'url': 'https://rukminim1.flixcart.com/image/416/416/kamtsi80/computer/k/a/v/apple-na-thin-and-light-laptop-original-imafs5nmg3kxcqnz.jpeg?q=70',
                                                                       'popularity': '₹1,74,900',
                                                                       'release_date': '2015-12-15',
                                                                       'overview': 'Apple MacBook Pro with Touch Bar Core i5 10th Gen - (16 GB/512 GB SSD/Mac OS Catalina) MWP42HN/A  (13 inch, Space Grey, 1.4 kg)',
                                                                       'genres': 'Flipkart',
                                                                       'vote_average': 7.4},  ]]

        print(Title)
        print(allData)
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
