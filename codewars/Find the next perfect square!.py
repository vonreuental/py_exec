def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sq_num = int(sq ** 0.5)
    if  sq_num ** 2 == sq:
        return (sq_num + 1) **2
    return -1


print(find_next_square(155))