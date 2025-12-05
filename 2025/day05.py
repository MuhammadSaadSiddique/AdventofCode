divTableContainer

import os

def solve_inventory_puzzle():
    file_path = "inputd5.txt"
    # Example input data to use if file is not found
    example_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    raw_data = example_input
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            raw_data = f.read()
    else:
        print(f"File '{file_path}' not found. Using example data:\n")
        raw_data = example_input

    # Split the input into two parts: ranges and available IDs
    # They are separated by a blank line (double newline)
    parts = raw_data.strip().split('\n\n')
    
    if len(parts) < 2:
        print("Error: Input format incorrect. Expected two sections separated by a blank line.")
        return

    range_lines = parts[0].strip().split('\n')
    id_lines = parts[1].strip().split('\n')

    # Parse the valid ranges
    valid_ranges = []
    for line in range_lines:
        try:
            start, end = map(int, line.split('-'))
            valid_ranges.append((start, end))
        except ValueError:
            print(f"Skipping invalid range line: {line}")

    # Part 1 Logic: Count available IDs that are fresh
    fresh_count_p1 = 0
    print(f"Processing {len(id_lines)} IDs against {len(valid_ranges)} ranges...")

    for line in id_lines:
        try:
            ingredient_id = int(line)
            is_fresh = False
            # Check if ID falls into ANY valid range
            for start, end in valid_ranges:
                if start <= ingredient_id <= end:
                    is_fresh = True
                    break 
            if is_fresh:
                fresh_count_p1 += 1
        except ValueError:
            # print(f"Skipping invalid ID line: {line}")
            pass

    # Part 2 Logic: Count total unique fresh IDs in all ranges
    # Sort ranges by start value to enable merging
    valid_ranges.sort(key=lambda x: x[0])
    
    merged_ranges = []
    if valid_ranges:
        curr_start, curr_end = valid_ranges[0]
        
        for i in range(1, len(valid_ranges)):
            next_start, next_end = valid_ranges[i]
            
            # If the next range starts inside or immediately after the current range, merge them.
            # (e.g., 3-5 and 4-8 overlap; 3-5 and 6-8 are adjacent/contiguous integers)
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                merged_ranges.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        
        merged_ranges.append((curr_start, curr_end))
        
    total_fresh_ids_p2 = sum(end - start + 1 for start, end in merged_ranges)

    print("-" * 30)
    print(f"Part 1 - Total Fresh Ingredients (Specific IDs): {fresh_count_p1}")
    print(f"Part 2 - Total Fresh ID Space (Merged Ranges): {total_fresh_ids_p2}")
    print("-" * 30)

if __name__ == "__main__":
    # Ensure you create a file named 'input.txt' with your full puzzle input
    solve_inventory_puzzle()
