import pgzrun
import random

WIDTH = 800
HEIGHT = 500


hole = 5 * [None]
hole[0] = Actor('hole', center=(10+WIDTH/4, HEIGHT/2))
hole[1] = Actor('hole', center=(10+2*WIDTH/4, HEIGHT/2))
hole[2] = Actor('hole', center=(10+3*WIDTH/4, HEIGHT/2))
hole[3] = Actor('hole', center=(120+1*WIDTH/4, HEIGHT/2+150))
hole[4] = Actor('hole', center=(120+2*WIDTH/4, HEIGHT/2+150))


mole = Actor('mole')
mole_timer = 0
mole_hole = random.randint(0, 4)
mole_state = 0
score = 0

music.play('itty_bitty')

def update():
	global mole_timer
	global mole_hole
	global mole_state

	mole_timer += 1
	if mole_state == 0:
		mole_hole = random.randint(0, 4)
	if mole_state == 0 and mole_timer >= 60:
		mole_state = 1
		mole.image = 'half_mole'
		mole.x = hole[mole_hole].x - 5
		mole.y = hole[mole_hole].y - 27
	if mole_timer == 159:
		mole_hole = random.randint(0, 4)
		mole.x = hole[mole_hole].x - 5
		mole.y = hole[mole_hole].y - 27
	if mole_state == 1 and mole_timer >= 240:
		mole_hole = random.randint(0, 4)
		mole_state = 2
		mole.image = 'mole'
		mole.x = hole[mole_hole].x - 5
		mole.y = hole[mole_hole].y - 50
	if mole_state == 2 and mole_timer >= 360:
		mole_state = 0
		mole_timer = 0
	if mole_state == 3 and mole_timer >= 60:
		mole_state = 0
		mole_timer = 0

def draw():
	global mole_timer
	global mole_state
	global score
	
	screen.clear()
	screen.fill((90,160,0))
	screen.blit('background', (0,0))

	if mole_state != 0:
		if mole_state == 1:
			if (70 <= mole_timer <= 120) or (160 <= mole_timer <= 220):
				mole.draw()
		elif mole_state == 2 and (250 <= mole_timer <= 320):
			mole.draw()
		else:
			pass
	
	for h in hole:
		h.draw()
		if mole_state == 3 and mole_timer < 25:
			mole.draw()

	screen.draw.text(f'TIMER: {mole_timer:03d}\n\nSTATE: {mole_state}', topleft=(20,20), owidth=2, ocolor='black')
	screen.draw.text(f'SCORE: {score:05d}', topright=(WIDTH-20, 20), owidth=2, ocolor='black')

def on_mouse_down(pos):
	global mole_state
	global mole_hole
	global mole_timer
	global score

	if mole.collidepoint(pos) and mole_state == 2:
		score += 100
		mole_state = 3
		mole.image = 'boom'
		mole_timer = 0
		sounds.boom.play()
	else:
		pass

pgzrun.go()