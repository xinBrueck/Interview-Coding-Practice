#given the implementation of cons below, which constructed a pair
#write a function: car to return the first element of the pair
#write a function: cdr to return the second element of the pair

##this is the implementation of cons
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

##This implementation of cons, takes in two parameters a & b
##then in cons, it calls a function "pair", which calls another function f
##and cons return the function "pair"
##so my implementation of car/cdr would take the function "pair" as the parameter
##which means, I will need to write the function that "pair" take to return either a, or b

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

#test
print(car(cons(1,8)))
print(cdr(cons(7,10)))
