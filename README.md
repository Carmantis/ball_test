# Ball Test Game (Pallo Koe)

A simple Pygame application that demonstrates random movement generation and collision detection mechanics using colored balls.

## 🎮 Description

**Finnish (Suomi):**
Pallo kokeen tarkoitus on testata satunnaisgeneraattoria pallon liikuttamiseen. Pallo liikkuu satunnaisesti. Osuessaan vihreään palloon se kasvaa ja vastaavasti osuessaan punaiseen se pienenee.

**English:**
This ball test game demonstrates random number generation for ball movement. A blue ball moves randomly around the screen. When it collides with green balls, it grows larger, and when it collides with red balls, it shrinks.

## ✨ Features

- **Random Movement**: Blue ball moves randomly around the screen using a random generator
- **Collision Detection**: Detects collisions between the blue ball and other colored balls
- **Dynamic Size Changes**:
  - Hitting green balls increases the blue ball's size
  - Hitting red balls decreases the blue ball's size
- **10 Red Balls**: Obstacles that shrink the player's ball
- **10 Green Balls**: Power-ups that grow the player's ball
- **Boundary Collision**: Ball stays within screen boundaries

## 🎯 Game Rules

1. A blue ball moves randomly around the screen
2. **Green Balls** (10): Colliding with these makes your blue ball grow
3. **Red Balls** (10): Colliding with these makes your blue ball shrink
4. The game continues until you close the window

## 🛠️ Requirements

- Python 3.x
- Pygame library

## 📦 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ball_test
```

2. Install the required dependencies:
```bash
pip install pygame
```

## 🚀 How to Run

Run the game using Python:

```bash
python koepallo.py
```

Or on some systems:

```bash
python3 koepallo.py
```

## 🎲 Technical Details

### Game Configuration

- **Screen Size**: 800x600 pixels
- **Initial Ball Radius**: 20 pixels
- **Blue Ball Speed**: 5 pixels per move
- **Size Change on Red Ball Hit**: -2 pixels
- **Size Change on Green Ball Hit**: +4 pixels
- **Maximum Growth**: 2x the growth increment
- **Frame Rate**: 60 FPS

### Colors

- Background: Black (0, 0, 0)
- Player Ball: Blue (0, 0, 255)
- Shrink Balls: Red (255, 0, 0)
- Grow Balls: Green (0, 255, 0)

### Code Structure

The main game file `koepallo.py` includes:
- Pygame initialization and display setup
- Ball properties and color definitions
- Random ball placement for red and green balls
- Main game loop with:
  - Event handling (window close)
  - Random movement generation
  - Collision detection using Euclidean distance
  - Size adjustment logic
  - Ball rendering

## 🎨 How It Works

1. **Random Movement**: The blue ball chooses a random direction (x: -1, 0, or 1; y: -1, 0, or 1) each frame
2. **Collision Detection**: Uses Euclidean distance formula to detect when balls touch:
   ```python
   distance = sqrt((x2 - x1)² + (y2 - y1)²)
   ```
3. **Size Adjustment**: Ball size changes when collision is detected with red or green balls

## 📝 License

This is a test/educational project demonstrating basic Pygame mechanics.

## 🤝 Contributing

This is a test project, but feel free to fork and experiment with the code!

## 📧 Contact

For questions or suggestions, please open an issue in the repository.
