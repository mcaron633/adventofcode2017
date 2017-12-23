def get_puzzle_input(text_file):

    data = []
    f = open(text_file)
    for line in f:
        data.append(line.rstrip())

    return data


def solve_captcha(line_input):

    # str_input = str(puzzle_input)
    input_sum = 0
    i = 0
    last = -1
    jump = len(line_input)/2

    for i in range(0, len(line_input)):

        i_next = i + jump

        if i_next > len(line_input) - 1:
            i_next = i_next - len(line_input)

        current = int(line_input[i])
        try :
            next_val = int(line_input[i_next])
        except Exception as e:
            print i
            print i_next
            print int(line_input[i])
            print int(line_input[i_next])

        # if i == 0:
        #    first = current

        if current == next_val:
            input_sum += current

        # if i == len(line_input)-1 and first == current:
        #    input_sum += current
        # last = current

    return input_sum

input_dat = get_puzzle_input('input.txt')

for line in input_dat:
    print solve_captcha(line)

