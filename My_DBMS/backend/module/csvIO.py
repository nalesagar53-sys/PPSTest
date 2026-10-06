def main():

    # file1=open(".\\..\\..\\..\\dummy_data.csv","r")
    # data = file1.read()
    # file1.close()
    # print(data)
    data={

        "Name":"Rajesh",
        "age":13
    }
    file2=open("hello.csv","w")
    file2.write(str(data))



if __name__=="__main__":
    main()