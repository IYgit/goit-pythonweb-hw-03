from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
DATA_FILE = os.path.join('storage', 'data.json')

# Завантаження головної сторінки
@app.route('/')
def index():
    return render_template('index.html')

# Завантаження сторінки з формою
@app.route('/message', methods=['GET', 'POST'])
def message():
    success = False

    if request.method == 'POST':
        username = request.form.get('username')
        message_text = request.form.get('message')

        if username and message_text:
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}

            data[str(datetime.now())] = {
                'username': username,
                'message': message_text
            }

            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            success = True

    return render_template('message.html', success=success)


# Завантаження всіх повідомлень
@app.route('/read')
def read():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = {}

    return render_template('read.html', messages=messages)

# Обробка помилки 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

# Запуск сервера на порту 3000
if __name__ == '__main__':
    app.run(port=3000)
