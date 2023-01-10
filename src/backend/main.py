from flask import Flask, request # creating flask API
from flask_cors import CORS
import json

# create instance of class
app = Flask(__name__)
CORS(app)


@app.route('/del_rezervacia', methods=['GET', 'POST'])
def del_rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            pobocka["rezervacie"].remove(request.get_data().decode("utf-8"))
            f.close()
            json_object = json.dumps(users, indent=4)
            f = open("user.json", "w")
            f.write(json_object)
            f.close()
            return "ano"
    return "nie"


@app.route('/make_rezervacia', methods=['GET', 'POST'])
def mkae_rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            pobocka["rezervacie"].append(request.get_data().decode("utf-8"))
            f.close()
            json_object = json.dumps(users, indent=4)
            f = open("user.json", "w")
            f.write(json_object)
            f.close()
            return "ano"
    return "nie"


@app.route('/rezervacia', methods=['GET', 'POST'])
def rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            for rezervace in pobocka["rezervacie"]:
                if rezervace == request.get_data().decode("utf-8"):
                    return "ano"
    return "nie"

@app.route('/pridat_pobocku', methods=['GET', 'POST'])
def pridat_pobocku():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        if user["email"] == request.get_data().decode("utf-8"):
            return 200
    return None


@app.route('/pobocky', methods=['GET', 'POST'])
def pobocky():
    f = open("user.json", "r")
    users = json.loads(f.read())
    output = []
    for user in users:
        output = output + user["pobocky"]
    return output


@app.route('/prihlasenie', methods=['GET', 'POST'])
def prihlasenie():
    f = open("user.json", "r")
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
