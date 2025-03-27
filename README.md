# Rock-Paper-Scissors Simulation

A dynamic, visually engaging Rock-Paper-Scissors simulation where emojis bounce, collide, and evolve based on classic game rules. The game runs in a controlled environment with real-time tracking and an intuitive interface.

## Features
- **Interactive Simulation**: Emojis move inside a box, bouncing off walls and colliding based on Rock-Paper-Scissors rules.
- **User Input**: Enter a count (2-50) to determine the initial number of Rock, Paper, and Scissors emojis.
- **Real-Time Counter**: A live counter in the left panel tracks the remaining count of each type.
- **Win Condition**: The game continues until only one type remains, declaring it the winner.
- **Timeout Mechanism**: If no winner is determined within 2 minutes, the game ends in a draw.

## How to Play
1. Launch the program.
2. Enter a number (2-50) in the left panel and press **Enter**.
3. Watch the emojis move, collide, and transform.
4. The game ends when only one type remains, or after 2 minutes.
5. The winner is displayed in the left panel.

## Requirements
- Python 3.x
- Pygame (`pip install pygame`)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/rock-paper-scissors-sim.git
   cd rock-paper-scissors-sim
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```
3. Run the game:
   ```sh
   python game.py
   ```

## Customization
- Adjust **TIMEOUT** in the script to modify the game duration.
- Change emoji symbols for different visual effects.

## License
This project is open-source under the MIT License.

