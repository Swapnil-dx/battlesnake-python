import bottle
import os
import random
from directions import *

board_width = 0
board_height = 0
game_id = 0
taunts = [
	"Y'all gold diggers!",
	"LOL Benis :DDD",
	"Punish me Daddy",
	"ur a nrd",
	"cash me ousside",
	"send noots",
	"Quik it up"
]

def findFood(data, mySnake):
	dirGo = []
	minD = 1000
	bestFood = None
	myCoords = mySnake['coords'][0]
	for coords in data['food']:
		distanceF = distance(myCoords, coords)
		if(distanceF < minD):
			minD = distanceF
			bestFood = coords
	if((bestFood[0] - myCoords[0]) < 0):
		dirGo.append('left')
	elif((bestFood[0] - myCoords[0]) > 0):
		dirGo.append('right')
	if((bestFood[1] - myCoords[1]) < 0):
		dirGo.append('up')
	elif((bestFood[1] - myCoords[1]) > 0):
		dirGo.append('down')	
	return dirGo
	
def distance(x, y):
	x_steps = abs(x[0]-y[0])
	y_steps = abs(y[1]- x[1])
	return x_steps + y_steps;
	

@bottle.route('/static/<path:path>')
def static(path):
	return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
	data = bottle.request.json
	game_id = data['game_id']
	board_width = data['width']
	board_height = data['height']

	head_url = '%s://%s/static/pic.png' % (
		bottle.request.urlparts.scheme,
		bottle.request.urlparts.netloc
	)


    # TODO: Do things with data

	return {
		'color': 'gold',
		'taunt': "y'all gold diggers!",
		#'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
		'head_url': head_url,
		'head_type': "shades",
		'tail_type': "skinny-tail",
		'name': 'Steve the Snek'
    }


	

@bottle.post('/move')
def move():
	data = bottle.request.json

    # TODO: Do things with data
	directions = ['up', 'down', 'left', 'right']

	parsedMapData = []
	otherSnakes = []
	ourSnakeId = data['you']
	ourSnake = None
	for snake in data['snakes']:
		if snake['id'] == ourSnakeId:
			ourSnake = snake
		else:
			otherSnakes.append(snake)
	food = data['food']
	dirsCanGo = directionsCanGo( parsedMapData, ourSnake, board_height, board_width, otherSnakes, food)
	
	dirsWantGo = None
	finalChoice = []
	
	if(ourSnake['health_points'] < 65):
		dirsWantGo = findFood(data, ourSnake)
		for dir1 in dirsCanGo:
			for dir2 in dirsWantGo:
				if(dir1 == dir2):
					finalChoice.append(dir1)
	else:
		finalChoice = dirsCanGo

	return {
		'move': random.choice(finalChoice),
		'taunt': random.choice(taunts)
	}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
	bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
