from flask import *
import pandas as pd
pd.set_option('display.max_colwidth', -1)
app = Flask(__name__)


# def linkify(column):
#     words2url = ['<a href="http://url.com/{}">{}</a>'.format(a,a) for e in column for a in e.split()]
#     return words2url

#casi sale con esto:
#linkify = lambda column: ['<a href="http://url.com/{}">{}</a>'.format(a,a) for e in [column] for a in e.split()]
linkify = lambda column: ['<a href="http://url.com/{}">{}</a>'.format(a,a) for e in [column] for a in e.split(', ')]

def remove_words(word, data_frame):
    new_df = data_frame[data_frame['topics'].str.contains(word)]
    return new_df

@app.route("/")
def show_tables():
    data = pd.read_csv('/Users/user/PycharmProjects/SMH-TopicViewer/SMH-topic-viewer/models/wiki.en.full_r_2_l_68.en.topics.csv',  sep = "(?<!,) ", names=['Weight', 'Topics'])
    del data['Weight']
    #data = data.apply(linkify,axis=0).to_frame
    data = pd.DataFrame(data['Topics'].apply(linkify))

    return render_template('view.html',
                           tables=[data.to_html(classes='male', escape=False)],
                           titles = ['na', 'Wikipedia Model'])

if __name__ == "__main__":
    app.run(debug=True)