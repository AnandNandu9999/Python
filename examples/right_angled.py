def print_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)


def opposite_right_angle_traingel(n):
    while n > 0:
        print("* " * n)
        n -= 1
        
        


print_pattern(5)
opposite_right_angle_traingel(5)