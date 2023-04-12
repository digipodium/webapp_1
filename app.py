from flask import Flask, render_template
import plotly.express as px 


app = Flask(__name__)

def load_data():
    df = px.data.iris()
    return df

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


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 