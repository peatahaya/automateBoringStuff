# looped program that checks name and password
# and displays appropriate message

while True:
    print('Who are you?')
    name = input()
    if name != 'pit':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')    