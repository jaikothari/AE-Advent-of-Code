'''
This is a solution attempt for week 14 advent of code problem.
The detailed problem can be found here - https://adventofcode.com/2023/day/14
'''

import argparse


# Process the file in the input format required
def process_file_as_argument():
    content = []
    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument('-f', '--file', help='Path to the input file', required=True)
    args = parser.parse_args()
    file_path = args.file
    with open(file_path, 'r') as file:
        content = file.read().strip().split("\n")
    file.close()
    return (content)


# Get load of individual columns
def get_load_of_each_column(rows, column, content):
    locate_hash = 0
    load = 0
    while locate_hash < rows:
        count = 0
        while locate_hash < rows and content[locate_hash][column] == "#":
            locate_hash += 1
        start = locate_hash
        while locate_hash < rows and content[locate_hash][column] != "#":
            if content[locate_hash][column] == "O":
                count += 1
            locate_hash += 1
        load += sum(rows - value for value in range(start, start + count))
    return (load)


# Part 1 processing function
def part1(content):
    rows, columns = len(content), len(content[0])
    return (sum(get_load_of_each_column(rows, column, content) for column in range(columns)))


# Main function definition
def main():
    content = process_file_as_argument()
    print("Part1 Answer: ", part1(content))


# Name main idiom
if __name__ == "__main__":
    main()
