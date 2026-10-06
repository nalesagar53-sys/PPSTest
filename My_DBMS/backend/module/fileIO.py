def main():
    file1=open("hello.txt","w")
    file1.write("hello world after opening file in 'w'")
    file2=open("hello2.txt","r")
    file2_data=file2.read()
    print(file2_data)
    file3=open("hello3.txt","a")
    file3.write("\nNamskar jantarmantar")



if __name__=="__main__":
    main()