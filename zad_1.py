# Задача_1 ======================================================================================================================================================
# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint as ri

total_sweet = 150  # Общее количество конфет
take_sweet = 0     # сколько конфет будет брать игрок или бот на один ход. Начальное значение =0
player_sweet = 0   # количество конфет у игрока. Начальное значение = 0
bot_sweet = 0      # количество конфет у бота. Начальное значение = 0


def who_is_firts():   # функция рандомной жеребьевки, выбор игрока для первого хода
    random_number = ri(1,2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()

def player_turn():
    global total_sweet       # используем переменную из основного тела программы
    global take_sweet
    global player_sweet
    print(f"Ваш ход. На столе {total_sweet}")
    take_sweet = int(input("Сколько конфет вы хотите взять?: "))
    while  take_sweet > 28  or take_sweet < 0 or  take_sweet >  total_sweet:          # проверка на правильность ввода, что игрок берет не более 28-ми конфет и не больше кончет, чем есть на столе
        take_sweet = int(input("Вы берете слишком много конфет! Попробуйте снова: "))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print("Вы победили!")

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1,28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f"Бот взял {take_sweet} конфет! На столе осталось {total_sweet} конфет!")
    if total_sweet > 0:
        player_turn()
    else:
        print("Бот победил")

print('Я хочу сыграть с тобой в игру "Конфетки"!!!')
who_is_firts()


