import string
import random

class Password:
    def __init__(self):
        self.pw = None
        self.strength = None
        self.allowed = [string.ascii_letters, string.digits, '!$%^&*()_-=+']

    def createPassword(self):

        badPassword = True
        while badPassword:

            length = random.randint(8, 12)
            pw = ''

            for _ in range(length):
                pw += random.choice(''.join(self.allowed))
            
            self.pw = pw
            self.checkPassword()

            if self.strength > 20:
                badPassword = False


    def inputPassword(self):
        badInput = True
        while badInput:
            pw = input('Enter a password:\n')
            if 8 <= len(pw) <= 24:
                badInput = any(list(map(lambda x: x not in ''.join(self.allowed), list(pw))))
        self.pw = pw
    
    def checkPassword(self):
        self.strength = len(self.pw)

        checks = []

        checks.append(any([True for char in self.pw if char in string.ascii_uppercase]))
        checks.append(any([True for char in self.pw if char in string.ascii_lowercase]))
        checks.append(any([True for char in self.pw if char in string.digits]))
        checks.append(any([True for char in self.pw if char in self.allowed[2]]))
        self.strength += sum([5 for boolean in checks if boolean])
        self.strength += 10 if all(checks) else 0

        checks = []
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

        checks.append(all([True if char in string.ascii_uppercase or char in string.ascii_lowercase else False for char in self.pw]))
        checks.append(all([True if char in string.digits else False for char in self.pw]))
        checks.append(all([True if char in self.allowed[2] else False for char in self.pw]))
        self.strength -= sum([5 for boolean in checks if boolean])

        count = 0
        for index in range(len(self.pw) - 3):
            compare = self.pw[index:index+3].lower()
            for row in keyboard:
                if compare in row:
                    count += 1
        self.strength -= count * 5
    
    def show(self):
        print('Password:', self.pw)
        print('Strength:', self.strength)

def menu(options: list) -> None:

    formatLine = lambda num, option: f' {num}.   {option}'
    print('Which option would you like to choose?')

    for num, option in enumerate(options, start=1):
        print(formatLine(num, option))

def validate(options: list) -> int:
    badInput = True
    while badInput:
        userInput = input(f'Please enter a number between 1 and {len(options)}:\n')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput in range(1, len(options) + 1):
                return userInput
            print(f'{userInput} is not in the required range')
        else:
            print('That is not a number')

def execute(password: object, option: int) -> None:
    if option == 1:
        password.inputPassword()
        password.checkPassword()
    if option == 2:
        password.createPassword()
    if option == 3:
        print('****Thanks for using PASSWORD****')
        quit()
    else:
        password.show()

def main():

    password = Password()

    options = ['Check Password', 'Gernerate Password', 'Quit']

    running = True
    while running:

        menu(options)

        option = validate(options)

        execute(password, option)

if __name__ == '__main__':
    main()