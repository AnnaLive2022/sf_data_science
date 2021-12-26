"""Игра угадай число
Компьютер сам загадывает 
и сам угадывает число"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число/"""
    
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break 
    return(count)

# print(f'Компьютер угадал число за {random_predict(10)} попыток ')       
# print(random_predict(10))    

def score_game(random_predict) -> int:
    count_ls = []
    np.random.speed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список писел от 1 до 101
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Скорость = {score}')
    return(score)
score_game(random_predict)