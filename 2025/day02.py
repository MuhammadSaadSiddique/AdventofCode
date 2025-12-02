import re

def solve_gift_shop_puzzleP1(input_ranges_str: str) -> int:
    """
    Finds the sum of all "invalid IDs" within the given product ID ranges.

    An invalid ID is a number formed by repeating a sequence of digits (e.g., 6464, 123123).
    None of the numbers have leading zeroes.
    """

    # --- Step 1: Parse the Input Ranges ---
    ranges = []
    # Split the long string by commas, then split each part by the dash
    range_parts = input_ranges_str.split(',')
    
    # Determine the maximum value in the ranges to limit ID generation
    max_id = 0

    for part in range_parts:
        # The input is wrapped in the prompt, so remove potential newlines/spaces
        part = part.strip()
        if '-' in part:
            start_str, end_str = part.split('-')
            start = int(start_str)
            end = int(end_str)
            ranges.append((start, end))
            max_id = max(max_id, end)

    # --- Step 2: Generate All Possible Invalid IDs ---
    invalid_ids = set()
    
    # Invalid IDs have length 2k, where k is the length of the repeating part N.
    # The max ID is a 10-digit number (2121212124), so k can be 1, 2, 3, 4, or 5.
    
    # We iterate over k (length of the repeating segment N)
    for k in range(1, 6):
        # The repeating sequence N starts from 1 (to avoid leading zero)
        # 1-digit N starts at 1. 2-digit N starts at 10. k-digit N starts at 10^(k-1).
        start_n = 10**(k - 1)
        
        # Calculate the multiplier: 10^k + 1 (e.g., 101, 1001, 10001, etc.)
        multiplier = 10**k + 1
        
        # Determine the maximum N that results in an ID <= max_id
        # N * multiplier <= max_id
        # N <= max_id / multiplier
        
        # The maximum possible k-digit N is 10^k - 1 (e.g., 9, 99, 999)
        end_n = min(10**k - 1, max_id // multiplier)
        
        for n in range(start_n, end_n + 1):
            invalid_id = n * multiplier
            if invalid_id <= max_id:
                invalid_ids.add(invalid_id)
            else:
                # Since N is increasing, we can stop the loop early
                break
    
    # --- Step 3 & 4: Check IDs against Ranges and Sum them up ---
    total_sum = 0
    
    # Convert ranges to a sorted list for slightly faster searching (though set-based approach is simple)
    # Since the total number of IDs (approx 21k) and ranges (11) is small, simple iteration is fine.
    
    for invalid_id in sorted(list(invalid_ids)):
        is_in_range = False
        for start, end in ranges:
            if start <= invalid_id <= end:
                total_sum += invalid_id
                is_in_range = True
                # Once an ID is found in a range, we can stop checking other ranges for this ID
                break
                
    return total_sum

def solve_gift_shop_puzzleP2(input_ranges_str: str) -> int:
    """
    Finds the sum of all "invalid IDs" within the given product ID ranges.

    An invalid ID is a number formed by repeating a sequence of digits N, at least 
    twice (e.g., 6464, 123123, 11111).
    None of the numbers have leading zeroes.
    """

    # --- Step 1: Parse the Input Ranges ---
    ranges = []
    # Split the long string by commas, then split each part by the dash
    range_parts = input_ranges_str.split(',')
    
    # Determine the maximum value in the ranges to limit ID generation
    max_id = 0

    for part in range_parts:
        # The input is wrapped in the prompt, so remove potential newlines/spaces
        part = part.strip()
        if '-' in part:
            start_str, end_str = part.split('-')
            start = int(start_str)
            end = int(end_str)
            ranges.append((start, end))
            max_id = max(max_id, end)

    # --- Step 2: Generate All Possible Invalid IDs (New Logic) ---
    invalid_ids = set()
    
    # Determine the maximum length of an ID we need to check (up to 10 digits in this input)
    max_length = len(str(max_id))

    # k is the length of the repeating segment N (e.g., k=3 for '123'123'123)
    for k in range(1, max_length + 1):
        # m is the number of repetitions (m must be >= 2)
        for m in range(2, max_length + 1):
            L = k * m  # Total length of the generated ID
            
            if L > max_length:
                # If the total length exceeds the max ID length, we can stop for this k
                break
            
            # 1. Calculate the pattern factor: 1 + 10^k + 10^(2k) + ... + 10^((m-1)k)
            # This is equivalent to (10^L - 1) / (10^k - 1)
            # Example: k=2, m=3 (121212). L=6. Factor = (10^6 - 1) / (10^2 - 1) = 10101.
            pattern_factor = (10**L - 1) // (10**k - 1)
            
            # 2. Determine the range for the repeating segment N
            # N must not have a leading zero, so N starts at 10^(k-1)
            start_n = 10**(k - 1) 
            # N ends at the largest possible k-digit number
            end_n_max = 10**k - 1 
            
            # 3. Generate IDs and check against max_id
            for n in range(start_n, end_n_max + 1):
                invalid_id = n * pattern_factor
                
                if invalid_id > max_id:
                    # Since N is increasing, we can stop the loop for N
                    break
                    
                invalid_ids.add(invalid_id)

    # --- Step 3 & 4: Check IDs against Ranges and Sum them up ---
    total_sum = 0
    
    # Check every unique invalid ID against all the input ranges
    for invalid_id in sorted(list(invalid_ids)):
        for start, end in ranges:
            if start <= invalid_id <= end:
                total_sum += invalid_id
                # Once an ID is found in a range, we stop checking for this ID
                break
                
    return total_sum
# The provided example puzzle input (ranges separated by commas, wrapped for legibility)
puzzle_input = (
    "990244-1009337,5518069-5608946,34273134-34397466,3636295061-3636388848,8613701-8663602,573252-688417,472288-533253,960590-988421,7373678538-7373794411,178-266,63577667-63679502,70-132,487-1146,666631751-666711926,5896-10827,30288-52204,21847924-21889141,69684057-69706531,97142181-97271487,538561-555085,286637-467444,93452333-93519874,69247-119122,8955190262-8955353747,883317-948391,8282803943-8282844514,214125-236989,2518-4693,586540593-586645823,137643-211684,33-47,16210-28409,748488-837584,1381-2281,1-19"
)

# Calculate the result
resultp1 = solve_gift_shop_puzzleP1(puzzle_input)

print(f"The sum of all invalid product IDs in the given ranges is: {resultp1}")

resultp2=solve_gift_shop_puzzleP2(puzzle_input)
print(f"The sum of all invalid product IDs in the given ranges is: {resultp2}")
