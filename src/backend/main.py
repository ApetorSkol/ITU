import flask
from flask import Flask, request # creating flask API
from flask_cors import CORS
import json

# create instance of class
app = Flask(__name__)
CORS(app)


@app.route('/pobocky_user', methods=['GET', 'POST'])
def pobocky_user():
    f = open("user.json", "r")
    users = json.loads(f.read())
    output = []
    for user in users:
        if user["email"] != request.get_data().decode("utf-8"):
            continue
        output = user["pobocky"]
        print("uspesne som dokoncil /pobocky_user")
        return output
    return "nie"


@app.route('/emaily', methods=['GET', 'POST'])
def emaily():
    f = open("user.json", "r")
    users = json.loads(f.read())
    output = []
    for user in users:
        output.append(user["email"])
    print("uspesne som dokoncil /emaily")
    return output


@app.route('/last_res', methods=['GET', 'POST'])
def de_rezervacia():
    global LAST_PODNIK
    LAST_PODNIK = request.get_data().decode("utf-8")
    print("uspesne som dokoncil /last_res")
    return LAST_PODNIK


@app.route('/del_rezervacia', methods=['GET', 'POST'])
def del_rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            if pobocka["title"] != LAST_PODNIK:
                continue
            pobocka["rezervacie"].remove(request.get_data().decode("utf-8"))
            f.close()
            json_object = json.dumps(users, indent=4)
            f = open("user.json", "w")
            f.write(json_object)
            f.close()
            print("uspesne som dokoncil /del_rezervacia")
            return "ano"
    print("neuspesne som dokoncil /del_rezervacia")
    return "nie"


@app.route('/make_rezervacia', methods=['GET', 'POST'])
def mkae_rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            if pobocka["title"] != LAST_PODNIK:
                continue
            pobocka["rezervacie"].append(request.get_data().decode("utf-8"))
            f.close()
            json_object = json.dumps(users, indent=4)
            f = open("user.json", "w")
            f.write(json_object)
            f.close()
            print("uspesne som dokoncil /make_rezervacia")
            return "ano"
    print("neuspesne som dokoncil /make_rezervacia")
    return "nie"


@app.route('/rezervacia', methods=['GET', 'POST'])
def rezervacia():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        for pobocka in user["pobocky"]:
            for rezervace in pobocka["rezervacie"]:
                if rezervace == request.get_data().decode("utf-8"):
                    print("uspesne som dokoncil /rezervacia")
                    return "ano"
    print("neuspesne som dokoncil /rezervacia")
    return "nie"


@app.route('/pridat_pobocku', methods=['GET', 'POST'])
def pridat_pobocku():
    f = open("user.json", "r")
    users = json.loads(f.read())
    incoming_data = json.loads(request.get_data().decode("utf-8"))
    for user in users:
        if user["email"] == incoming_data["email"]:
            user["pobocky"].append(incoming_data)
            f.close()
            json_object = json.dumps(users, indent=4)
            f = open("user.json", "w")
            f.write(json_object)
            f.close()
            print("uspesne som dokoncil /pridat_pobocku")
            return "ano"
    print("neuspesne som dokoncil /pridat_pobocku")
    return "nie"


@app.route('/pobocky', methods=['GET', 'POST'])
def pobocky():
    f = open("user.json", "r")
    users = json.loads(f.read())
    output = []
    for user in users:
        output = output + user["pobocky"]
    print("uspesne som dokoncil /pobocky")
    return output


# vrati ti usera zo vsetkeho
@app.route('/prihlasenie', methods=['GET', 'POST'])
def prihlasenie():
    f = open("user.json", "r")
    users = json.loads(f.read())
    for user in users:
        if user["email"] == request.get_data().decode("utf-8"):
            print("uspesne som dokoncil /prihlasenie")
            return user
    print("neuspesne som dokoncil /prihlasenie")
    return None

# basic pingerrino
@app.route('/ping', methods=['GET', 'POST'])
def parse_request():
    #a = Request.get_data()
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    f = open("demofile3.txt", "r")
    print("spracoval som ping")
    return f.read()


if __name__ == "__main__":  # create api interface if this script is called
    app.run(host='0.0.0.0', port=105)
