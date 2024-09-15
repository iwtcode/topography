lvl31 = [['а', 'б'], ['в', 'г']]
lvl3 = [['А', 'Б'], ['В', 'Г']]
lvl4 = [['I', 'II', 'III', 'IV', 'V', 'VI'],
        ['VII', 'VIII', 'IX', 'X', 'XI', 'XII'],
        ['XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII'],
        ['XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV'],
        ['XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX'],
        ['XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI']]
cnt = 1
lvl5 = []
for i in range(12):
    lvl5.append([])
    for j in range(12):
        lvl5[i].append(str(cnt))
        cnt += 1

def find_coords(coords):
    splited_coords = coords.split('-')
    filename = ''
    if(len(splited_coords) == 2): filename = 'map1.csv'
    elif(len(splited_coords) == 3 and any(splited_coords[-1] in sublist for sublist in lvl3)): filename = 'map2.csv'
    elif(len(splited_coords) == 3 and any(splited_coords[-1] in sublist for sublist in lvl4)): filename = 'map3.csv'
    elif(len(splited_coords) == 3 and any(splited_coords[-1] in sublist for sublist in lvl5)): filename = 'map4.csv'
    elif(len(splited_coords) == 4): filename = 'map5.csv'
    elif(len(splited_coords) == 5): filename = 'map6.csv'

    with open(filename, 'r', encoding='utf-8') as file:
        fullmap = [[x for x in line.split(';')] for line in file]
    
    neighbors = [[]]
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    for x, submap in enumerate(fullmap):
        for y, s in enumerate(submap):
            if coords in s:
                cnt = 0
                ln = len(coords)
                for new_x, new_y in moves:
                    new_x += x
                    new_y += y
                    if(new_x < 0): new_x = len(fullmap)-1
                    elif(new_x > len(fullmap)-1): new_x = 0
                    if(new_y < 0): new_y = len(fullmap[0])-1
                    elif(new_y > len(fullmap[0])-1): new_y = 0

                    neighbors[cnt].append(fullmap[new_x][new_y])
                    if(len(neighbors[cnt])%3 == 0):
                        neighbors.append([])
                        cnt += 1
                    ln = max(ln, len(fullmap[new_x][new_y]))
                return neighbors[:-1], ln

def write_out(arr, ln):
    for i, subarr in enumerate(arr):
        print(' '*(ln+2) + '|' + ' '*(ln+2) + '|' + ' '*(ln+2))
        for j, item in enumerate(subarr):
            item = item.replace('\n', '')
            print(' ' + item + ' '*(ln-len(item)), end='')
            if j < 2: print(' |', end='')
        print('\n' + ' '*(ln+2) + '|' + ' '*(ln+2) + '|' + ' '*(ln+2))
        if i < 2: print('—'*(ln+2) + '+' + '—'*(ln+2) + '+' + '—'*(ln+2))

inp = str(input('координаты\n> '))
res, ln = find_coords(inp)
write_out(res, ln)