from flask import Flask

app = Flask(__name__)

# decorators challenge
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<h2 style='text-align: center'>This is a test HTML Flask return</h2>" \
            "<center><video controls autoplay style='align: center'><source src='https://img-9gag-fun.9cache.com/photo/ay2BwWW_460svav1.mp4' type='video/mp4'></video></center>"

# different routes using the app.route decorator
@app.route("/bye")
# decorator challenge
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "Bye, World!"

# creating variable paths and converting  the path to a specific data type
@app.route("/username/<name>")
def hello_name(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route("/username/<name>/<int:age>")
def name_age(name, age):
    return f"<p>{name} is {age} years old.</p>"

if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    app.run(debug=True)