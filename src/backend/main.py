from flask import Flask, Request   # creating flask API

# create instance of class
app = Flask(__name__)


@app.route('/ping', methods=['GET', 'POST'])
def parse_request():
    #a = Request.get_data()
    return "a"


if __name__ == "__main__":  # create api interface if this script is called
    app.run(host='0.0.0.0', port=105)
