import os

BASE_PATH = "C:\\Users\\kaush\\Desktop\\Genx\\My_DBMS\\backend\\module\\Databases\\"

cmd_len3 = ("make","del","fill","all")
cmd_len2 = ("vapar","db")

postfix_2_for_len3 = ("db","table","in")  
postfix_2_for_len2 = ("list",)

postfix_3_for_len3 = ("data",)

current_db = "__base__"

def create_directory(dirname:str)->str:
    if os.path.exists(BASE_PATH+dirname):
        return f"MESSAGE : DATABASE ALREADY EXIST WITH SAME NAME {dirname}"
    
    os.mkdir(BASE_PATH+dirname)
    return "MESSAGE : DATABASE CREATED SUCCESFULLY "

def delete_directry(dirname:str)->str:
    if os.path.exists(BASE_PATH+dirname):
        os.rmdir(BASE_PATH+dirname)
        return "MESSAGE : DATABASE DELETED SUCCESSFULLY "

    return "MESSAGE : DATABASE DOESENT EXISTIS"




def table_formatter(header:list , data_lists:list )-> None:
    
    column_width =  []
    
    for col in range(0,len(header)):

        maxx = len(header[col])

        for data in range(0,len(data_lists)):

            if len(data_lists[data][col]) > maxx:
                maxx = len(data_lists[data][col])   

        column_width.append(maxx)


    padding = int(len(column_width) * 2.5)
    width = (sum(column_width))+padding

    line = "+"+width*"-"+"+"

    print(line)

    print("| ",end="")
    for head in header:
           print(head,"| ",end="")
    print()

    print(line)

    for data in data_lists:
        print("| ",end="")

        for i,j in zip(data,column_width):
            print(i+((j-len(i))*" "),"| ",end="")
        print()

    print(line)


def column_formater(header:str, data_list: list )-> None:

    copy_data_list = tuple(data_list)
    list(copy_data_list).append(header)

    max = 0

    for word in copy_data_list :
        word_len = len(word)

        if word_len > max:
            max = word_len

    horizontal_line = "+"+((max+2) * "-")+"+"
    print(horizontal_line)
    print("|",header+((max-len(header)))*" ","|")
    print(horizontal_line)

    for td in data_list:
        print("|",td+((max-len(td))*" "),"|")

    print(horizontal_line)

def format_cmd_input(Input_cmd:str)->tuple:

    Input_cmd = Input_cmd.split(" ")
    global current_db

    if((Input_cmd[0] in cmd_len3) and len(Input_cmd) == 3) and (Input_cmd[1] in postfix_2_for_len3):

        if Input_cmd[1] == "db" and Input_cmd[0] == "make":
            print(create_directory(Input_cmd[2]))         

        elif (("table" == Input_cmd[1]) and current_db != "__base__") and Input_cmd[0] == "make":
            col_name = (Input_cmd[2].replace("]","")).split("[")

            if os.path.exists(BASE_PATH+current_db+"\\"+col_name[0]+".csv"):
                print(f"\tMESSAGE : TABLE ALREADY EXISTS WITH THE NAME `{col_name[0]}`")
                
            else:
                # col_name = (Input_cmd[2].split("[")).replace("]","")
                table_file = open(BASE_PATH+current_db+"\\"+col_name[0]+".csv","w")
                table_file.write(col_name[1])
                print("\tMESSAGE : TABLE CREATED SUCCESFULLY")

        elif Input_cmd[1] == "db" and Input_cmd[0] == "del":
            print(delete_directry(Input_cmd[2]))

        elif (("table" == Input_cmd[1]) and current_db != "__base__") and Input_cmd[0] == "del":
            print(delete_directry(current_db+"\\"+Input_cmd[2]+".csv"))

        elif (Input_cmd[0] == "fill" and Input_cmd[1] == "in"):
            # "schedule[(1,yash),(2,raj),(3,suyash,1000)]"
            col_name = (Input_cmd[2].replace("]","")).split("[")

            # ["schedule","(1,yash),(2,raj),(3,suyash,1000)"]

            if os.path.exists(BASE_PATH+current_db+"\\"+col_name[0]+".csv"):
                data1 = (col_name[1].replace(")","")[1:]).replace(",(","\n")
                data = col_name[1].replace(")","").split(",(")
                # ['(1,yash','2,raj','3,suyash,1000']

                data[0] = data[0][1:]
                # ['1,yash','2,raj','3,suyash,1000']

                for i in range(0,len(data)):
                    data[i] = data[i].split(",")

                # [['1','yash'],['2','raj'],['3','suyash','1000']]
                
                f_data = open(BASE_PATH+current_db+"\\"+col_name[0]+".csv","r").read()
                header_count = len((f_data.split("\n")[0]).split(","))

                to_write = True

                for i in data:
                    if len(i) != header_count:
                        # print("\tMESSAGE: VALUE COUNT DOESENT MATCH WITH THE COLUMN COUNT")
                        to_write = False
                        break

                # data = data[0:len(data)-1]
                if to_write :
                    # # [['1','yash'],['2','raj'],['3','suyash','1000']]

                    # data = (str(data).replace("[","").replace("'","").replace("],","\n"))
                    # # 1,yash\n2,raj \n 3,suyash,1000]]

                    # data = data[0:len(data)-2]
                    # # 1,yash\n2,raj \n 3,suyash,1000

                    file = open(BASE_PATH+current_db+"\\"+col_name[0]+".csv","a")
                    file.write("\n"+data1)
                    print("\tMESSAGE: DATA INSERTED SUCCESSFULLY")

                else:
                    print("\tMESSAGE: VALUE COUNT DOESENT MATCH WITH THE COLUMN COUNT")

            else :
                print("\tMESSAGE TABLE DOESENT EXISTS")

        else:
            print("\tMESSAGE : PLEASE SELECT ANY DB FIRST USE CMD (vapar <db_name>)")


    elif (Input_cmd[0] in cmd_len2) and len(Input_cmd) == 2:

        if Input_cmd[0] == "vapar" and os.path.exists(BASE_PATH+Input_cmd[1]):
            current_db = Input_cmd[1]
            print(f"\tMESSAGE : `{current_db}` DATABASE IN USE")

        elif Input_cmd[0] == "db" and Input_cmd[1] == "list":

            dir_list = os.listdir(BASE_PATH)

            for dir in dir_list:
                if not os.path.isdir(BASE_PATH+dir):
                    dir_list.remove(dir)

            column_formater("Databases",dir_list)
            

        else:
            print(f"\tMESSAGE : DATABASE DOESENT EXISTS WITH THE NAME {Input_cmd[1]}")
            return

    elif (Input_cmd[0] in cmd_len3) and (Input_cmd[2] in postfix_3_for_len3) and len(Input_cmd)==3:

        if current_db != "__base__":

            data = open(BASE_PATH+current_db+"\\"+Input_cmd[1]+".csv","r").read()

            data = data.split("\n")
            header_data = data[0].split(",")

            data.pop(0)

            for data_index in range(0,len(data)):
                data[data_index] = data[data_index].split(",")

            table_formatter(header_data,data)

    elif Input_cmd[0] == "gharija":
        exit()

    else:
        print(f"\tMESSAGE : UNAPROPRIATE COMMAND FOUND \n\tREFERENCE EXAMPLE : make {"table <table>[col1,col2,...coln]" if "table" in Input_cmd else "db <dbname>"}")

import sys


def main():

    print("+-----------------------------------------------------------------------+")
    print("| WELCOME NUCLEUS DABMS made by - Yash Deshmukh                         |")
    print("+-----------------------------------------------------------------------+")
    print("| Instructions : for help or DOCUMENTATION type '-h' or 'help'          |")
    print("| This project has copyright licenced by @Nucleus_Programming           |")
    print("+-----------------------------------------------------------------------+")

    if len(sys.argv) > 1:
        if sys.argv[1] == "--h" or sys.argv[1] == "help":
            print("\n\n")
            data = open(BASE_PATH+"root\\query.csv","r").read()
            
            data = data.split("\n")
            header_data = data[0].split(",")
            
            data.pop(0)
            
            for data_index in range(0,len(data)):
                data[data_index] = data[data_index].split(",")
            
            table_formatter(header_data,data)
            

    while True:
        cmd = input("my_db>").lower()

        if cmd == "clear":
            os.system("cls")
        else:
            format_cmd_input(cmd)

if __name__ == "__main__":
    main()