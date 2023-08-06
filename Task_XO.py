# Задача XO необязательная. Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля. Если есть желание, то можете наделить бота псевдоинтеллектом, чтобы он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
# -------------
# |   |   |   |
# -------------
# | O | X |   |
# -------------
# |   |   |   |
# -------------

import random

def display_board(board: list[list[str]]) -> None:        # Функция для отображения игрового поля
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")


def check_win(board: list[list[str]], player: str) -> bool:   # Функция проверки выигрышных комбинаций
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def bot_move(board: list[list[str]]) -> tuple[int, int]:   # Функция ходов бота
    
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":                # Проверка свободных ячеек на поле
                available_moves.append((i, j))
    
   
    for move in available_moves:
        temp_board = [row[:] for row in board] 
        temp_board[move[0]][move[1]] = "O"       # Ход бота
        if check_win(temp_board, "O"):
            return move
    
    for move in available_moves:
        temp_board = [row[:] for row in board]  
        temp_board[move[0]][move[1]] = "X"       # Ход игрока
        if check_win(temp_board, "X"):
            return move
    
    return random.choice(available_moves)       # Если нет победных ходов, выбираем случайный ход


def play_game()-> None:   # Основная функция игры
   
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)
    
    while True:
        while True:
            row = int(input("Введите номер строки (от 1 до 3): ")) - 1
            col = int(input("Введите номер столбца (от 1 до 3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Некорректный ход. Попробуйте снова.")
        
        display_board(board)
        
        if check_win(board, "X"):             # Проверка выигрыша игрока
            print("Вы победили!")
            break
        
        if all(board[i][j] != " " for i in range(3) for j in range(3)):    # Проверка на ничью
            print("Ничья!")
            break
        
        row, col = bot_move(board)
        board[row][col] = "O"
        print("Ход бота:")
        display_board(board)
        
        if check_win(board, "O"):            # Проверка выигрыша бота
            print("Бот победил!")
            break


print("Игра Крестики-Нолики")
play_game()