#!/usr/bin/env python3

import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Loop over each line from stdin
for line in sys.stdin:
    # Parse line according to input format
    try:
        ip, _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        # Skip line if format is incorrect
        continue

    # Update variables
    total_size += file_size
    status_codes[status_code] += 1
    line_count += 1

    # Print statistics every 10 lines or on keyboard interruption
    if line_count % 10 == 0:
        print(f"File size: {total_size}")
        for code in sorted(status_codes):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")
        print()

# Print final statistics
print(f"File size: {total_size}")
for code in sorted(status_codes):
    if status_codes[code] > 0:
        print(f"{code}: {status_codes[code]}")
