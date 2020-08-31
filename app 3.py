from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

# halaman dataset
@app.route('/dataset', methods=['POST', 'GET'])
def dataset():
    return render_template('datasetbooks.html')  

# halaman visualisasi
@app.route('/visualisation', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

# halaman input 
@app.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    return render_template('recommendation.html')

# halaman hasil
@app.route('/result', methods=['POST', 'GET'])
def result():
    if flask.request.method == ‘POST’:
    m_name = flask.request.form[‘movie_name’]
    m_name = m_name.title()

    if m_name not in all_titles:
        return(flask.render_template(‘negative.html’,name=m_name))
    else:
   result_final = get_recommendations(m_name)
   names = []

for i in range(len(result_final)):
    names.append(result_final.iloc[i][0])
    return flask.render_template(‘positive.html’,book_names=names,search_name=m_name)

    if __name__ == '__main__' :
        model_joblib = joblib.load('model_DT_Joblib')
        app.run(debug=True)