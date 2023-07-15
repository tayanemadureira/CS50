#print("#")
#print("#")
#print("#")

def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
     print("?" * width)

def print_square(size):
    # for each row in square
    for i in range(size):
        # fro each brick in row
            print("#" * size)

def print_row(width):
    print("!" * width)


main()