# This allows symbolic functions / integrals
from sympy import *
# Allows output to be paused
import time

def Bisection(f,a:float,b:float,eps:float):
    start=a
    end=b
    c=(a+b)/2

    while Abs(f.subs(x,c)) >= eps:
        if f.subs(x,c)*f.subs(x,start) < 0:
            end = c
        else: start = c
        
        c = (start+end)/2

    return [c,f.subs(x,c)]

if __name__ == '__main__':
    x = symbols('x')

    print("According to the bisection method, the [zero,eps] for problem #1 is \n\t", Bisection(x**3+2*x-2, 0, 1, 0.000025))
    time.sleep(2.0)
    print("According to the bisection method, the [zero,eps] for problem #2 is \n\t", Bisection(x*exp(x)-2, 0, 1, 0.000025))
    time.sleep(2.0)
    print("According to the bisection method, the [zero,eps] for problem #3 is \n\t", Bisection(sin(x), 2, 4, 0.000025))
    time.sleep(2.0)
    
    bonus = input("Would you like to run the bisection method on your own function? (yes or no) ")
    
    # ~~~~~~~~~~~~~~~~~`Added bonus: Accepts user inputs!~~~~~~~~~~~~~~~~~``
    if bonus.lower() == "yes" or bonus.lower() == "y":
        func = input("What is your function? \n (use x as your variable, e.g. cos(x), and use ** for exponentiation, e.g. x**2 for x squared) ")
        a = input("What is your starting point? ")
        b = input("What is your ending point? ")
        eps = input("What is your error tolerance? ")
        time.sleep(1.0)
        print("According to the bisection method, the [zero,eps] for your input is \n\t", Bisection(parse_expr(func),float(parse_expr(a)),float(parse_expr(b)),float(parse_expr(eps))))