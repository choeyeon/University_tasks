import numpy as np
import matplotlib.pyplot as plt

# open and read file
with open('input.dat', 'r') as file:
    str = file.readline()
    I4959 = float(str[8:13])
    print('I4959 = ', I4959)
    str = file.readline()
    I5007 = float(str[8:13])
    print('I5007 = ', I5007)
    str = file.readline()
    I4363 = float(str[8:13])
    print('I4363 = ', I4363)
    str = file.readline()
    I4068 = float(str[8:13])
    print('I4068 = ', I4068)
    str = file.readline()
    I4076 = float(str[8:13])
    print('I4076 = ', I4076)
    str = file.readline()
    I6717 = float(str[8:13])
    print('I6717 = ', I6717)
    str = file.readline()
    I6731 = float(str[8:13])
    print('I5007 = ', I6731)

ne1 : float
ne2 : float

# equation
I1 = (I4959 + I5007) / I4363
I2 = (I4068 + I4076)/(I6717+I6731)
def ne1(Te):
    return (7.9 * np.exp(3.29 * ((10**4)/Te)) - I1) / (I1 * 4.5 * (10**-4)/(Te**(1/2)))
def ne2(Te):
    return (I2 - (0.164 * np.exp(-13800/Te) * 3.8))/(0.164 * np.exp(-13800/Te) * 10**(-2) * Te * (1 + 1.32 * np.exp(-13800/Te)))

# Creating an array of Te values ​​from 4000 to 30000 in increments of 10
Te = np.arange(4000, 30000, 10)

# Setting limits for ne
plt.xlim(4000, 30000)
plt.ylim(-10, 100)
# Construction of graphs of functions f1 and f2
plt.plot(Te, ne1(Te), label='ne(Te) - [OIII]')
plt.plot(Te, ne2(Te), label='ne(Te) - [SII]')

# Adding legends and captions to graphs
plt.legend()
plt.xlabel('Te')
plt.ylabel('ne')
plt.title('Залежність ne від Te для [OIII] та [SII]')


# Graph output
plt.show()