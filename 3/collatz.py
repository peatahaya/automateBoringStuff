def collatz(num):
    if num % 2 == 0:
        global new_num 
        new_num = int(num / 2)
        if new_num != 1:
            print(new_num)
            collatz(new_num)
        elif new_num == 1:
            print(new_num)
            
    elif num % 2 == 1:
        new_num = 3 * num + 1
        print(new_num)
        collatz(new_num)

while True:
    num = int(input('Enter number: '))
    collatz(num)
    if new_num == 1:
        break

