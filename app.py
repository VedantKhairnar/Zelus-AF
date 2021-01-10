from flask import Flask, render_template, redirect, request
import scbt_Final as sc
import json
app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        Title = request.form['Title']

        sc.URL_Generator(Title)

        # -------------------
        with open('./data.json') as f:
            d = json.load(f)
        with open('empty.txt', 'w') as json_file:
            json.dump({}, json_file)
        print("dddddd",d)
        d = d['SCBT']
        print("FINAL!!", d)

        """
        d = {"Tris Base": [{'title': 'Tris Base',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$147.07', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'Tris Base',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$138.05', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'Tris Base',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$140.08', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],
                            
            "DMEM": [{'title': 'DMEM',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$400.34', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'DMEM',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$398.34', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'DMEM',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$405.56', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],

            "Triethylammonium bromide": [{'title': 'Triethylammonium bromide',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$537.68', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'Triethylammonium bromide',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$460.00', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'Triethylammonium bromide',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$500.00', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],
            
            "Bovine Serum Albumin": [{'title': 'Bovine Serum Albumin',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$7200.55', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'Bovine Serum Albumin',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$7339.80', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'Bovine Serum Albumin',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$7238.40', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],
                            
            "Sodium Citrate": [{'title': 'Sodium Citrate',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$15.32', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'Sodium Citrate',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$20.67', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'Sodium Citrate',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$18.78', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],    
            "SDS": [{'title': 'SDS',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$400.17', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'SDS',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$430.16', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'SDS',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$398.90', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],  
            "Tris hydrochloride": [{'title': 'Tris hydrochloride',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$380.00', 'release_date': '2015-12-15',
                            'overview': 'SKU RM9971-30G',
                            'genres': 'Himedia', 'vote_average': 7.4}, {'title': 'Tris hydrochloride',
                                                                        'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                                                                        'popularity': '$360.00', 'release_date': '2015-12-15',
                                                                        'overview': 'SKU RM9971-30G',
                                                                        'genres': 'Santa Cruz', 'vote_average': 7.4},
                           {'title': 'Tris hydrochloride',
                            'url': 'http://cdna1.zoeysite.com/Adzpo594RQGDpLcjBynL1z/cache=expiry:31536000/resize=fit:max,width:1200//auto_image/compress/https://s3.amazonaws.com/zcom-media/sites/a0iE000000P2ZHyIAN/media/catalog/product/r/m/rm9971-30g.jpg',
                            'popularity': '$340.00', 'release_date': '2015-12-15',          'overview': 'SKU RM9971-30G',
                            'genres': 'Merck', 'vote_average': 7.4}],  
                        }
        """

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
