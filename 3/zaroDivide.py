def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(0))