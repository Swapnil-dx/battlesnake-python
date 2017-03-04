def directionsCanGo(mapdata, ourSnake, mapHeight, mapWidth, otherSnakes, food):
    #if len(ourSnake.coords) == 0:
    
    #    return
    canGo = ['up', 'left', 'down', 'right']
    # Code to decide which dirs we can go
    head = ourSnake['coords'][0]
    #length = len(ourSnake.coords)
    print head
    #-----WALLS-----
    
    #if head co-ord x is 0, cant move up
    if head[0] == 0:
        canGo.remove('up')
    
    #if head co-ord x is height-1 cant move down
    if head[0] == mapHeight-1:
        canGo.remove('down')
        
    #if head co-ord y is 0, cant move left
    if head[1] == 0:
        canGo.remove('left')
        
    #if head co-ord y is  width - 1 cant more right 
    if head[1] == mapWidth-1:
        canGo.remove('right')
    print str(canGo)
    #-----Ourselves-----
    del ourSnake['coords'][-1]    
    for coord in ourSnake['coords']:
        if coord == head:
            continue
        if (coord[1] - head[1] == 1) and (coord[0] - head[0] == 0):
            if 'down' in canGo:
                canGo.remove('down')
        if (coord[0] - head[0] == 1) and (coord[1] - head[1] == 0):
            if 'right' in canGo:
                canGo.remove('right')
        if (coord[1] - head[1] == -1) and (coord[0] - head[0] == 0):
            if 'up'  in canGo:
                canGo.remove('up')
        if (coord[0] - head[0] == -1) and (coord[1] - head[1] == 0):
            if 'left' in canGo:
                canGo.remove('left')

    #-----Other Snakes -----
    for snake in otherSnakes:
        del snake['coords'][-1]
        for coord in snake['coords']:
            if (coord[1] - head[1] == 1) and (coord[0] - head[0] == 0):
                if 'down' in canGo:
                    canGo.remove('down')
            if (coord[0] - head[0] == 1) and (coord[1] - head[1] == 0):
                if 'right' in canGo:
                    canGo.remove('right')
            if (coord[1] - head[1] == -1) and (coord[0] - head[0] == 0):
                if 'up'  in canGo:
                    canGo.remove('up')
            if (coord[0] - head[0] == -1) and (coord[1] - head[1] == 0):
                if 'left' in canGo:
                    canGo.remove('left')
                    
    for snake in otherSnakes:
        if (snake['coords'][0][0] - head[0] == 2) and (snake['coords'][0][1] == head[1]):
            if 'right' in canGo:
                canGo.remove('right')
        if (snake['coords'][0][0] - head[0] == -2) and (snake['coords'][0][1] == head[1]):
            if 'left' in canGo:
                canGo.remove('left')
        if (snake['coords'][0][1] - head[1] == 2) and (snake['coords'][0][0] == head[0]):
            if 'down' in canGo:
                canGo.remove('down')
        if (snake['coords'][0][1] - head[1] == -2) and (snake['coords'][0][0] == head[0]):
            if 'up' in canGo:
                canGo.remove('up')
        if ((snake['coords'][0][0] - head[0] == 1) and (snake['coords'][0][1] - head[1] == -1)):
            if 'right' in canGo:
                canGo.remove('right')
            if 'up' in canGo:
                canGo.remove('up')
        if ((snake['coords'][0][0] - head[0] == 1) and (snake['coords'][0][1] - head[1] == 1)):
            if 'right' in canGo:
                canGo.remove('right')
            if 'down' in canGo:
                canGo.remove('down')
        if ((snake['coords'][0][0] - head[0] == -1) and (snake['coords'][0][1] - head[1] == -1)):
            if 'left' in canGo:
                canGo.remove('left')
            if 'up' in canGo:
                canGo.remove('up')
        if ((snake['coords'][0][0] - head[0] == -1) and (snake['coords'][0][1] - head[1] == 1)):
            if 'left' in canGo:
                canGo.remove('left')
            if 'down' in canGo:
                canGo.remove('down')
    return canGo