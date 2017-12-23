def get_puzzle_input(text_file):

    data = []
    f = open(text_file)
    for line in f:
        data.append((line.rstrip()).split('\t'))

    return data

def main(data):
    line_sum = 0

    for line in data:
        line_sum += line_max(line) - line_min(line)

    return line_sum

def line_max(line):

    max_val = 0

    for item in line:
        if int(item) > max_val:
            max_val = int(item)

    return max_val

def line_min(line):

    min_val = 999999999999

    for item in line:
        if int(item) < min_val:
            min_val = int(item)

    return min_val



print main(get_puzzle_input('input.txt'))