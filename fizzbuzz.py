from enum import Enum
#enumeration of the types of values
class Name(Enum):
     LUCKY = 1
     FIZZ = 2
     BUZZ = 3
     FIZZBUZZ = 4
     INTGR = 5

#checks if the value has the number 3 on it
def isnotlucky(val):
    while val:
        digit = val%10

        if digit == 3:
            #print("lucky", end ="")
            return False

        val //= 10
    return True

#checks which of the types the value is
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

#stores each response and the count of the values
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
    
    retString = ""

    for s in solution:
        #print(s, end=" ")
        retString +=str(s) +" "

    retString += "fizz: " + str(counts[Name.FIZZ]) + " buzz: " + str(counts[Name.BUZZ]) + " fizzbuzz: " + str(counts[Name.FIZZBUZZ]) + " lucky: " + str(counts[Name.LUCKY]) + " integer: " + str(counts[Name.INTGR])
    return retString

rtrn = fizzbuzz(range(1,21))
print("return is:", rtrn)

solution = "1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz fizz: 4 buzz: 3 fizzbuzz: 1 lucky: 2 integer: 10"

print("solution should be:", solution)

if(rtrn == solution):
    print("correct")
else:
    print("incorrect")