def print_move(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to) #base case
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
