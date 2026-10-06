facto=1
def fact(no):
    global facto
    if no<2:
        return facto
    
    facto*=no
    return fact(no-1)



def main():
    a=fact(5)
    print(a)



if __name__=="__main__":
    main()