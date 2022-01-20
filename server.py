from flask import Flask

# __name__ references the appliations's module or package
app = Flask(__name__)


# decorator which specifies the URL to trigger the following function:
@app.route("/")
def hello_world():  # function name can be anything
    return "<p>hello world</p>"


if __name__ == "__main__":
    # keeps flask server running when python script is called
    app.run(debug=True)

# there is live reload so no need restart code
