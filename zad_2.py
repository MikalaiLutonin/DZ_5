
# Задача_2 ======================================================================================================================================================
# Создайте программу для игры в ""Крестики-нолики"".

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)                # по 10 звездочек вначале и вконце

board = list(range(1,10))                                                           # создаем список от [1 до 10)  - это будет игровое поле для игры

def draw_board(_board_):                                                              # рисуем игровое поле с клеточками - разделителями
   print("-" * 13)
   for i in range(3):
      print("|", _board_[0+i*3], "|", _board_[1+i*3], "|", _board_[2+i*3], "|")
      print("-" * 13)

def take_input(_player_token_):                                                       # Принимаем ввод пользователя, проверяет корректность ввода
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + _player_token_ +"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:  
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = _player_token_
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")
 
def check_win(_board_):                                                                     # функция проверки игрового поля, проверяет, выиграл ли игрок.
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if _board_[each[0]] == _board_[each[1]] == _board_[each[2]]:
          return _board_[each[0]]
   return False

def main(_board_):                 # основная функция игры, которая будет запускать все ранее описанные функции. Данная функция запускает и управляет игровым процессом.
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(_board_)

main(board)                     # вызов основной функции

input("Нажмите Enter для выхода!")


