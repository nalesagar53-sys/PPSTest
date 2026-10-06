def main():
    a=[1,2,3,4,5,6,7,8,9,0]
    b=11
    length=len(a)
    print(length)
    for i in range(length-1,1,-1):
        print(a[i])
    a.pop()
    print(a)
    a.remove(2)
    print(a)
    a.append(b)
    print(a)


if __name__=="__main__":
    main()