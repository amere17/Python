import csv
import sys
import pandas as pd
from datetime import datetime

date_now = datetime(2018, 12, 1, 00, 00, 00)


def main():
    print()
    print("****************************************************")
    print("************ Welcome to DataBase TDMS **************")
    print("****************************************************")

    while True:
        print()
        global date_now
        dat_now_temp = input("Enter 0 (Default now Date) or  Enter a new now Date (DD/MM/YY HH:MM): ")
        if dat_now_temp != '0':
            date_now = datetime.strptime(dat_now_temp, '%d/%m/%Y %H:%M')
            date_now = date_now.strftime('%d/%m/%Y %H:%M')
        else:
            dat_now_temp = "01/12/2018 00:00"
            date_now = datetime.strptime(dat_now_temp, '%d/%m/%Y %H:%M')
            date_now = date_now.strftime('%d/%m/%Y %H:%M')
        print(date_now)
        choice = input(""" 1: Display | 2: Insert | 3: Update | 4: Erase | 5: Exit
        Please enter your choice: """)

        if choice == "1":
            print()
            Display()
        elif choice == "2":
            print()
            Insert()
        elif choice == "3":
            print()
            Update()
        elif choice == "4":
            print()
            Erase()
        elif choice == "5":
            sys.exit()
        else:
            print()
            print("------ You must only select 1,2,3,4 or 5 --------")
            print("------------ Please try again -------------------")


# --------------------------------------------------------------
def Display():
    global date_now
    single = []
    history = []
    print("Please insert the index of your choice")
    print("1 - Value")
    print("2 - History")
    opt = int(input())
    print()
    date_now = datetime.strptime(date_now, '%d/%m/%Y %H:%M')
    if opt == 1:
        num = input("Please insert the wanted Parameter: ")
        firs_name = input("Please insert the First Name: ")
        las_name = input("Please insert the Last Name: ")
        date_da = input("Please Insert the valid Date Time: ")
        if ' ' in date_da:
            date_d = datetime.strptime(date_da, '%d/%m/%Y %H:%M')
            with open('dbp.csv', 'r') as fil:
                reader = csv.reader(fil)
                first_row = next(reader)
                for i in reader:
                    row = list(enumerate(i))
                    date_c = datetime.strptime(row[6][1], '%d/%m/%Y %H:%M')
                    date_t = datetime.strptime(row[7][1], '%d/%m/%Y %H:%M')
                    if firs_name == row[0][1] and las_name == row[1][1] and num == row[2][
                        1] and date_d.date() == date_c.date():
                        if date_now >= date_t and row[8][1] == '':
                            single.clear()
                            single.append(num)
                            single.append(row[3][1])
                            single.append(row[4][1])
                        if date_now == date_t and row[8][1] == '0':
                            break
                        if date_now < date_t and row[8][1] == '0':
                            single.clear()
                            single.append(num)
                            single.append(row[3][1])
                            single.append(row[4][1])
                            break
                        if date_now == date_t and row[8][1] != '' and row[8][1] != '0':
                            single.clear()
                            single.append(num)
                            single.append(row[8][1])
                            single.append(row[4][1])
                            break
                        if date_now < date_t and row[8][1] != '' and row[8][1] != '0':
                            single.clear()
                            single.append(num)
                            single.append(row[3][1])
                            single.append(row[4][1])
                            break
        else:
            date_d = datetime.strptime(date_da, '%d/%m/%Y')
            with open('dbp.csv', 'r') as fil:
                reader = csv.reader(fil)
                first_row = next(reader)
                for i in reader:
                    row = list(enumerate(i))
                    date_c = datetime.strptime(row[6][1], '%d/%m/%Y %H:%M')
                    date_t = datetime.strptime(row[7][1], '%d/%m/%Y %H:%M')
                    if firs_name == row[0][1] and las_name == row[1][1] and num == row[2][
                        1] and date_d.date() == date_c.date():
                        if date_now >= date_t and row[8][1] == '':
                            single.clear()
                            single.append(num)
                            single.append(row[3][1])
                            single.append(row[4][1])
                        if date_now == date_t and row[8][1] == '0':
                            break
                        if date_now < date_t and row[8][1] == '0':
                            single.clear()
                            single.append(num)
                            single.append(row[3][1])
                            single.append(row[4][1])
                            break
                        if date_now == date_t and row[8][1] != '' and row[8][1] != '0':
                            break
                        if date_now < date_t and row[8][1] != '' and row[8][1] != '0':
                            single.clear()
                            single.append(num)
                            single.append(row[8][1])
                            single.append(row[4][1])
                            break
        if len(single) != 0:
            show_d(single)
            print(date_now)
    elif opt == 2:
        num = input("Please insert the wanted Parameter: ")
        firs_name = input("Please insert the First Name: ")
        las_name = input("Please insert the Last Name: ")
        date_da = input("Please Insert the valid Date Time: ")
        date_bef = input("Please Insert start valid DateTime: ")
        date_af = input("Please Insert end valid DateTime: ")
        date_d = datetime.strptime(date_da, '%d/%m/%Y')
        date_be = datetime.strptime(date_bef, '%d/%m/%Y %H:%M')
        date_aft = datetime.strptime(date_af, '%d/%m/%Y %H:%M')

        with open('dbp.csv', 'r') as fil:
            reader = csv.reader(fil)
            first_row = next(reader)
            for i in reader:
                row = list(enumerate(i))
                date_c = datetime.strptime(row[6][1], '%d/%m/%Y %H:%M')
                date_t = datetime.strptime(row[7][1], '%d/%m/%Y %H:%M')
                if firs_name == row[0][1] and las_name == row[1][1] and num == row[2][1] \
                        and date_d.date() == date_c.date() \
                        and date_be <= date_t <= date_aft:
                    history.append(row)
        print(num + " = " + comp_loinc(num))
        for j in enumerate(history):
            print(j)



def show_d(data_arr):
    with open('LoincTable.csv', 'r') as dataloinc:
        reader2 = csv.reader(dataloinc)
        for j in reader2:
            row2 = list(enumerate(j))
            if data_arr[0] == row2[0][1]:
                print(row2[1][1] + " " + data_arr[1] + " " + data_arr[2])


def History(data_arr):
    pass


# --------------------------------------------------------------
def Insert(FirstName=0, LastName=0, ParameterName=0, rowe=-1, notAll=False, Val='', Value = 0):
    if not notAll:
        while True:
            FirstName = input("First Name: ")
            LastName = input("Last Name: ")
            if Name_Valid(FirstName, LastName, 1):
                break
            else:
                print("**** Please Insert a valid name ****")
        ParameterName = input("Parameter Name: ")
        Value = int(input("Insert Value: "))
    is_Valid = False
    switch = 0
    while not is_Valid:
        try:
            if switch == 0:
                Valid_Start = input("Insert Valid Start Time (DD/MM/YYYY HH:MM):")
                Valid_Start = datetime.strptime(Valid_Start, '%d/%m/%Y %H:%M')
                Valid_Start = Valid_Start.strftime('%d/%m/%Y %H:%M')
                switch = 1
            if switch == 1:
                Valid_Stop = input("Insert Valid Stop Time (DD/MM/YYYY HH:MM): ")
                Valid_Stop = datetime.strptime(Valid_Stop, '%d/%m/%Y %H:%M')
                Valid_Stop = Valid_Stop.strftime('%d/%m/%Y %H:%M')
                is_Valid = True
        except ValueError:
            print("**** Please Insert valid Date & Time (DD/MM/YYYY HH:MM) ****")
        break
    Transaction_time = date_now
    unit = get_unit(ParameterName)
    csv_Line = [FirstName, LastName, ParameterName, Value, unit, Valid_Start, Valid_Stop, Transaction_time, Val]
    if rowe != -1:
        AddLine(csv_Line, rowe-1)
    else:
        AddLine(csv_Line)


def Erase():
    csv_file = csv.reader(open('dbp.csv', "r+"), delimiter=",")
    while True:
        FirstName = input("First Name: ")
        LastName = input("Last Name: ")
        parmeter = input("Parameter Name: ")
        if Name_Valid(FirstName, LastName):
            break
        else:
            print("**** Please Insert a valid name ****")
    first_row = next(csv_file)
    data2show = Show_Data(csv_file, FirstName, LastName, parmeter)
    print(data2show)
    Row2Erase = CheckRow(data2show, "Insert Row To Delete: ")
    val = find_val(Row2Erase)
    RowErase(Row2Erase - 1)
    Insert(FirstName, LastName, parmeter, Row2Erase, True, '0', val)


def Update():
    csv_file = csv.reader(open('dbp.csv', "r+"), delimiter=",")
    while True:
        FirstName = input("First Name: ")
        LastName = input("Last Name: ")
        if Name_Valid(FirstName, LastName):
            break
        else:
            print("**** Please Insert a valid name ****")
    ParameterName = input("Parameter Name: ")
    Value = int(input("Insert Value: "))
    data2show = Show_Data(csv_file, FirstName, LastName, ParameterName)
    Row2Erase = CheckRow(data2show, "Insert Row To Update:")
    val = find_val(Row2Erase)
    RowErase(Row2Erase-1)
    Insert(FirstName, LastName, ParameterName, Row2Erase, True, Value, val)


# --------------------------------------------------------------
def find_val(row1):
    with open('dbp.csv', 'r') as valfile:
        reader = csv.reader(valfile, delimiter=",")
        for idx, item in enumerate(reader):
            row = list(enumerate(item))
            if row1 == idx:
                return row[3][1]
    return 0
def Name_Valid(first, last, opt=0):
    cvFile = csv.reader(open('dbp.csv', "r+"), delimiter=",")
    for row in cvFile:
        if first == row[0] and last == row[1]:
            return True
    if first.isalpha() and last.isalpha() and opt == 1:
        return True
    return False


def DateTime_Valid(dt):
    if isinstance(dt, datetime):
        return True
    return False


def Show_Data(file, first, last, Parameter=0):
    data2show = []
    i = 0
    for row in file:
        if row:
            if first == row[0] and last == row[1] and Parameter == row[2]:
                row.insert(0, i)
                data2show.append(row)
            i += 1
    for j in data2show:
        print(j)
    return data2show


def RowValid(rowNum, data):
    for row in data:
        if rowNum == row[0]:
            return True
    return False


def RowErase(rowNum):
    data = pd.read_csv("dbp.csv")
    data.drop(rowNum, inplace=True)
    data.to_csv("dbp.csv", sep=',', encoding='utf-8', index=False)


def CheckRow(data, str1):
    while True:
        Row2Erase = int(input(str1))
        Valid_id = RowValid(Row2Erase, data)
        if Valid_id:
            break
        else:
            print("Row " + Row2Erase + " Not Valid, Please insert a valid row")
    return Row2Erase


def AddLine(csv_line, row=-1):
    if row != -1:
        with open('dbp.csv', 'r') as f:
            reader = csv.reader(f)
            lines = list(reader)
            lines.insert(row + 1, csv_line)
            df = pd.DataFrame(lines)
            df.to_csv(r"dbp.csv", sep=',', encoding='utf-8', index_label=False, index=False, header=0)
        f.close()
    else:
        with open('dbp.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(csv_line)
        f.close()


def comp_loinc(num):
    with open('LoincTable.csv', 'r') as loincfile:
        reader = csv.reader(loincfile, delimiter=",")
        for i in reader:
            row = list(enumerate(i))
            if num == row[0][1]:
                return row[1][1]
    return num


def get_unit(parameter):
    with open('dbp.csv', 'r') as unitfile:
        reader = csv.reader(unitfile, delimiter=",")
        for i in reader:
            row = list(enumerate(i))
            if parameter == row[2][1]:
                return row[4][1]
def checkPerson(data2show):
    print("****************************************************")
    print("***** Invalid Input, Please Try another Input ******")
    print("****************************************************")


# --------------------------------------------------------------
main()
