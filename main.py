from flask import Flask
import utils

users = utils.user_data()
app = Flask(__name__)

@app.route("/")
def page_index():

    str = '<pre>'
    for user in users.values():
        str += f"{user['name']} \n {user['position']} \n {user['skills']} \n\n"
    str += '</pre>'


@app.route("/candidate/<int:id>")
def profile_index(id):
    user = users[id]
    str = '<img src="https://img.freepik.com/free-photo/portrait-beautiful-woman-engineer_23-2148826527.jpg?w=1380&t=st=1678827337~exp=1678827937~hmac=991181477606b23f9a04b371a588ad35047e643566b18e2dc3355409517641aa">'
    str += f'\n<pre>'
    str += f"{user['name']}\n{user['position']}\n{user['skills']}\n\n"
    str += '</pre>'
    return str

app.run(debug=True)