def battleships():
    from random import randint
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    print board, len(board)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print "Let's play Battleships! Try to guess where my battleship is hidden"
    print "Type 'exit' to leave the game at any time"
    print_board(board)

    def random_row(board):
        return randint(0, len(board))

    def random_col(board):
        return randint(0, len(board))

    ship_row =random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        guess_row = raw_input("Guess Row:")
        guess_col = raw_input("Guess Col:")
        if guess_row=='' or guess_col=='':
            print "You're not even trying"
            guess_row = int(raw_input("Guess Row:"))-1
            guess_col = int(raw_input("Guess Col:"))-1
            turn+=1
        elif guess_row=='exit' or guess_col=='exit':
            print "Thanks for playing"
            break
        else:
            guess_row=int(guess_row)-1
            guess_col=int(guess_col)-1
        if guess_row+1 == ship_row and guess_col+1 == ship_col:
            print "Congratulations! You sunk my battleship!"
            board[ship_row][ship_col] = "D"
            req=raw_input("Would you like to play again? y or n")
            if req=='y':
                battleships()
            if req=='n':
                break 
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0         or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            if turn==3:
                    print "Game Over"  
                    board[ship_row-1][ship_col-1] = "D"
                    print_board(board)
                    req=raw_input("Would you like to play again? y or n:")
                    if req=='y':
                        battleships()
                    if req=='n':
                        print "See ya"
                        break
            turn=turn+1
        print_board(board)
