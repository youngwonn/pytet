from matrix import *
import random

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

def delete_lines(s,b,top,dy,dx,dw):
    global score
    if b == None :
        return s
    nDeleted = 0
    nScanned = b.get_dy()
    if top + b.get_dy() -1 >= dy :
        nScanned -= (top+b.get_dy()-dy)
    zero = Matrix(1,dx-2*dw)
    for y in range(nScanned-1,-1,-1):
    #for(y=nScanned-1;y>=0;y--):
        cy = top+y+nDeleted
        line = s.clip(cy,0,cy+1,s.get_dx())
        if line.sum() == s.get_dx() :
            score += 1000
            temp = s.clip(0,0,cy,s.get_dx())
            s.paste(temp,1,0)
            s.paste(zero,0,dw)
            nDeleted = nDeleted +1
    return s


arrayBlk = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]

I = [ [ [ 0 , 0 , 1 ,0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
L = [ [ [ 1 , 0 , 0 , 0 ] , [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 1 , 1 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
H = [ [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ], 
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
T = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
a = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], 
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
b = [ [ [ 0 , 0 , 0 , 1 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 1 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 0 ] ] ]
c = [ [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], 
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2
h = random.randint(0,6)
i=0
arrayBlk=[I,L,H,T,a,b,c]

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk[h][i])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        i=(i+1)%4
        currBlk=Matrix(arrayBlk[h][i])
    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top+=1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            if tempBlk.anyGreaterThan(1):
                top-=1
                newBlockNeeded = True

    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            i = (i-1)%4
            currBlk = Matrix(arrayBlk[h][i])
        elif key == ' ': # undo: move up
            print('Not implemented')

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        oScreen = delete_lines(oScreen, currBlk, top, iScreenDy, iScreenDx, iScreenDw)
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        h = random.randint(0,6)
        i=0
        currBlk = Matrix(arrayBlk[h][i])
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
