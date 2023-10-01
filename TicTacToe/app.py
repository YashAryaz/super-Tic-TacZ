from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Define the game board (global variable)
initial_board = [' ' for _ in range(9)]
board = list(initial_board)  # Initialize the board
def reset_board():
    global board
    board = list(initial_board)



# Define a new route for resetting the game board
@app.route('/reset_game', methods=['POST'])
def reset_game():
    reset_board()
    return jsonify({'message': 'Game board has been reset.'})
# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    # Check if the board is full (draw)
    if ' ' not in board:
        return True
    return False

# Function to evaluate the game state for the AI
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == 'O':
            return 1  # AI wins
        elif board[condition[0]] == board[condition[1]] == board[condition[2]] == 'X':
            return -1  # Player wins
    return 0  # Draw or game still ongoing

# Minimax algorithm for AI's move
def minimax(board, depth, maximizing_player):
    if is_game_over(board):
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# AI's move using Minimax
def ai_move(board):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Define the route for the game page
@app.route('/')
def game():
    return render_template('index.html', board=board,game_over=is_game_over(board))

# Define an API endpoint for making a move
@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    player_move = data['player_move']
    
    # Validate and update the game board based on the player's move
    if board[player_move] == ' ':
        board[player_move] = 'X'
    
    # Check for game over
    game_over = is_game_over(board)
    if game_over:
        winner = evaluate(board)
        if winner == 1:
            result = "AI wins!"
        elif winner == -1:
            result = "Player wins!"
        else:
            result = "It's a draw!"
    else:
        # Perform AI move
        ai_best_move = ai_move(board)
        board[ai_best_move] = 'O'
        game_over = is_game_over(board)
        if game_over:
            winner = evaluate(board)
            if winner == 1:
                result = "AI wins!"
            elif winner == -1:
                result = "Player wins!"
            else:
                result = "It's a draw!"
        else:
            result = ""
    
    response_data = {
        'board': board,  # Return the updated game board
        'game_over': game_over,  # Indicate if the game is over
        'result': result  # Indicate the result of the game
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
