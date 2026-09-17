def upsidedown(x):
    if x > 0:
        x= str(x)
        y= len(x)
        if y % 2 == 0:
            count =0
            for i in range(0,(y//2)):
                n = (y - i)
                for j in range((n-1),n):
                    if x[i] == x[n-1]:
                        count= count +1
                        if count !=(y//2):
                            break
                        else:    
                            print("x is a Palindrome ")
                    else:
                        print("x is not a Palindrome")
        else:
            count = 0
            for m in range(0,((y-1)//2)):
                k = (y - m)
                for n in range((k-1),k):
                    if x[m] == x[k-1]:
                        count = count +1
                        if count !=((y-1)//2):
                            break
                        else:
                            print("x is a Palindrome")
                    else:
                        print("x is not a Palindrome")  
    else:
        print("x is not a Palindrome")
upsidedown(11241)  
