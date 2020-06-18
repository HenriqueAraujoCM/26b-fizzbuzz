def isnotlucky(val):
    while val:
        digit = val%10

        if digit == 3:
            print("lucky")
            return False

        val //= 10
    return True

def fizzbuzz(val):
    if isnotlucky(val):
        if val%3 != 0:
            if val%5 != 0:
                print(val)
            else:
                print("buzz")
        else:
            if val%5 != 0:
                print("fizz")
            else:
                print("fizzbuzz")

for i in range(1,20):
    fizzbuzz(i)