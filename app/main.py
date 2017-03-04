import bottle
import os
import random
import directions

#def initial(data):
#	grid = [[0 for col in xrange(data['height'])] for row in xrange(data['width'])]

def distance(x, y):
	x_steps = abs(x[0]-y[0])
	y_steps = abs(y[1]- x[1])
	return x_steps + y_steps;
	
def food_path():
	

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    print(data)

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': 'gold',
        'taunt': 'gg',
        #'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': 'shades',
        'tail_url': 'skinny-tail',
        'name': 'battlesnake-python'

    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    parsedMapData = []
    otherSnakes = []
    ourSnakeId = data['you']
    for snake in data['snakes']:
        if snake['id'] == ourSnakeId:
            ourSnake = snake
        else:
            otherSnakes.append(snake)
    food = data['food']
    dirsCanGo = directionsCanGo( parsedMapData, ourSnake, mapHeight, mapWidth, otherSnakes, food)
    currMove = dirsCanGo[random.randint(0, len(dirsCanGo)-1)]

    return {
        'move': currMove,
        'taunt': 'Direction: {}'.format(currMove)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
