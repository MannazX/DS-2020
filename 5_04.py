# ex 4 lec 5

def asd(list):
    i = 0
    t = 0
    for i in list:
        print("i in this loop is: ", i)
        t += list[i-1]
    print("t is:" , t)
    return t

a = [1,2,3,4,5,6]
print(asd(a))
