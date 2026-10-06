def main():
    no =int(input("Enter number:"))
    
    fact=1
    for i in range(no,1,-1):
        fact *= i
    print(fact)
    


if __name__=="__main__":
    main()