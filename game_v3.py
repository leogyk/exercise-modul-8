""" Игра угадай число
Компьютер сам загадывает и угадывает число
"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1 # Устанавливаем нижнюю границу диапазона
    high = 100 # Устанавливаем верхнюю границу диапазона
    predict = (low + high) // 2
    
    # Цикл продолжается, пока предсказанное число не совпадет с загаданным
    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1 # Изменеяем нижнюю границу
        elif number < predict:
            high = predict - 1 # Изменяем верхнюю границу
        predict = (low + high) // 2 # Выводим среднее значение измененных границ
        
    return (count)

"""Модифицируем задачу game_v2.py
Определяем среднее количество попыток угадывания числа"""

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)



    
    