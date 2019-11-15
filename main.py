from flask import Flask


# application,main(last line) function only one in a file is entrance of an application
hungry = Flask(__name__)

if __name__ == '__main__':
    print(__name__)
    hungry.run(debug=True)
