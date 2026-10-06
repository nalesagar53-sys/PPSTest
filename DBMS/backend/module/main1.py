from os import mkdir,rmdir
import os
from pathlib import Path 

F_PATH="C:\\Users\\kaush\\Desktop\\Genx\\DBMS\\backend\\module\\DB\\"



def main():
    current_Db="__none"
    while True:
        cmd1=input("\t>>>").lower()

        splited_cmd1=cmd1.split(" ")

        if (splited_cmd1[0]=="mk" or splited_cmd1[0]=="del") and (len(splited_cmd1)==3 and splited_cmd1[1]=="db"):

            if ";" in splited_cmd1[2]:

                splited_cmd1[2]=splited_cmd1[2].replace(";","")

            if os.path.exists(F_PATH + splited_cmd1[2]):

                if splited_cmd1[0]=="del":
                    rmdir(F_PATH+splited_cmd1[2])
                    print("\tMessage: Database is exists....")

                elif splited_cmd1[0]=="mk":
                    print("\tMessage:DB is already exists")

            else:
                    if splited_cmd1[0]=="mk":
                        mkdir(F_PATH+splited_cmd1[2])
                        print("\tMessage: DB is create successfully")
                            

                    elif splited_cmd1[0]=="del":
                        print("\tMessage: DB is deleted successfully")

        elif splited_cmd1[0]=="vapar"and len(splited_cmd1)==2 :

            current_Db=splited_cmd1[1]


        elif splited_cmd1[0]=="mk" and splited_cmd1[1]=="table" and len(splited_cmd1)==3 :
            if current_Db!="__none":

                ct1=splited_cmd1[2].split("[")
                open(F_PATH+current_Db+"\\"+ct1[0]+".csv","w")
            else:
                print("\tMessage: please select any database first")


                    

        elif splited_cmd1[0]=="gharija":
            exit()


if __name__=="__main__":
    main()
                    


