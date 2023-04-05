# Optional - allow the caller to select type of input user enters

# Try using break statements in while loop for try- catch


def input_number():

    num = input("Please enter an integer: ")

    while not num.isnumeric():
        num = input("Please enter an integer this time: ")

    if 0 <= int(num) < 101:
        return f"Your number of {num} is in the range 0 -> 100!"
    else:
        return num


print(input_number())
