def non_empty_input(prompt):
    while True:
        input_ = input(prompt).strip()
        if input_ == "":
            print("Input cannot be empty.")
        else:
            return input_

def int_input(prompt):
    while True:
        try:
            input_ = int(input(prompt))
            if input_ <= 0:
                print('Please enter a number greater than zero')
                continue
            return input_
        except ValueError:
            print('Enter a valid number')
def float_input(prompt):
    while True:
        try:
            input_ = float(input(prompt))
            if input_ <= 0:
                print('Please enter a cost greater than zero')
                continue
            return input_
        except ValueError:
            print('Enter a valid cost amount')
