from flask import *
import pandas as pd
pd.set_option('display.max_colwidth', -1)
app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv('/Users/user/PycharmProjects/SMH-TopicViewer/SMH-topic-viewer/models/wiki.en.full_r_2_l_68.en.topics.csv',  sep = "(?<!,) ", names=['Weight', 'Topics'])
    return render_template('view.html',
                           tables=[data.to_html(classes='male')],

    titles = ['na', 'Wikipedia Model'])


if __name__ == "__main__":
    app.run(debug=True)