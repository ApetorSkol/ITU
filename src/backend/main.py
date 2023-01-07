from flask import Flask, Request, make_response   # creating flask API
from flask_cors import CORS

# create instance of class
app = Flask(__name__)
CORS(app)


@app.route('/ping', methods=['GET', 'POST'])
def parse_request():
    #a = Request.get_data()
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    f = open("demofile3.txt", "r")
    return f.read()


if __name__ == "__main__":  # create api interface if this script is called
    app.run(host='0.0.0.0', port=105)
