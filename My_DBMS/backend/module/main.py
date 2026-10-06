from os import mkdir,rmdir
import os


BASE_PATH="C:\\Users\\kaush\\Desktop\\Genx\\My_DBMS\\backend\\module\\Databases\\"
def main():
    current_db="__none__"
    while True:
          
        cmd = input("\t>>>").lower()

        splited_cmd=cmd.split(" ")

        if (splited_cmd[0]=="make" or  splited_cmd[0]=="del") and (len(splited_cmd)== 3 and splited_cmd[1]=="db"):
             
                if ";" in splited_cmd[2]:
                    
                    splited_cmd[2]=splited_cmd[2].replace(";","")

                if os.path.exists(BASE_PATH + splited_cmd[2]):
                    
                    if splited_cmd[0]=="del":
                        rmdir(BASE_PATH + splited_cmd[2])
                        print("\tMessagae :DB is deleted..")

                    elif splited_cmd[0]=="make":
                        print("\tmessage :DB is already exists...")
                    
                else:
                         if splited_cmd[0]=="make":
                            mkdir(BASE_PATH + splited_cmd[2])
                            print("\tmessage :DB is created")

                         elif splited_cmd[0]=="del":
                             print("\tMessagae :DB is does'n exits..")
        elif splited_cmd[0]=="vapar"and len(splited_cmd)==2 :

            current_db=splited_cmd[1]


        elif splited_cmd[0]=="make" and splited_cmd[1]=="table" and len(splited_cmd)==3 :
            if current_db!="__none__":

                ct=splited_cmd[2].split("[")
                open(BASE_PATH+current_db+"\\"+ct[0]+".csv","w")
            else:
                print("\tMessage: please select any database first")
                




        elif splited_cmd[0]=="gharija":
            exit()





if __name__=="__main__":
    main()