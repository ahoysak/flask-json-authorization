from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('user_name')
        text_msg = request.form.get('text_msg')
        id = request.form.get('id')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        print(name)
        print(text_msg)
        print(id)
        print(email)
        print(first_name)
        print(last_name)
        print(password)
        with open('users.json') as f:
            data = json.load(f)

        if name != '' and text_msg != '' and id != '' and email != '' and first_name != '' and last_name != '' and password != '':
            name_text = {"nickname": name, "text": text_msg, "id": id, "email": email, "first_name": first_name, "last_name": last_name, "password": password}
            print(name_text)
            data.append(name_text)
            with open('users.json', 'w') as f:
                json.dump(data, f)

        with open('users.json') as f:
            data = json.load(f)

        return render_template('index.html', data=data)
    else:
        return render_template('index.html')
# всі команди
@app.route('/about', methods=['GET', 'POST'])
def go_user():
    with open('users.json') as f:
        data = json.load(f)
    return render_template('shows.html', data=data)
# видалення
@app.route('/delete/<int:id>/del', methods=['GET', 'POST'])
def delete_users(id):
    try:
        if request.method == 'GET':
            file = open('users.json', 'r')
            users = json.loads(file.read())
            file.close()
            counter = 0
            for user in users:
                if user['id'] == str(id):
                    break
                counter = counter + 1
            del users[counter]
            with open('users.json', 'w') as file:
                file.write(json.dumps(users))
        return redirect('/about')
    except:
        return ' ne tak'
# редагування
@app.route('/update/<int:id>/up', methods=['GET'])
def update_user_page(id):
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    for user in users:
        if user['id'] == str(id):
            return render_template('update.html', user=user)

@app.route('/update/<int:id>/save', methods=['POST'])
def save_user(id):
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    for user in users:
        if user['id'] == str(id):
            user['nickname'] = request.form.get('nickname')
            user['text'] = request.form.get('text')
            user['email'] = request.form.get('email')
            user['first_name'] = request.form.get('first_name')
            user['last_name'] = request.form.get('last_name')
            user['password'] = request.form.get('password')
    with open('users.json', 'w') as file:
        file.write(json.dumps(users))
    return redirect('/about')

@app.route('/search', methods=['GET'])
def show_user():
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    nickname = request.args.get('nickname')
    for user in users:
        if user['nickname'] == nickname:
            return render_template('/finded.html', searched=user)
    return 'Error'

@app.route('/find', methods=['GET'])
def find():
    return render_template('find.html')

@app.route('/email', methods=['GET'])
def show_command():
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    password = request.args.get('password')
    email = request.args.get('email')
    for user in users:
        if user['password'] == password and user['email'] == email:
            return render_template('/cheking.html')
    return 'Error'

@app.route('/check', methods=['GET'])
def check_email():
    return render_template('authorization.html')


if __name__ == '__main__':
    app.run(debug=True)







