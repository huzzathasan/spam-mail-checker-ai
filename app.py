from flask import Flask, request
import joblib


app = Flask(__name__)

load_model_data = joblib.load('model-spam-mail-checker-1k-params.joblib')
model = load_model_data['model']


def check_spam(mail: str):
    res = model.predict([mail])[0]
    return res


@app.route('/')
def index():
    return "Welcome to the spam mail checker!"


@app.route("/check")
def check_mail():
    body: dict = request.get_json()
    mail = body.get('mail')
    predict = check_spam(mail)
    if predict == 1:
        return {
            "message": "⚠ Be careful, the mail is spam!",
            "predict": str(predict)
        }
    return {
        "message": "✅ Don't worry, the mail is safe!",
        "predict": str(predict)
    }


if __name__ == "__main__":
    app.run(debug=True)
