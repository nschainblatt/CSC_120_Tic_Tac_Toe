def main():
    print()
    print("Printing board...")
    game_board = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])
    current = game_board
    while True:
        # Player 1
        player = 1
        print("Player 1, make your move")
        row = int(input("Enter row nos (0-2): "))
        col = int(input("Enter col nos (0-2): "))

        while row < 0 or row >= 3 or col < 0 or col >= 3:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            print_board(current)
            print()
            print("Player 1, make your move")
            row = int(input("Enter row nos (0-2): "))
            col = int(input("Enter col nos (0-2): "))
        taken = check_existing(row, col, game_board)
        while taken:
            print(f"**** Board [{row}][{col}] has already been selected. Please somewhere else on the board ****")
            print("**** Invalid choice. Please mark again! ****")
            print_board(current)
            print()
            print("Player 1, make your move")
            row = int(input("Enter row nos (0-2): "))
            col = int(input("Enter col nos (0-2): "))
            taken = check_existing(row, col, game_board)
        print()
        print(f"Player 1 added mark at the location {row}, {col}")
        current = board_changes(player, row, col, game_board)
        print_board(current)
        print()

        # Player 2
        player = 2
        print("Player 2, make your move")
        row = int(input("Enter row nos (0-2): "))
        col = int(input("Enter col nos (0-2): "))

        while row < 0 or row >= 3 or col < 0 or col >= 3:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            print_board(current)
            print()
            print("Player 2, make your move")
            row = int(input("Enter row nos (0-2): "))
            col = int(input("Enter col nos (0-2): "))
        taken = check_existing(row, col, game_board)
        while taken:
            print(f"**** Board [{row}][{col}] has already been selected. Please somewhere else on the board ****")
            print("**** Invalid choice. Please mark again! ****")
            print_board(current)
            print()
            print("Player 2, make your move")
            row = int(input("Enter row nos (0-2): "))
            col = int(input("Enter col nos (0-2): "))
            taken = check_existing(row, col, game_board)
        print()
        print(f"Player 2 added mark at the location {row}, {col}")
        current = board_changes(player, row, col, game_board)
        print_board(current)
        print()


def check_existing(r, c, b):
    if b[r][c] == 'X' or b[r][c] == 'O':
        return True
    else:
        return False


def board_changes(p, r, c, b):
    if p == 1:
        b[r][c] = 'X'
    if p == 2:
        b[r][c] = 'O'
    winner(b)
    return b


def print_board(b):
    print("Printing board...")
    print(b[0])
    print(b[1])
    print(b[2])


def winner(board):
    # horizontal
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and \
            board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print("Player 1 wins!")
        exit()

    elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0' or board[1][0] == '0' and board[1][
        1] == '0' and board[1][2] == '0' or board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print("Player 2 wins!")
        exit()

    # Vertical
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][1] == 'X' and board[1][
        1] == 'X' and board[2][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print("Player 1 wins!")
        exit()

    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0' or board[0][1] == '0' and board[1][
        1] == '0' and board[2][1] == '0' or board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
        print("Player 2 wins!")
        exit()

    # Diagonal
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][
        1] == 'X' and board[2][0] == 'X':
        print("Player 1 wins!")
        exit()

    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0' or board[0][2] == '0' and board[1][
        1] == '0' and board[2][0] == '0':
        print("Player 2 wins!")
        exit()


main()
