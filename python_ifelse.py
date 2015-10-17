name = 'Dora'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
elif name == "Dora":
	print("Heeeeeey Dora")
else:
    print('Hey anonymous!')


if 3>4:
	print('It works!')
else:
	print("It doesn't work")


def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("dora")