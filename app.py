from flask import Flask, render_template, request, redirect
import plotly.express as px 
from database import Feedback
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


app = Flask(__name__)

def load_data():
    df = px.data.iris()
    return df

def getdb():
    engine = create_engine('sqlite:///app.sqlite', echo=True)
    db = scoped_session(sessionmaker(bind=engine))
    return db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph/1')
def graph_1():
    iris = load_data()
    fig = px.scatter_3d(iris, x="sepal_width", y="sepal_length",
               z="petal_width", color="species", height=700)
    
    fig2 = px.scatter(iris, x="sepal_width", y="sepal_length",
                      color="species", height=700)
    return render_template('graph_1.html', 
                           fig1= fig.to_html(),
                           fig2= fig2.to_html())

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if len(name) == 0 or len(message) == 0:
            print('Name or message is empty')
        else:
            db = getdb()
            db.add(Feedback(name=name, email=email, message=message))
            db.commit()
            db.close()
            return redirect('/feedback')
    return render_template('feedback.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 