import pgzrun

WIDTH = 800
HEIGHT = 600

apple = Actor('apple', center=(600, 100))

def update():
	apple.y += 0.5
	
def draw():
	screen.clear()
	apple.draw()

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print('Good Shot!')
	else:
		print('Miss Shot')

pgzrun.go()