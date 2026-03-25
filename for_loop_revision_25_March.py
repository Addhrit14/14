a_range = input('enter an integer:')
a_range = int(a_range)
b_range = input('enter an integer:')
b_range = int(b_range)
c_range = input('enter an integer:')
c_range = int(c_range)
for a in range(1,a_range):
    for b in range(1,b_range):
        for c in range(1,c_range):
            a_squared = a*a
            b_squared = b*b
            c_squared = c*c
            if a_squared+b_squared == c_squared:
               print('you have entered a pythagorean triple',a,b,c)

