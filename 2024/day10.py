import datetime
start = datetime.datetime.now()

def construct_trail_map(text):
    trail_map = {}
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] not in trail_map.keys():
                trail_map[text[i][j]] = {(i,j)}
            else:
                trail_map[text[i][j]].add((i,j))
    return trail_map

def trailheads(trail_map):
    trailhead_score = 0
    base = trail_map['0']
    #print(f"Initial positions: {base}")
    for tuple in base:
        move_set = next_moves(tuple,trail_map,'1')
        #print(f"First steps: {move_set}")
        i = 2
        while i <= 9:
            next_move_set = set()
            #print(f"Starting move {i}")
            for tuple in move_set:
                next_move_set = next_move_set.union(next_moves(tuple,trail_map,str(i)))
                #print(f"After union {next_move_set}")
            move_set = next_move_set
            #print(move_set)
            i+=1
        trailhead_score+=len(move_set)
    return trailhead_score

def next_moves(tuple,trail_map,height):
    up = (tuple[0] - 1, tuple[1])
    down = (tuple[0]+1, tuple[1])
    left = (tuple[0],tuple[1]-1)
    right = (tuple[0],tuple[1]+1)
    move_set = {up,down,left,right}
    #print(f"Possible moves: {move_set}")
    move_set&=trail_map[height]
    #print(f"Returning to main loop: {move_set}")
    return move_set

def count_paths(current_pos, current_height, trail_map):
    """Recursively count paths from current position to height 9."""
    if current_height == 8:
        # Base case: return number of valid moves to height 9
        return len(next_moves(current_pos, trail_map,'9'))
        
    # Find valid moves to next height
    next_height = current_height + 1
    valid_moves = next_moves(current_pos, trail_map,str(next_height))
    
    # Recursively count paths from each valid move
    path_count = 0
    for next_pos in valid_moves:
        path_count += count_paths(next_pos, next_height, trail_map)
    
    return path_count

def count_paths_total(trail_map):
    """Count total valid paths starting from height 0."""
    total_paths = 0
    for start_pos in trail_map['0']:  # For each height 0 position
        total_paths += count_paths(start_pos, 0, trail_map)
    return total_paths

def onOpen():
    with open("text/day10.txt") as f:
        text = f.read().splitlines()
        trail_map = construct_trail_map(text)
        print(trailheads(trail_map))
        print(count_paths_total(trail_map))
    return

onOpen()

print("Time: "+ str(datetime.datetime.now() - start))