import pgzrun
import random

WIDTH = 800
HEIGHT = 600

apple = Actor('apple', center=(600, 100))
pineapple = Actor('pineapple', center=(100, 300))

def update():
	apple.y += 0.5
	pineapple.y +=0.5
	
def draw():
	screen.clear()
	apple.draw()
	pineapple.draw()

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print('Apple Shot!')
		apple.x = random.randint(20, 780)
		apple.y = random.randint(0, 50)
	else:
		print('Miss Shot')

	if pineapple.collidepoint(pos):
		print('Pineapple Shot!')
		pineapple.x = random.randint(20, 780)
		pineapple.y = random.randint(0, 50)
	else:
		print('Miss Shot')

pgzrun.go()