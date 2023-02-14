from flask import Flask, request, render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
from numpy import abs



app = Flask(__name__, template_folder='templates')
@app.route('/', methods = ['POST', 'GET'])
def main():
    y_pred = ''
    if request.method == 'POST':
        exp = float(request.form['experience'])
        y_pred = loaded_model.predict([[exp]])
        y_pred = abs(y_pred)
    return render_template('main.html', result = y_pred)


if __name__ == '__main__':
    with open('lr_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    app.run(debug=True)
