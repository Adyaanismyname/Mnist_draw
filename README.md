# MNIST Letter Prediction Game

Welcome to the MNIST Letter Prediction Game! This project allows users to draw letters on a 28x28 grid and predicts the letter using a pre-trained MNIST neural network model.

## Project Overview

This game uses a simple Pygame interface where users can draw on a 28x28 board. After drawing, users can press the "Predict" button to see the predicted letter using the MNIST model. The model is pre-trained and saved as `mnist_model.h5`.

## Features

- **Draw Letters:** Use the mouse to draw on the board.
- **Predict Button:** Predicts the letter drawn on the board using the MNIST model.
- **Clear Button:** Clears the board for a new drawing.

## Requirements

- Python 3.x
- Pygame
- TensorFlow
- NumPy

You can install the necessary Python packages using pip:

```bash
pip install pygame tensorflow numpy
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Adyaanismyname/Mnist_game.git
   cd Mnist_game
   ```
2. **Run the Game**

   ``` bash
   python main.py
   ```
## How It Works

# Drawing on the Board:

Use the left mouse button to draw on the 28x28 grid. The grid is represented as a 28x28 block canvas where each block can be colored white.
 
# Predicting:

Press the "Predict" button to save the current drawing as a PNG file. The image is then processed and fed into the pre-trained MNIST model to predict the digit.

# Clearing the Board:

Press the "Clear" button to reset the board and start a new drawing.



