from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Правила игры
WIN_CONDITIONS = {
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень'
}

CHOICES = ['камень', 'ножницы', 'бумага']


@app.route('/')
def index():
    """Главная страница с игрой"""
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    """Обработка хода игрока"""
    data = request.get_json()
    player_choice = data.get('choice', '').lower()

    # Проверка корректности выбора
    if player_choice not in CHOICES:
        return jsonify({'error': 'Неверный выбор'}), 400

    # Выбор компьютера
    computer_choice = random.choice(CHOICES)

    # Определение победителя
    if player_choice == computer_choice:
        result = 'ничья'
        message = f'Ничья! Оба выбрали {player_choice}'
    elif WIN_CONDITIONS[player_choice] == computer_choice:
        result = 'win'
        message = f'Вы выиграли! {player_choice} побеждает {computer_choice}'
    else:
        result = 'lose'
        message = f'Вы проиграли! {computer_choice} побеждает {player_choice}'

    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
        'message': message
    })


if __name__ == '__main__':
    app.run(debug=True)
else:
    pass