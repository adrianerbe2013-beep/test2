import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Варианты игры и правила: что что побеждает
CHOICES = ['rock', 'paper', 'scissors']
CHOICES_RU = {
    'rock': 'Камень 🪨',
    'paper': 'Бумага 📄',
    'scissors': 'Ножницы ✂️'
}


def get_winner(user, computer):
    """Определяет победителя: 'user', 'computer' или 'draw'"""
    if user == computer:
        return 'draw'

    # Условия победы пользователя
    if (user == 'rock' and computer == 'scissors') or \
            (user == 'scissors' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        return 'user'

    return 'computer'


@app.route('/', methods=['GET', 'POST'])
def index():
    user_choice = None
    computer_choice = None
    result = None
    message = ""

    if request.method == 'POST':
        # Получаем выбор игрока из формы
        user_choice = request.form.get('choice')

        if user_choice in CHOICES:
            # Выбор компьютера
            computer_choice = random.choice(CHOICES)

            # Определяем итог
            winner = get_winner(user_choice, computer_choice)

            # Формируем красивое сообщение
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

    return render_template(
        'index.html',
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        message=message
    )


if __name__ == '__main__':
    app.run(debug=True)