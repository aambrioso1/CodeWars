def possible_positions(pos):
    # A very straightforward solution.
    # I use two dictionaries to convert moves from chess notation
    # to numerical coordinates.  Then I add  +- 1 
    # and +- 2 to them.  Then remove mmoves are not on the board.
    # Then finally the moves are changed back to chess notation
    let = dict(zip(range(8),'abcdefgh'))
    num = dict(zip('abcdefgh', range(8)))
    x,y = num[pos[0]], int(pos[1])-1
    lst = []
    if x - 2 in range(8) and y - 1 in range(8):
        lst.append([x-2, y-1])
    if x - 2 in range(8) and y + 1 in range(8):
        lst.append([x-2, y+1])
    if x - 1 in range(8) and y - 2 in range(8):
        lst.append([x-1, y-2])
    if x - 1 in range(8) and y + 2 in range(8):
        lst.append([x-1, y+2])
    if x + 1 in range(8) and y - 2 in range(8):
        lst.append([x+1, y-2])
    if x + 1 in range(8) and y + 2 in range(8):
        lst.append([x+1, y+2])
    if x + 2 in range(8) and y - 1 in range(8):
        lst.append([x+2, y-1])
    if x + 2 in range(8) and y + 1 in range(8):
        lst.append([x+2, y+1])
    move_list = [str(let[i[0]])+str(i[1]+1) for i in lst]
    return move_list
    