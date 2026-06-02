import random
import os
from flask import Flask, request, render_template

# Указываем Flask искать HTML-файлы прямо в корневой папке проекта
app = Flask(__name__, template_folder='.')

CHOICES = ['rock', 'paper', 'scissors']
CHOICES_RU = {
    'rock': 'Камень 🪨',
    'paper': 'Бумага 📄',
    'scissors': 'Ножницы ✂️'
}

def get_winner(user, computer):
    if user == computer:
        return 'draw'
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return 'user'
    return 'computer'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    message = ""

    if request.method == 'POST':
        user_choice = request.form.get('choice')
        if user_choice in CHOICES:
            computer_choice = random.choice(CHOICES)
            winner = get_winner(user_choice, computer_choice)

            user_display = CHOICES_RU[user_choice]
            computer_display = CHOICES_RU[computer_choice]

            if winner == 'draw':
                result = 'draw'
                message = f"Ничья! Оба выбрали {user_display}."
            elif winner == 'user':
                result = 'user'
                message = f"Вы выиграли! Ваш {user_display} побеждает {computer_display}."
            else:
                result = 'computer'
                message = f"Вы проиграли! {computer_display} побеждает ваш {user_display}."

    # Рендерим index.html, который лежит в той же папке
    return render_template('index.html', result=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
else:
    pass