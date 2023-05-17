import pgzrun
import random
import numpy as np

WIDTH = 800
HEIGHT = 600

apple = Actor('apple', center=(400, 100))

t = 0
time = 0
counter = 0

def update():
	global t
	global time
	global counter
	apple.x = 400 + 300*np.cos(np.pi * t)
	apple.y = 300 + 200*np.sin(np.pi * t)
	t += 0.25/60
	counter += 1
	if counter == 60:
		time += 1
		counter = 0
	
def draw():
	global t
	screen.clear()
	apple.draw()
	screen.draw.text(f'TIME = {time:05d}\nt = {t:.05f}', center=(700, 50))

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print('Good Shot!')
		apple.x = random.randint(20, 780)
		apple.y = random.randint(0, 50)
	else:
		print('Miss Shot')

pgzrun.go()