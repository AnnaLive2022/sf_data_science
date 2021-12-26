"""Игра угадай число
Компьютер сам загадывает 
и сам угадывает число"""

import numpy as np


def random_predict(number:int=1) -> int:
             
    """Рандомно угадываем число/"""
    
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,500)
        if number == predict_number:
            break 
    return(count)


def score_game(random_predict) -> int: 
    """функция считает скорость угадывания"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список писел от 1 до 101
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Скорость = {score}')
    return(score)


score_game(random_predict)   
    