def Triangle():
        a = eval(input("Enter the base of your triangle : ")) #For the exercise's example, use 9
        c = int(a/2)+1
        if a%2==1:
                for i in range(c):
                    if i < int(a/2):
                        print("*"*(i+1))
                    else:
                        for i in range(c):
                            print("*"*(c-(i)))
        else:
                    for i in range(c):
                        if i < int(a/2):
                            print("*"*(i+1))
                        else:
                            for i in range(c-1):
                                print("*"*(c-(i+1)))


Triangle()
