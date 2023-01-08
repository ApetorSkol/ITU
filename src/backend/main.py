from flask import Flask, request # creating flask API
from flask_cors import CORS
import json

# create instance of class
app = Flask(__name__)
CORS(app)

@app.route('/prihlasenie', methods=['GET', 'POST'])
def prihlasenie():
    f = open("user.json", "r")
    print(f)
    users = json.loads(f.read())
    for user in users:
        if user["email"] == request.get_data().decode("utf-8"):
            return user
    return None

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
