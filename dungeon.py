import random
import sys
import os
import logging
os.system("clear")
logging.basicConfig(filename='game.log', level=logging.DEBUG)

def grid(columns, rows):
    rows = range(rows)
    cols = range(columns)
    return [(y,x) for y in rows for x in cols]

GRIDS = [grid(3,3), grid(4,4), grid(5,5), grid(6,6), grid(7,7), grid(8,8), grid(9,9), grid(10,10)]

def get_locations(level):

    monster = random.choice(GRIDS[level-1])
    start = random.choice(GRIDS[level-1])
    door = random.choice(GRIDS[level-1])
    if monster == door or monster == start or door == start:
        return get_locations(level-1)

    return monster, door, start



def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x,y

def move_monster(monster, door, player):
    a, b = player
    c, d = door
    i, j = monster
    if a-c > i or c-a > i:
        i += 1
    elif b-d > j or d-b:
        j += 1

    return i, j

def max_x(grid):
    return max(grid)[0]

def max_y(grid):
    return max(grid)[1]

def get_moves(player, level):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == max_y(GRIDS[level-1]):
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == max_x(GRIDS[level-1]):
        moves.remove('DOWN')

    return moves

def draw_map(player, level):
    tile = '|{}'
    indices = [[0,1,
                3,4,
                6,7],
               [0,1,2,
                4,5,6,
                8,9,10,
                12,13,14],
               [0,1,2,3,
                5,6,7,8,
                10,11,12,13,
                15,16,17,18,
                20,21,22,23],
               [0,1,2,3,4,
                6,7,8,9,10,
                12,13,14,15,16,
                18,19,20,21,22,
                24,25,26,27,28,
                30,31,32,33,34],
               [0,1,2,3,4,5,
                7,8,9,10,11,12,
                14,15,16,17,18,19,
                21,22,23,24,25,26,
                28,29,30,31,32,33,
                35,36,37,38,39,40,
                42,43,44,45,46,47],
               [0,1,2,3,4,5,6,
                8,9,10,11,12,13,14,
                16,17,18,19,20,21,22,
                24,25,26,27,28,29,30,
                32,33,34,35,36,37,38,
                40,41,42,43,44,45,46,
                48,49,50,51,52,53,54,
                56,57,58,59,60,61,62],
               [0,1,2,3,4,5,6,7,
                9,10,11,12,13,14,15,16,
                18,19,20,21,22,23,24,25,
                27,28,29,30,31,32,33,34,
                36,37,38,39,40,41,42,43,
                45,46,47,48,49,50,51,52,
                54,55,56,57,58,59,60,61,
                63,64,65,66,67,68,69,70,
                72,73,74,75,76,77,78,79],
               [0,1,2,3,4,5,6,7,8,
                10,11,12,13,14,15,16,17,18,
                20,21,22,23,24,25,26,27,28,
                30,31,32,33,34,35,36,37,38,
                40,41,42,43,44,45,46,47,48,
                50,51,52,53,54,55,56,57,58,
                60,61,62,63,64,65,66,67,68,
                70,71,72,73,74,75,76,77,78,
                80,81,82,83,84,85,86,87,88,
                90,91,92,93,94,95,96,97,98]]
    for index, cell in enumerate(GRIDS[level-1]):
        if index in indices[level-1]:
            if cell == door:
                print(tile.format('D'), end='')
            # elif cell == monster:
            #     print(tile.format('M'), end='')
            elif cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == door:
                print(tile.format('D|'))
            elif cell == player:
                print(tile.format('X|'))
            # elif cell == monster:
            #     print(tile.format('M|'))
            else:
                print(tile.format('_|'))


print("Welcome to the dungeon!")
print("Enter quit to exit")
print("Enter left, right, up or down to move!")

level = 1
monster, door, player = get_locations(level)

while True:
    moves = get_moves(player, level)

    print("You are currently in room {}".format(player))
    # sys.stdout.write("\x1b[2J\x1b[H")
    draw_map(player, level)

    move = input("> ")
    move= move.upper()
    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
        monster = move_monster(monster, door, player)
    else:
        os.system("clear")
        print("** Walls are hard, stop running into them! **")
        monster = move_monster(monster, door, player)
        continue
    if player == door:
        os.system("clear")
        print("You escaped!!")
        level += 1
        try:
            monster, door, player = get_locations(level)
        except IndexError:
            if level == 9:
                print("\n" + "**********************")
                print("Holy shit you made it!")
                print("**********************" + "\n")
                break
            print("Entering level {}!".format(level))
        get_locations(level)
        continue

    elif player == monster:
        print("You were eating by the grue!")
        print("You dead now.")
        break
    os.system("clear")
