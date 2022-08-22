# Рисуем поле
def show_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)


# Проверяем шаг
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


# Проверяем на победу
def win_check(spots):
    # По горизонтали
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    # По вертикали
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    # По диагонали
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]):
        return True

    else:
        return False


# Переменные
IsPlaying = True
turn = 0
HasWon = False
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

# Механика игры
while IsPlaying:
    show_board(spots)
    choice = input("Очередь игрока " + str((turn % 2) + 1) + ": ")
    turn += 1
    spots[int(choice)] = check_turn(turn)
    # Не занято ли уже это место?
    if str.isdigit(choice) and str(choice) in spots:
        if not spots[int(choice)] in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if win_check(spots):
        IsPlaying, HasWon = False, True

    if turn > 8:
        IsPlaying = False

# Кто побеждает?
show_board(spots)
if HasWon:
    if check_turn(turn) == "X":
        print("Игрок 1 побеждает!")
    else:
        print("Игрок 2 побеждает!")
else:
    print("Ничья")