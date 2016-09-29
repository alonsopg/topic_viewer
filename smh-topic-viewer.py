from flask import *
import pandas as pd
pd.set_option('display.max_colwidth', -1)
app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv('/Users/user/PycharmProjects/SMH-TopicViewer/SMH-topic-viewer/models/wiki.en.full_r_2_l_68.en.topics.csv',  sep = "(?<!,) ", names=['Weight', 'Topics'])
    del data['Weight']
    return render_template('view.html',
                           tables=[data.to_html(classes='male')],

    titles = ['na', 'Wikipedia Model'])


@app.route("/word/<word>")
def show_word(word):

    data = pd.read_csv('/Users/user/PycharmProjects/SMH-TopicViewer/SMH-topic-viewer/models/wiki.en.full_r_2_l_68.en.topics.csv',  sep = "(?<!,) ", names=['Weight', 'Topics'])
    del data['Weight']
    data  = remove_words(word, data)

    return render_template('view.html',
                           tables=[data.to_html(classes='male')],

    titles = ['na', 'Wikipedia Model'])

def remove_words(word, data_frame):
    new_df = data_frame[data_frame['topics'].str.contains(word)]
    return new_df

#ToDo
#ToDo
#ToDo
#ToDo
#ToDo

if __name__ == "__main__":
    app.run(debug=True)