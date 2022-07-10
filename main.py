from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello."


@app.route("/to_f/<value>")
def celsius_to_fahrenheit(value):
    try:
        value = float(value)
        f_value = (value * (9 / 5)) + 32
    except:
        return "there was an issue"
    return str(f_value)


@app.route("/to_c/<value>")
def fahrenheit_to_celsius(value):
    try:
        value = float(value)
        f_value = (value - 32) * 5 / 9
    except:
        return "there was an issue"
    return str(f_value)


if __name__ == "__main__":
    app.run()
