def get_location_info(target_loc):
    # define layer size from rank
    # define layer side from rank
    # define first position in layer from center
    # use center as 0,0
    # define info block per location rank
    # position base is 1

    current_loc = 1
    positionInfo = []
    x = 0
    y = 0
    quadrant = []

    while 1:

        [l_size, l_side, l_s_pos] = get_layer_info(current_loc)

        # find all values that are defined and that touch the current value,
        # using x and y coordinates

        val = get_val(positionInfo, x, y)

        positionInfo.append([current_loc, l_size, l_side, quadrant, l_s_pos, x, y, val])

        if current_loc >= target_loc:
            break

        # set x,y val to next val
        [x, y, quadrant] = next_move(l_s_pos, l_size, l_side, current_loc, x, y)
        out = val_case_def(quadrant, l_side, current_loc)

        current_loc += 1

    return positionInfo


def calculate_layer_base(location):
    import numpy as np

    first_pos = (location == 1)
    base = np.sqrt(location)

    even_base = (np.floor(base) % 2 == 0)
    first_position_in_layer = ((base % 1 != 0) and not even_base and not first_pos)

    last_pos_in_layer = (base % 1 == 0) and not first_pos and not even_base

    if first_position_in_layer:

        base = np.floor(np.sqrt(location)) + 2

    elif first_pos:
        base = 1

    elif even_base:
        base = np.floor(base) + 1

    elif last_pos_in_layer:
        print("last")

    else:
        print(base)
        base = None

    return base


def get_layer_info(location):
    side = calculate_layer_base(location)
    layer_rank = ((side - 1) / 2) + 1

    if location != 1:
        # size
        layer_size = 8 * (layer_rank - 1)

        # layer start position
        l_s_pos = side ** 2 + 1 - layer_size

    elif location == 1:
        layer_size = 1
        l_s_pos = 1

    out = [layer_size, side, l_s_pos]

    return out


def get_val(positionInfo, x, y):
    val = -999

    return val


def val_case_def(q, side, location):

    if side !=1:

        q_no = q[0]
        q_pos = q[1]
        valid_coord = []

        # sides
        if q_pos < side and q_pos != 1:
            print("side---")
            if q_no == 1:
                valid_coord = [[0, -1], [-1, -1], [-1, 0], [-1, 1]]
            elif q_no == 2:
                valid_coord = [[-1, -1], [0, -1], [-1, 1], [1, 0]]
            elif q_no == 3:
                valid_coord = [[0, 1], [1, 1], [1, 0], [1, -1]]
            elif q_no == 4:
                valid_coord = [[-1, 0], [-1, 1], [0, 1], [1, 1]]

        if q_pos == 1:
            print("corner---")


            if q_no == 1:
                valid_coord = [[-1, 0], [-1, 1]]
            elif q_no == 2:
                valid_coord = [[0, -1], [-1, -1]]
            elif q_no == 3:
                valid_coord = [[1, -1], [-1, 0]]
            elif q_no == 4:
                valid_coord = [[0, 1], [1, 1]]

        if q_pos == side:
            print("asdasdeeee")

        print(location)
        print(q_no)
        print(q_pos)
        print(valid_coord)

    else:
        valid_coord = []

    return valid_coord


def main():
    print("processing data ---------------------------------------------")

    array = get_location_info(51)

    print("done /r/r---------------------------------------------/r")
    for line in array:
        print(line)

    return


def next_move(l_s_pos, l_size, l_side, location, x, y):

    # next_mov = [x_shift, y_shift]
    next_mov = [-100, -100]

    if l_size == 1:
        next_mov = [1, 0]
        print("initial position")
        n_q = []

    else:

        l_pos = location - l_s_pos + 2
        quadrant = (l_pos // (l_side - 1)) + 1
        pos_in_quadrant = l_pos % (l_side - 1)
        n_q = [quadrant, pos_in_quadrant]

        if quadrant == 1 and pos_in_quadrant <= l_side:
            next_mov = [0, 1]

        elif quadrant == 2 and pos_in_quadrant <= l_side:
            next_mov = [-1, 0]

        elif quadrant == 3 and pos_in_quadrant <= l_side:
            next_mov = [0, -1]

        elif quadrant == 4 and pos_in_quadrant <= l_side:
            next_mov = [1, 0]

        elif quadrant == 5: # special case of last position in layer
            next_mov = [1, 0]

        else:
            print("---------------------------not passed")
            next_mov = None



    n_x = next_mov[0] + x
    n_y = next_mov[1] + y
    n_xy = [n_x, n_y, n_q]

    print("--")
    return n_xy

main()
