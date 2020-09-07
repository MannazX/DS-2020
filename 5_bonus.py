# ex bonus lec 5
letterX = ""
i = 0
iMax = 5

while i < iMax:
    letterX += letterX.join("*")
    print(letterX)
    i += 1

while i > 1:
    letterX = letterX[:-1]
    print(letterX)
    i -= 1
    #print(" i is: ", i)

# written by Gergo Gyori
