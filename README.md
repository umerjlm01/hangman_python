

## 🕵️ Hangman Game in Python

This is a simple **command-line Hangman game** implemented in Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time within a limited number of attempts.

### ✅ Features

* **Random Word Selection:** Loads a random word from a predefined word list (`words.py`).
* **User Input Handling:** Takes letter guesses from the user, validating inputs.
* **Lives System:** Player has 6 lives; each wrong guess reduces one life.
* **Progress Display:** Shows the current guessed state of the word.
* **Win/Loss Messages:** Displays a message depending on whether the user wins or loses.

### 💡 How it Works

1. A word is randomly selected from the `words` list.
2. The player tries to guess the word by suggesting letters.
3. For each incorrect guess, the player loses a life.
4. The game continues until the word is fully guessed or the player runs out of lives.

### 📁 Requirements

* Python 3.x
* A `words.py` file containing a list of valid words:

  ```python
  words = ["python", "hangman", "developer", "code", "algorithm"]
  ```

### ▶️ Run the Game

```bash
python hangman.py
```


