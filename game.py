import random
javab= random.randint(1,99)

hads = input('what is your guess?')
hads = int(hads)

while hads != javab:
    if hads > javab:
        print('mine is smaller!')
    else :
        print('mine is larger')
    hads = input('what is your guess?')
    hads = int(hads)

print('woooow !!! you did it !! you rock')



