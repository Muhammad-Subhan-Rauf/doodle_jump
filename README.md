[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Th8mt3_7)
# Assignment 2: Doodle Jump

You are given skeletal code for a game called Doodle Jump. The game is a simple platformer where the player controls a character that can jump on platforms. The game is played by using the arrow keys to move the character left and right. The character will automatically jump when it lands on a platform. The goal of the game is to jump as high as possible without falling off. The game is over when the character falls off the screen.

**Starter Code:** If you run this game you will see a window in portrait aspect ratio. This is the start state. The game is not yet implemented. Your task is to implement the game so that it behaves as described above.

You can play the online doodle jump game here:

[https://doodlejump.io/](https://doodlejump.io/).

# Game Requirements

The game should have the following features:

## Game States _[15 points]_
1. **Main Menu:** The game should have a main menu that displays the title of the game and a play button. The game should transition to the play state when the play button is clicked.
2. **Game Play:** The game should have a play state where the character can move left and right and jump on platforms. The game should transition to the game over state when the character falls off the screen.
    - Must be able to pause and unpause the gameplay.
3. **Game Over:** The game should have a game over state that displays the final score and a play again button. The game should transition to the play state when the play again button is clicked.

## Game Play Mechanics _[25 points]_
1. The main character that can move left and right using the arrow keys.
    - If the character moves off the screen to the left, it should reappear on the right side of the screen and vice versa.
2. The character should jump automatically when it lands on a platform.
    - The character is jumping under the influence of gravity, so it should fall back down after reaching the peak of its jump.
3. The game should have platforms that the character can jump on, randomly spawn at different positions.
    - Make sure the platforms are not too far apart, so the character can jump from one to the other.
    - Everytime there should be a different level procedurally generated.
4. The game should have a score that increases as the character jumps on platforms.
    - The score should be displayed on the screen.
5. The game should end when the character falls off the screen.

## Graphics _[15 points]_
This time it is up to you to find suitable graphics or create your own. You can also use the images from the original game as a reference.

Following are some of the assets you can use:
- [https://opengameart.org](https://opengameart.org)
- [https://itch.io/game-assets/free](https://itch.io/game-assets/free)
- [https://www.gameart2d.com/freebies.html](https://www.gameart2d.com/freebies.html)

## Sound _[10 points]_
You can use bfxr to create your own sound effects for the game.

- [https://www.bfxr.net/](https://www.bfxr.net/)

Some sites where you can find free sound effects:
- [https://freesound.org/](https://freesound.org/)

Good quality free music:
- [https://incompetech.com/](https://incompetech.com/)


# Bonus _[25 points]_
1. **High Score:** Implement a high score system that saves the highest score to a file and displays it on the main menu.
2. **Power-ups:** Implement power-ups that the character can collect to increase its score or jump higher.
    - For example, you could implement a spring power-up that allows the character to jump higher.
3. **Enemies:** Implement enemies that the character must avoid.
4. **Gun:** Note that in the original game, if you tap on the screen, the character shoots bullets out of its nose. Implement a similar feature in your game.
5. **Moving Platforms:** Implement platforms that move left and right or up and down.


# _[Optional]_ pygame installation

In cases where `pygame` is giving trouble installing, you can try out the following steps:

1. Create a new virtual environment

```
python3 -m venv venv
```

2. Activate the virtual environment

```
source venv/bin/activate
```

3. Install pygame

```
pip3 install pygame
```
