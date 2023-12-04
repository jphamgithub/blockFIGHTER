# blockFIGHTER

## Getting Started

These instructions will get you a copy of the game up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the game, make sure you have Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Additionally, you need to have Pygame installed, which is a set of Python modules designed for writing video games. Install Pygame using pip:


bash:
```
pip install pygame
```
## Installation
To play blockFIGHTER, you need to clone the repository from GitHub and run the game using Python.
Open your terminal and clone the repository using the following command:

```
git clone https://github.com/jphamgithub/blockFIGHTER.git
```

Change the directory to the repository folder:

```
cd blockFIGHTER
```

Run the Game
Now, you can run the game using Python:
```
python blockFIGHTER.py
```

This command will start the game, and you should see the game window open.

**If this fails. Try just navigating to the game in Windows File Explorer and double clicking the python file!**

Enjoy playing blockFIGHTER!

## Play in Docker

Now with Docker support! If you're OVER installing more and more dependencies just use Docker and be done with it! No more installing pygame just to beat up some blocks.

```
git clone https://github.com/jphamgithub/blockFIGHTER
cd blockFIGHTER
docker build -t blockfighter .
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix blockfighter
```
