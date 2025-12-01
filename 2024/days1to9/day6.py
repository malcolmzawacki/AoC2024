# # # timing # # #
import datetime
start = datetime.datetime.now()

def parse_grid(text_lines):
    """Parse the grid to find guard position, direction and obstacles."""
    obstacles = set()  # Using set for O(1) lookup
    guard_pos = None
    guard_dir = None
    
    for i, row in enumerate(text_lines):
        for j, char in enumerate(row):
            if char == '#':
                obstacles.add((i, j))
            elif char in '^v<>':
                guard_pos = (i, j)
                guard_dir = get_direction(char)
    
    return guard_pos, guard_dir, obstacles

def get_direction(char):
    """Convert character to direction vector."""
    directions = {
        '^': (-1, 0),  # up
        'v': (1, 0),   # down
        '<': (0, -1),  # left
        '>': (0, 1)    # right
    }
    return directions.get(char)

def rotate_right(direction):
    """Rotate direction vector 90 degrees clockwise."""
    row, col = direction
    return (col, -row)

def find_exit_with_path(text_lines):
    """Return exit point, path length, and full path with directions."""
    grid_rows = len(text_lines)
    grid_cols = len(text_lines[0])
    pos, direction, obstacles = parse_grid(text_lines)
    visited = {pos}
    path = [(pos, direction)]  
    
    while True:
        new_row = pos[0] + direction[0]
        new_col = pos[1] + direction[1]
        new_pos = (new_row, new_col)

        if not (0 <= new_row < grid_rows and 0 <= new_col < grid_cols):
            "if new position is out of bounds, guard has left"
            return pos, len(visited), visited, path, obstacles
        
        if new_pos in obstacles:
            direction = rotate_right(direction)
            path.append((pos, direction))
        else:
            pos = new_pos
            visited.add(pos)
            path.append((pos, direction))

def find_loop_positions(text_lines, original_path, original_obstacles):
    obstacle_points = []
    for i in range(0,len(original_path)):
        position, _ = original_path[i]
        if position not in obstacle_points:
            obstacle_points.append(position)
    grid_rows = len(text_lines)
    grid_cols = len(text_lines[0])
    loop_count = 0
    noloop = 0
    current_pos, current_dir = original_path[0]
    for i in range(len(obstacle_points)):
        
        next_pos = obstacle_points[i]
        #print(f"testing {i} of {len(obstacle_points)} obstacle positions")
        test_obstacles = original_obstacles | {next_pos}
        loop_truth = detect_loop_from_path(current_pos, current_dir, test_obstacles, grid_rows, grid_cols)
        if loop_truth:
            loop_count += 1
        else:
            noloop += 1
    return loop_count, noloop

def detect_loop_from_path(pos, direction, test_obstacles, grid_rows, grid_cols):
    
    seen_states = set()
    current_pos = pos
    current_dir = direction
    first_repeat_state = False
    steps = 0
    loop_trigger1 = 0
    loop_trigger2 = 0
    loop_set1 = set()
    loop_set2 = set()
    while steps < 1000000:
        new_row = current_pos[0] + current_dir[0]
        new_col = current_pos[1] + current_dir[1]
        new_pos = (new_row, new_col)
        
        if not (0 <= new_row < grid_rows and 0 <= new_col < grid_cols):
            "if outside grid, no loop obviously (exited)"
            return False
        elif new_pos in test_obstacles:
            "turn right at obstacles, just like in part 1"
            current_dir = rotate_right(current_dir)
        else:
            "can move here"
            current_pos = new_pos

        "whatever happened above, new state now formatted properly"
        state = (current_pos, current_dir)

        "BEFORE adding state to seen states, check if it is already in there"  
        if state in seen_states and first_repeat_state is False:
            "if it IS, that means since this test path started, this exact state has been visited before"
            "however this is not enough on its own to constitute a loop"
            first_repeat_state = True
            loop_trigger1 = steps+100 # wait for loop to 'settle in'
            loop_trigger2 = loop_trigger1 + 1 # skip over state stored in loop_set1 
        if steps >= loop_trigger1 and first_repeat_state is True:
            loop_set1.add(state)
        if steps >= loop_trigger2 and first_repeat_state is True:
            loop_set2.add(state)
        if loop_set1 - loop_set2 == set() and first_repeat_state is True:

            return True
        "log the state (reset for each test obstacle) AFTER checking for inclusion in seen_states"
        seen_states.add(state)
        steps += 1
            
    print("  Hit step limit!")
    return False

# Main execution:
with open("text/day6.txt") as f:
    text_lines = f.read().splitlines()

exit_pos, path_length, visited, original_path, obstacles = find_exit_with_path(text_lines)
print(f"Guard exits at position: {exit_pos}")
print(f"Path length: {path_length}")
print(f"Number of steps: {len(original_path)}")

loop_positions, noloop = find_loop_positions(text_lines, original_path, obstacles)
print(f"Number of possible loop-creating positions: {loop_positions}, and {noloop} that will not")
print("Time: "+ str(datetime.datetime.now() - start))