# super-Tic-TacZ
This Tic-Tac-Toe game is a simple demonstration of how a basic AI opponent can be implemented using the Minimax algorithm. It serves as a starting point for more complex AI implementations and web-based games.

## Prerequisites
Make sure you have Python 3.x installed on your system. You can download Python from the official website.

## Installation
Clone or download this repository to your local machine.

Navigate to the project directory in your terminal:

``` bash
pip install -r requirements.txt
```

## Running the Game
Start the Flask application:

```bash
python app.py
```

Open a web browser and go to http://localhost:5000/ to play the game.

### How to Play
The game is played on a 3x3 grid.
You are "X," and the AI opponent is "O."
Click on any empty cell on the game board to make your move.
The AI opponent will make its move automatically.
The game ends when either you or the AI wins, or it's a draw.
Resetting the Game
You can reset the game at any time by clicking the "Reset Game" button.
Files and Structure
app.py: The main Python file containing the Flask application and game logic.
templates/index.html: The HTML template for the game interface.
static/styles.css: Custom CSS styles for the game board.
README.md: This readme file.
Game Logic
The game logic is implemented in the app.py file.
The AI opponent uses the Minimax algorithm to make its moves.
The game checks for win conditions, draws, and game over scenarios.
Technologies Used
Python 3.x
Flask (Python web framework)
HTML
CSS
JavaScript

