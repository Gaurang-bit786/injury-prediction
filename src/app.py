from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        data = dict(request.form)
        print(list(data.values()))
        fp = open("../model/models.pkl","rb")
        model = pickle.load(fp)

        predict = model.predict([list(data.values())])
        print(predict)
        return render_template('index.html',predict=predict)
    return render_template('index.html',predict=None)

@app.route('/prediction', methods=['POST'])
def prediction():
    data = dict(request.form)
    print(list(data.values()))
    fp = open("../model/models.pkl","rb")
    model = pickle.load(fp)

    predict = model.predict([list(data.values())])
    print(predict)
    return render_template('prediction.html',pre=request.form.get("age"))

if __name__ == '__main__':
    app.run(debug=True)