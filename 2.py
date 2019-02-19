def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
first = 1
second = 2
sum = 0
while (first <= 4000000):
    if isEven(first):
        sum += first
    new = first + second
    first = second
    second = new
print ("Sum is: {0}").format(sum)
