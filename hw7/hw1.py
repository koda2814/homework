"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    # Open the files and create file handles
    file_handles = [open(file, 'r') for file in file_list]

    # Read the first line from each file
    current_values = [int(fh.readline().strip()) for fh in file_handles]

    while True:
        # Find the minimum value among the current values
        min_value = min(current_values)

        # Yield the minimum value
        yield min_value

        # Get the index of the file with the minimum value
        min_index = current_values.index(min_value)

        # Read the next line from the file with the minimum value
        next_value = file_handles[min_index].readline().strip()

        # If the next line is empty, break the loop
        if not next_value:
            break

        # Update the current value at the corresponding index
        current_values[min_index] = int(next_value)

    # Close the file handles
    for fh in file_handles:
        fh.close()