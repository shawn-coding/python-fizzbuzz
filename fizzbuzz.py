"""
FizzBuzz
A program that outputs numbers 1 -> 100
with each multiple of 3 being Fizz
each multiple of 5 being Buzz
and each multiple of both being FizzBuzz
"""

def main():
    #set in a range
    for n in range(1,100):
        #multiple of three
        if n % 3 == 0:
            #output
            print('Fizz', end='')
        #multiple of five
        elif n % 5 == 0:
            #output
            print('Buzz', end='\n')
        #neither
        else:
            print(n, end='\n')

if __name__=='__main__':
    main()