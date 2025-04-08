import neattext.functions as nfx
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from dashboard import getvaluecounts, getlevelcount, getsubjectsperlevel, yearwiseprofit

app = Flask(__name__)


def getcosinematrics(df):

    countvectorizer = CountVectorizer()
    CV = countvectorizer.fit_transform(df['Clean_title'])
    return CV

# getting the title which doesn't contain stopwords and all which we removed with the help of nfx


def getcleantitle(df):

    df['Clean_title'] = df['course_title'].apply(nfx.remove_stopwords)

    df['Clean_title'] = df['Clean_title'].apply(nfx.remove_special_characters)

    return df


def cosinesimilaritymatrix(CV):

    return cosine_similarity(CV)


def readdata():

    df = pd.read_csv('UdemyCleanedTitle.csv')
    return df

# this is the main recommendation logic for a particular title which is choosen


def recommend(df, title, cosine_matrix, n=10):

    course_index = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    index = course_index[title]
    scores = list(enumerate(cosine_matrix[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    selected_course_index = [i[0] for i in sorted_scores[1:]]
    selected_course_score = [i[1] for i in sorted_scores[1:]]
    rec_df = df.iloc[selected_course_index]
    rec_df['Similarity_Score'] = selected_course_score
    final_recommended_courses = rec_df[['course_title', 'Similarity_Score', 'url', 'price', 'num_subscribers']]

    return final_recommended_courses.head(n)

# this will be called when a part of the title is used,not the complete title!


def searchterm(term, df):
    result_df = df[df['course_title'].str.contains(term)]
    top10 = result_df.sort_values(by='num_subscribers', ascending=False).head(10)
    return top10


# extract features from the recommended dataframe

def extractfeatures(recdf):

    course_url = list(recdf['url'])
    course_title = list(recdf['course_title'])
    course_price = list(recdf['price'])

    return course_url, course_title, course_price


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':

        my_dict = request.form
        titlename = my_dict['course']
        print(titlename)
        try:
            df = readdata()
            df = getcleantitle(df)
            CV = getcosinematrics(df)

            num_rec = 10
            cosine_matrix = cosinesimilaritymatrix(CV)

            recdf = recommend(df, titlename,cosine_matrix, num_rec)
            course_url, course_title, course_price = extractfeatures(recdf)

            # print(len(extractimages(course_url[1])))

            dictmap = dict(zip(course_title, course_url))

            if len(dictmap) != 0:
                return render_template('index.html', coursemap=dictmap, coursename=titlename, showtitle=True)

            else:
                return render_template('index.html', showerror=True, coursename=titlename)

        except:

            resultdf = searchterm(titlename, df)
            if resultdf.shape[0] > 10:
                resultdf = resultdf.head(10)
                course_url, course_title, course_price = extractfeatures(resultdf)
                coursemap = dict(zip(course_title, course_url))
                if len(coursemap) != 0:
                    return render_template('index.html', coursemap=coursemap, coursename=titlename, showtitle=True)

                else:
                    return render_template('index.html', showerror=True, coursename=titlename)

            else:
                course_url, course_title, course_price = extractfeatures(resultdf)
                coursemap = dict(zip(course_title, course_url))
                if len(coursemap) != 0:
                    return render_template('index.html', coursemap=coursemap, coursename=titlename, showtitle=True)

                else:
                    return render_template('index.html', showerror=True, coursename=titlename)

    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    df = readdata()
    valuecounts = getvaluecounts(df)

    levelcounts = getlevelcount(df)

    subjectsperlevel = getsubjectsperlevel(df)

    yearwiseprofitmap, subscriberscountmap, profitmonthwise, monthwisesub = yearwiseprofit(
        df)

    return render_template('dashboard.html', valuecounts=valuecounts, levelcounts=levelcounts,
                           subjectsperlevel=subjectsperlevel, yearwiseprofitmap=yearwiseprofitmap, subscriberscountmap=subscriberscountmap, profitmonthwise=profitmonthwise, monthwisesub=monthwisesub)


if __name__ == '__main__':
    app.run(debug=True)