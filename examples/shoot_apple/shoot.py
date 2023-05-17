import pgzrun
import time
import os
import random

WIDTH = 1000
HEIGHT = 600
TIME_COUNT = 0
GAME_LEVEL = 1
GAME_OVER = False
os.environ['SDL_VIDEO_CENTERED'] = '1'
music_switch = 0

apple = Actor('red_apple', center=(random.randint(0, WIDTH), random.randint(0, HEIGHT-500)))
orange = Actor('orange', center=(random.randint(0, WIDTH), random.randint(0, HEIGHT-500)))
pineapple = Actor('pineapple', center=(random.randint(0, WIDTH), random.randint(0, HEIGHT-500)))
quit_box = Rect((WIDTH-100,HEIGHT-50), (WIDTH, HEIGHT))
music.play('jingle')


def draw():
	global GAME_OVER
	global music_switch
	screen.clear()
	if GAME_OVER:
		if music_switch == 0:
			music.stop()
			music.play('sadness')
			music_switch = 1
		gameover()
		screen.draw.rect(quit_box, (0,0,0))
	else:
		apple.draw()
		orange.draw()
		pineapple.draw()

def place(fruit, x, y):
	fruit.x = x
	fruit.y = y

def on_mouse_down(pos):
	global GAME_LEVEL
	global GAME_OVER
	if GAME_OVER:
		if quit_box.collidepoint(pos):
			print('Quit game')
			quit()
	else:
		for f in [apple, orange, pineapple]:
			if f.collidepoint(pos):
				print('Good Shot!')
				sounds.slash.play()
				GAME_LEVEL += 1
				print(f'GAME_LEVEL = {GAME_LEVEL}')
				place(f, random.randint(0, WIDTH), random.randint(0, HEIGHT-500))
			else:
				print('You missed')

def fall(fruit):
	global TIME_COUNT
	global GAME_LEVEL
	global GAME_OVER
	fall_time = 10
	if TIME_COUNT == fall_time:
		TIME_COUNT = 0
		place(fruit, fruit.x, fruit.y + GAME_LEVEL)
		if fruit.midbottom[1] >= HEIGHT:
			GAME_OVER = True
			print('GAME OVER!')
	else:
		TIME_COUNT += 1


def update():
	global GAME_OVER
	if not GAME_OVER:
		for f in [apple, orange, pineapple]:
			fall(f)

def gameover():
	global GAME_LEVEL
	screencenter = (WIDTH/2, HEIGHT/2)
	screen.draw.text('GAME OVER', center=screencenter)
	screencenter = (WIDTH/2, HEIGHT/2 + 20)
	screen.draw.text(f'AT THE LEVEL {GAME_LEVEL}', center=screencenter)
	
	qpos = (WIDTH-50, HEIGHT-25)
	screen.draw.text('QUIT?', center=qpos)
	


	
pgzrun.go()