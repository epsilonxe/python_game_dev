import pgzrun
import os
import random

class Game():
	def __init__(self):
		self.level = 1
		self.scene = None
		self.fruits = None
		self.popups = None
		self.score = 0

	def level_up(self, addlevel=1):
		self.level += addlevel
		self.set_scene(f'level_{self.level}')

	def set_scene(self, scene_title):
		self.scene = scene_title
		if self.scene == 'game_over':
			music.stop()
			music.play('sadness')
		else:
			n = game.level + 2
			fruits = n * [None]
			popups = n * [Popup()]
			for i in range(n):
				fruits[i] = Fruit(specie='Apple', img='apple')
				fruits[i].id = i
				fruits[i].actor.x = random.randint(20, WIDTH-20)
				fruits[i].actor.y = random.randint(0, HEIGHT-400)
			self.fruits = fruits
			self.popups = popups
			music.stop()
			music.play('jingle')


class Fruit():
	def __init__(self, specie=None, img=None):
		self.id = None
		self.specie = specie
		self.actor = Actor(img)
		self.fall_step = 0.5
		if self.specie == 'Apple':
			self.score = 10
		else:
			self.score = 2
		self.is_shot = False
		self.spawntime = 0

	def fall(self):
		self.actor.y += self.fall_step

	def is_on_ground(self):
		ypos = self.actor.midbottom[1]
		if ypos >= HEIGHT:
			result = True
		else:
			result = False
		return result

class Popup():
	def __init__(self):
		self.text = ''
		self.timer = 0
		self.pos = None
		self.step = random.uniform(0, 0.25)

	def windup(self):
		x = self.pos[0] + random.uniform(-1, 1)
		y = self.pos[1] - self.step
		self.pos = (x, y)

def update():
	if game.scene == 'game_over':
		pass
	else:
		for f in game.fruits:
			f.fall()
			if f.is_on_ground():
				game.is_over = True
				print('GAME OVER')
				game.set_scene('game_over')

		for f in game.popups:
			if f.timer > 0:
				f.windup()


def draw():
	screen.clear()
	if game.scene == 'game_over':
		display_text = f'GAME OVER!\n\nYour score is {game.score} points'
		screen.draw.text(display_text, center=(WIDTH/2, HEIGHT/2))
	else:
		for p in game.popups:
			if p.timer > 0:
				p.timer += 1
				if p.timer <= 60:
					screen.draw.text(p.text, center=p.pos)
				else:
					p.timer = 0
		for f in game.fruits:
			if f.is_shot:
				f.spawntime += 1
				if f.spawntime <= 10:
					f.is_shot = False
					f.spawntime = 0
			else:
				f.actor.draw()
		screen.draw.text(f'SCORE: {game.score:05d}', center=(WIDTH/2, 20))
		screen.draw.text(f'LEVEL {game.level}', topleft=(20, 20))

def on_mouse_down(pos):
	if game.scene == 'game_over':
		pass
	else:
		for f in game.fruits:
			if f.actor.collidepoint(pos):
				sounds.coin.play()
				f.is_shot = True
				game.popups[f.id].pos = pos
				game.popups[f.id].timer = 1
				game.popups[f.id].text = f'+{f.score} Pts'
				game.score += f.score 
				f.actor.x = random.randint(20, WIDTH-20)
				f.actor.y = random.randint(-10, 0)
				f.fall_step += 0.25
				f.score += 5*game.level

				if game.level == 1 and game.score >= 500:
					game.level_up()
				elif game.level == 2 and game.score >= 2000:
					game.level_up()
				else:
					pass

	
WIDTH = 800
HEIGHT = 600
os.environ['SDL_VIDEO_CENTERED'] = '1'
game = Game()
game.set_scene('level_1')
pgzrun.go()