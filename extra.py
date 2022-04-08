'''This is the CLI-based password generator in the world'''
import string
import random
import datetime
dat = datetime.datetime.now()
print('HELLO SIR\n WELCOME TO THE BEST PASSWORD GENERATOR IN THE WORLD!\nIT WILL CREATE THE MIXTURE OF LETTERS AND WORDS')
N = int(input('What should be your password length: '))
purpose = input('Enter the company,website name for you are making the password for : ')
id = input('Enter the email, id for which you are making your password: ')
pasw = ''.join(random.choices(string.ascii_uppercase +string.digits+string.ascii_lowercase, k = N))
print(f'YOUR PASSWORD IS : {pasw}')
with open('password.txt', 'a') as pw:
    pw.write(f"\nThe company name is {purpose}, id is {id}, Password is '{pasw}'\nAnd the time is {dat}")
    print('Yeah! Your password is made!')
    print('Thanks for using this password generator')