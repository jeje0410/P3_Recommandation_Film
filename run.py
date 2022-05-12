from flask import Flask, render_template,request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world 3333 !"

@app.route('/filmsSimilaires')
def filmsSimilaires():
    numFilm = request.args.get('numFilm')
    if type(numFilm) is str:
        numFilmToInt = int(numFilm)
        if not 'df' in locals():
            df = pd.read_csv('KNN_BRUTE.csv', sep = '\t', encoding='UTF-8')
        filmChoisi = df.iloc[numFilmToInt]
        filmSimilaire1 = df.iloc[df.iloc[numFilmToInt,3]]
        filmSimilaire2 = df.iloc[df.iloc[numFilmToInt,4]]
        filmSimilaire3 = df.iloc[df.iloc[numFilmToInt,5]]
        filmSimilaire4 = df.iloc[df.iloc[numFilmToInt,6]]
        filmSimilaire5 = df.iloc[df.iloc[numFilmToInt,7]]
        return render_template('films.html', name=filmChoisi,
                           name1 = filmSimilaire1,
                           name2 = filmSimilaire2,
                           name3 = filmSimilaire3,
                           name4 = filmSimilaire4,
                           name5 = filmSimilaire5)
    else :
        return render_template('filmsVide.html')

if __name__ == "__main__":
    app.run()