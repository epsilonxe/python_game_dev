import pgzrun
import random

WIDTH = 1000
HEIGHT = 800

apple = Actor('apple', center=(WIDTH/2, HEIGHT/2))


def update():
	apple.y += 0.5


def draw():
	screen.clear()
	apple.draw()


def on_mouse_down(pos):
	if apple.collidepoint(pos):
		apple.x = random.randint(0, WIDTH)
		apple.y = random.randint(0, HEIGHT)
	else:
		print('You missed ...')


pgzrun.go()