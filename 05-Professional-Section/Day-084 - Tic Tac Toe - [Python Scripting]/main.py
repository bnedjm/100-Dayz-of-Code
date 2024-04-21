import click

# Define constants for player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    for row in board:
        click.echo(' | '.join(row))
        click.echo('- ' * 5)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    return (any(all(cell == player for cell in row) for row in board) or
            any(all(board[i][j] == player for i in range(3)) for j in range(3)) or
            all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3)))

# Function to check for a draw
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to handle player input
def get_player_move(board, player):
    while True:
        try:
            move = click.prompt(f"Player {player}, enter your move (row column)", type=str)
            row, col = map(int, move.split())
            if 1 <= row < 4 and 1 <= col < 4 and board[row-1][col-1] == ' ':
                return row-1, col-1
            else:
                click.echo("Invalid move. Please try again.")
        except ValueError:
            click.echo("Invalid input. Please enter row and column numbers separated by space.")

# Main game loop
def main():
    board = initialize_board()
    current_player = PLAYER_X

    while True:
        display_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            click.echo(f'Player {current_player} wins!')
            break
        elif check_draw(board):
            display_board(board)
            click.echo('The game is a draw!')
            break

        # Switch players
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    # Ask if players want to play again

if __name__ == "__main__":
    main()
