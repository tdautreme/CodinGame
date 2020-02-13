import sys
import math

def print_map(golf_map):
    for y in range(height):
        line = ""
        for x in range(width):
            line += golf_map[y][x]
        print(line)

width, height = [int(i) for i in input().split()]
golf_map = []
backup_map = []
for i in range(height):
    line = input()
    golf_map.append(list(line))
    backup_map.append(list(line))

ball_lst = []
for y in range(height):
    for x in range(width):
        if golf_map[y][x].isdigit():
            ball_lst.append({'spos': {'y': y, 'x': x}, 'epos': {'y': -1, 'x': -1}, 'shoot': int(golf_map[y][x])})
            
def erase(length, dirx, diry, pos):
    i = 0
    apos = dict(pos)
    while i < length:
        golf_map[apos['y']][apos['x']] = backup_map[apos['y']][apos['x']]
        i+=1
        apos['y'] += diry
        apos['x'] += dirx

def go_direction(axe, direction, char, pos, shoot, ball_i):
    if shoot == 0:
        return False
    dirx = direction if axe == 'x' else 0
    diry = direction if axe == 'y' else 0
    apos = dict(pos) # actual pos
    golf_map[apos['y']][apos['x']] = '.'
    i = 0
    while i < shoot and apos['y'] >= 0 and apos['x'] >= 0 and apos['y'] < height and apos['x'] < width and (golf_map[apos['y']][apos['x']] == '.' or golf_map[apos['y']][apos['x']] == 'X'):
        golf_map[apos['y']][apos['x']] = char
        i+=1
        apos['y'] += diry
        apos['x'] += dirx
    if i < shoot:
        return erase(i, dirx, diry, pos)
    elif not (apos['y'] >= 0 and apos['x'] >= 0 and apos['y'] < height and apos['x'] < width): # Can't shoot
        return erase(i, dirx, diry, pos)
    elif golf_map[apos['y']][apos['x']] == '.': # If need continue
        return True if find_target(apos, shoot - 1, ball_i) else erase(i, dirx, diry, pos)
    elif golf_map[apos['y']][apos['x']] == 'H': # If next ball
        golf_map[apos['y']][apos['x']] = 'P'
        return True if ball_i + 1 == len(ball_lst) or find_target(ball_lst[ball_i + 1]['spos'], ball_lst[ball_i + 1]['shoot'], ball_i + 1) else erase(i + 1, dirx, diry, pos)
    return erase(i, dirx, diry, pos)
    
def find_target(pos, shoot, ball_index):
    return go_direction('x', +1, '>', pos, shoot, ball_index) or go_direction('x', -1, '<', pos, shoot, ball_index) or go_direction('y', +1, 'v', pos, shoot, ball_index) or go_direction('y', -1, '^', pos, shoot, ball_index)

def encode_map():
    for y in range(height):
        for x in range(width):
            if golf_map[y][x] == 'X' or golf_map[y][x] == 'P':
                golf_map[y][x] = '.'
                
sys.setrecursionlimit(10000000)
find_target(ball_lst[0]['spos'], ball_lst[0]['shoot'], 0)
encode_map()
print_map(golf_map)