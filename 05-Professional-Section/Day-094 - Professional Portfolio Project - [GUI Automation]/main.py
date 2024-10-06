import AppKit
import pyautogui
import time
import webbrowser
from PIL import ImageGrab

GAME_URL = "https://elgoog.im/t-rex/"
GAME_AREA = (0, 400, 1500, 750)
CACTUS_COLOR_THRESHOLD = (100, 100, 100)
SLEEP_TIME = 0.1
PIXEL_STEP = 5
CHECK_HEIGHT = 200

def detect_obstacle():
    """Detects if there is an obstacle in the defined game area."""
    try:
        screen = ImageGrab.grab()
        screen = screen.convert('RGB')

        for x in range(450, 750, PIXEL_STEP):
            for y in range(625, 700, PIXEL_STEP):
                r, g, b = screen.getpixel((x, y))
                if r != 255 or g != 255 and b != 255:
                    return True
        return False
    except Exception as e:
        print(f"Error detecting obstacle: {e}")
        return False

def jump():
    """Simulates a jump by pressing the space bar."""
    pyautogui.press('space')
    time.sleep(SLEEP_TIME)

def open_game():
    """Opens the T-Rex game in the default web browser."""
    print("Opening the T-Rex game...")
    webbrowser.open(GAME_URL)
    time.sleep(5)

def play_game():
    """Main loop to run the T-Rex game."""
    print("Starting the T-Rex game automation...")
    time.sleep(5)
    jump()
    while True:
        if detect_obstacle():
            print("Obstacle detected! Jumping...")
            jump()

if __name__ == "__main__":
    try:
        open_game()
        play_game()
    except KeyboardInterrupt:
        print("Game automation stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

