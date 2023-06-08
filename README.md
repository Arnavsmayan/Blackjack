# Blackjack Game

This repository contains a command-line blackjack game implemented in Python. The game allows you to play a simplified version of the popular casino card game against the computer.

## How to Play

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/blackjack-game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blackjack-game
   ```

3. Run the game by executing the main Python file:

   ```bash
   python blackjack.py
   ```

4. Follow the on-screen instructions to play the game. You will be prompted to make decisions such as hitting or standing during your turn. The goal is to get as close to 21 as possible without going over.

5. Enjoy the game and try to beat the dealer!

## Code

The game code is implemented in the `blackjack.py` file. It uses the following libraries and modules:

```python
import random
import sys
```

The game logic is organized into functions and includes:

- `dealHand(hand)`: Deals a card to the specified hand by randomly selecting a card from the deck and removing it from the deck. The function returns the updated hand.
- `total(hand)`: Calculates the total value of the cards in the specified hand. It accounts for face cards (J, Q, K) and the special case of the Ace (A), which can be counted as either 1 or 11 depending on the total value of the hand.

The main gameplay section deals the initial cards to the player and the dealer, and then proceeds with the game loop. The loop allows the player to choose whether to hit or stand. If the player's total exceeds 21, the player loses. When the player stands, the dealer's logic comes into play. The dealer continues to draw cards until their total is at least 16. If the dealer's total exceeds 21, the player wins. Finally, the total values of the player's and dealer's hands are compared, and the outcome of the game is displayed.

Please refer to the `blackjack.py` file in this repository for the complete code implementation.

## Project Structure

The repository is organized as follows:

- `blackjack.py`: The main Python file containing the game logic and user interface.
- `README.md`: A Markdown file describing the project and providing instructions.

## Dependencies

This game has no external dependencies. It is implemented using Python's built-in libraries and modules only. Therefore, you do not need to install any additional packages to run the game.

## Contributing

Contributions to this blackjack game are welcome! If you find any bugs, have suggestions for improvements, or would like to add new features, please open an issue or submit a pull request to the repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the terms of the license.

## Acknowledgements

- The game was developed by Arnav Jain as a personal project.
- Thanks to the open-source community for providing resources and inspiration.
