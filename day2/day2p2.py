def get_puzzle_input(text_file):

    data = []
    f = open(text_file)
    for line in f:
        data.append((line.rstrip()).split('\t'))

    return data


def main(data):

    line_sum = 0

    for line in data:

        line_sum += divide_line_items(line)

    return line_sum


def divide_line_items(line):

    div_sum = 0
    done = False

    for item in line:

        for i in range(0, len(line)):

            item1 = int(item)
            item2 = int(line[i])

            div1 = item1/item2
            div2 = item2/item1

            if isinstance(div1, (int, long)) and div1 != 1:
                div_sum += div1
                done = True
                break

            elif isinstance(div2, (int, long)) and div2 != 1:
                div_sum += div2
                done = True
                break

        if done == True:
            break

    return div_sum

print main(get_puzzle_input('input.txt'))