spam = ['apples', 'bananas', 'tofu', 'cats', 'bats', 'rats']

def print_item(list):
    for i in range(0, len(list)):
        if i != len(list) - 1:
            print(f'{list[i]}, ')
        if i == len(list) - 1:
            print('and ')
            print(list[i])

print_item(spam)