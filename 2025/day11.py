import sys

def solve_reactor_paths(puzzle_input):
    # 1. Parse the Input into a Graph (Adjacency List)
    graph = {}
    lines = [line.strip() for line in puzzle_input.split('\n') if line.strip()]
    
    for line in lines:
        # Line format: "name: dest1 dest2 dest3"
        parts = line.split(':')
        source = parts[0].strip()
        # Some nodes might point to nothing, or empty string if split fails, handle gracefully
        if len(parts) > 1:
            destinations = parts[1].strip().split()
            graph[source] = destinations
        else:
            graph[source] = []

    # 2. Define DFS function with Memoization
    memo = {}

    def count_paths_from(node):
        # Base Case: Reached the target
        if node == 'out':
            return 1
        
        # Base Case: Dead end (no outgoing connections defined)
        if node not in graph:
            return 0
        
        # Check Cache
        if node in memo:
            return memo[node]
        
        # Recursive Step: Sum paths from all neighbors
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths_from(neighbor)
        
        # Store result in cache
        memo[node] = total_paths
        return total_paths

    # 3. Execute
    start_node = 'you'
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in input.")
        return 0

    total = count_paths_from(start_node)
    return total
def solve_reactor_pathsP2(puzzle_input):
    # 1. Parse the Input into a Graph (Adjacency List)
    graph = {}
    lines = [line.strip() for line in puzzle_input.split('\n') if line.strip()]
    
    for line in lines:
        # Line format: "name: dest1 dest2 dest3"
        parts = line.split(':')
        source = parts[0].strip()
        # Some nodes might point to nothing, or empty string if split fails, handle gracefully
        if len(parts) > 1:
            destinations = parts[1].strip().split()
            graph[source] = destinations
        else:
            graph[source] = []

    # 2. Define DFS function with Memoization (including state)
    # Memo key: (node_name, visited_dac, visited_fft)
    memo = {}

    def count_paths_from(node, visited_dac, visited_fft):
        # Update flags if current node is one of the required ones
        if node == 'dac':
            visited_dac = True
        if node == 'fft':
            visited_fft = True

        # Base Case: Reached the target
        if node == 'out':
            # Only count this path if we have visited both required nodes
            return 1 if visited_dac and visited_fft else 0
        
        # Base Case: Dead end (no outgoing connections defined)
        if node not in graph:
            return 0
        
        # Check Cache
        state_key = (node, visited_dac, visited_fft)
        if state_key in memo:
            return memo[state_key]
        
        # Recursive Step: Sum paths from all neighbors passing down the current state
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths_from(neighbor, visited_dac, visited_fft)
        
        # Store result in cache
        memo[state_key] = total_paths
        return total_paths

    # 3. Execute
    start_node = 'svr'
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in input.")
        return 0

    # Start with False for both flags (unless start_node itself is dac or fft, handled inside func)
    total = count_paths_from(start_node, False, False)
    return total

# --- Input Area ---
puzzle_input = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

if __name__ == "__main__":
    result = solve_reactor_paths(puzzle_input)
    print(f"Total paths from 'you' to 'out': {result}")
    resultp2 = solve_reactor_pathsP2(puzzle_input)
    print(f"Total paths from 'svr' to 'out' visiting both 'dac' and 'fft': {resultp2}")
