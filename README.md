# French Trivia Bingo
#### Video Demo:  <URL HERE>

## Description
### General
This project helps with running a French themed trivia bingo. The web application automates the random selection of questions during the game as well as the random generation of bingo boards for convenient printing.

### The Game
- Typical bingo style game: 5 across a row/column/diagonal is a win
- There is a FREE space in the very center of the board, which the user can automatically fill at the beginning of the game
- Instead of directly calling out numbers, trivia questions will be called out with corresponding answers in the squares on the board
- In order to preserve player attention, the answers to each question will be revealed in a table once two additional questions have been read 
  - This way, players won't be as discouraged if they don't know the answer, though players who do know the answer will gain a slight advantage
- The host can decide to play until the first bingo, until multiple bingos, or until a blackout (all boxes are filled)

## Files
### application.py
This Python file is the main controller of the Flask application and handles all of the random generation.

The file first reads in the list of questions into a Python dictionary. The user is immediately landed on the index page, where they can choose to begin a game or generate boards.

Once a game begins, the application selects random questions to display and also keeps a running list of past questions and their answers. Clicking the "Begin" button also resets any past game in progress. If the user chooses to generate boards, they are prompted to enter in an amount, after which that amount of printable boards (letter sized) will be randomly generated.

### questions.csv
This file contains a list of 30 questions and their answers, pulled from the Alabama Federation of French Clubs French Convention Scholars Bowl question pool. The questions were intentionally selected to be fairly easy so that even non-French students can have a fair chance.

### requirements.txt
The only extra library necessary for the application is Flask.

### static/favicon.ico
A French flag icon for the title of the page.

### static/styles.css
Adapted from the CS50 Finance problem set css template with slight modifications to better fit this specific application, such as changing fonts and fixing table sizes.

### static/printstyle.css
Special css file for the Generate function that formats the page more adequately for printing.

### templates/layout.html
Adapted from the CS50 Finance problem set template with slight modifications to suit the application.

### templates/index.html
From here, the user can choose to begin a game or generate boards.

### templates/game.html
Displays the ongoing game, with the current question at the top and a Next button for proceeding to the next question. Also keeps a table of past questions and answers in the current game.

### templates/generate.html
Prompts the user for how many boards to generate.

### templates/boards.html
Randomly generates as many boards as necessary in a convenient format for printing (letter size paper).