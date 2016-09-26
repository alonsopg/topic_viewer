from flask import *
import pandas as pd
pd.set_option('display.max_colwidth', -1)
app = Flask(__name__)


def linkify(x):
    list_words = ['<a href="http://new_view.com/{}">{}</a>'.format(a,a) for a in x]
    return list_words



# def remove_words(word, data_frame):
#     new_df = data_frame[data_frame['topics'].str.contains(word)]
#     return new_df

@app.route("/")
def show_tables():
    data = pd.read_csv('/Users/user/PycharmProjects/SMH-TopicViewer/SMH-topic-viewer/models/wiki.en.full_r_2_l_68.en.topics.csv',  sep = "(?<!,) ", names=['Weight', 'Topics'])
    del data['Weight']
    data = data.apply(linkify,axis=0)

    return render_template('view.html',
                           tables=[data.to_html(classes='male', escape=False)],
                           titles = ['na', 'Wikipedia Model'])

if __name__ == "__main__":
    app.run(debug=True)
