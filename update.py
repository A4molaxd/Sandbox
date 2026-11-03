import copy

def update(pixels):
    
    rows = len(pixels)
    cols = len(pixels[0])

    newPixels = copy.deepcopy(pixels)

    for i in range(rows):
        for j in range(cols):
            if pixels[i][j].state == 'air': # ------------- AIR -------------- #
                newPixels[i][j].color = 'black'
            elif pixels[i][j].state == 'sand': # ------------- SAND -------------- #
                newPixels[i][j].color = 'yellow'
                if j == rows - 1:
                    continue
                elif pixels[i][j + 1].state == 'air' or pixels[i][j + 1].state == 'water':
                    newPixels[i][j].state = pixels[i][j + 1].state
                    newPixels[i][j + 1].state = 'sand'
                elif pixels[i][j + 1].state == 'sand' or pixels[i][j + 1].state == 'brick':
                    if i != cols - 1:
                        if (pixels[i + 1][j].state == 'air' and pixels[i + 1][j + 1].state == 'air') or (pixels[i + 1][j].state == 'water' and pixels[i + 1][j + 1].state == 'water'):
                            newPixels[i][j].state = pixels[i + 1][j + 1].state 
                            newPixels[i + 1][j + 1].state = 'sand'
                        elif i != 0:
                            if (pixels[i - 1][j].state == 'air' and pixels[i - 1][j + 1].state == 'air') or (pixels[i - 1][j].state == 'water' and pixels[i - 1][j + 1].state == 'water'):
                                newPixels[i][j].state = pixels[i - 1][j + 1].state
                                newPixels[i - 1][j + 1].state = 'sand'
                    
            elif pixels[i][j].state == 'brick': # ------------- BRICK -------------- #
                newPixels[i][j].color = 'red'

            elif pixels[i][j].state == 'water': # ------------- WATER -------------- #
                newPixels[i][j].color = 'blue'
                if j != rows - 1:
                    if pixels[i][j + 1].state == 'air':
                        newPixels[i][j].state = 'air'
                        newPixels[i][j + 1].state = 'water'
                    else:
                        if i != 0:
                            if i != cols - 1:
                                if pixels[i + 1][j] == 'air':
                                    newPixels[i][j] = 'air'
                                    newPixels[i + 1][j] = 'water'
                            elif i == cols - 1 or pixels[i + 1][j] != 'air':
                                if pixels[i - 1][j] == 'air':
                                    newPixels[i][j] = 'air'
                                    newPixels[i - 1][j] = 'water'
                        else:
                            if pixels[i + 1][j] == 'air':
                                newPixels[i][j] = 'air'
                                newPixels[i + 1][j] = 'water'
                else:
                    if i != 0:
                        if i != cols - 1:
                            if pixels[i + 1][j] == 'air':
                                newPixels[i][j] = 'air'
                                newPixels[i + 1][j] = 'water'
                        elif i == cols - 1 or pixels[i + 1][j] != 'air':
                            if pixels[i - 1][j] == 'air':
                                newPixels[i][j] = 'air'
                                newPixels[i - 1][j] = 'water'
                    else:
                        if pixels[i + 1][j] == 'air':
                            newPixels[i][j] = 'air'
                            newPixels[i + 1][j] = 'water'            


    return newPixels

