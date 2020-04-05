import os, sys

if sys.platform.lower() == "win32":
    os.system("color")

# Group of Different functions for different styles
class style:
    BLACK = lambda x: "\033[30m" + str(x)
    RED = lambda x: "\033[31m" + str(x)
    GREEN = lambda x: "\033[32m" + str(x)
    YELLOW = lambda x: "\033[33m" + str(x)
    BLUE = lambda x: "\033[34m" + str(x)
    MAGENTA = lambda x: "\033[35m" + str(x)
    CYAN = lambda x: "\033[36m" + str(x)
    WHITE = lambda x: "\033[37m" + str(x)
    UNDERLINE = lambda x: "\033[4m" + str(x)
    RESET = lambda x: "\033[0m" + str(x)


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ask/<string:question>", methods=["POST"])
def show_post(question):
    # show the post with the given id, the id is an integer
    return style.YELLOW("Hello, ") + style.RESET("World!x")
