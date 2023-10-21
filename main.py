x = str(input('Enter ur number: '))
length = len(x)
a = True
for i in range(len(x) // 2):

    if x[i] != x[length-(i+1)]:
        a = False
        break
if a != False:
    print('Your number is a Polyndrome')
else:
    print('Your number is not a Polyndrome')


