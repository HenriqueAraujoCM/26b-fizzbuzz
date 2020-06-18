from enum import Enum
class Name(Enum):
     LUCKY = 1
     FIZZ = 2
     BUZZ = 3
     FIZZBUZZ = 4
     INTGR = 5

def isnotlucky(val):
    while val:
        digit = val%10

        if digit == 3:
            #print("lucky", end ="")
            return False

        val //= 10
    return True

def isfizzbuzz(val):

    lucky = 0
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    intgr = 0

    if isnotlucky(val):
        if val%3 != 0:
            if val%5 != 0:
                intgr += 1
                return Name.INTGR
            else:
                buzz += 1
                return Name.BUZZ
        else:
            if val%5 != 0:
                fizz += 1
                return Name.FIZZ
            else:
                fizzbuzz += 1
                return Name.FIZZBUZZ
    lucky += 1
    return Name.LUCKY

def fizzbuzz(vals):

    solution = []

    names = {Name.LUCKY:"lucky", Name.FIZZ:"fizz", Name.BUZZ:"buzz", Name.FIZZBUZZ:"fizzbuzz"}
    counts = {Name.LUCKY:0, Name.FIZZ:0, Name.BUZZ:0, Name.FIZZBUZZ:0, Name.INTGR:0}

    for i in vals:
        res = isfizzbuzz(i)
        counts[res] += 1
        if res == Name.INTGR:
            solution.append(i)
        else:
            solution.append(names[res])
        
    for s in solution:
        print(s, end=" ")
    print("fizz:", counts[Name.FIZZ], "buzz:", counts[Name.BUZZ], "fizzbuzz:", counts[Name.FIZZBUZZ], "lucky:", counts[Name.LUCKY], "integer:", counts[Name.INTGR])

fizzbuzz(range(1,20))