from tkinter import filedialog
from os import rename as rn
from os import remove as rm
from pathlib import Path
from os import path
import csv

intial_file = "/home/nishant/Documents/Hopper/" + "Hopper.txt"
interim_csv_file = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/out.csv"
final_file = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Hopper.csv"



def File_Selection():
    #Creation of file dialog box and renaming the generic file to Hooperr.txt

    try:
        filename = filedialog.askopenfilename(initialdir="/home/nishant/Documents", title="Select the Hopper File",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        file_to_delete = initial_file

        if path.exists(file_to_delete):
            rm(Path(file_to_delete))
            rn(filename,file_to_delete)
            print("File removed and renamed")
        else:
            rn(filename,file_to_delete)
            print("File renamed")
    except Exception as e:
        print("Failed to execute function" + str(e))
        raise SystemExit

"""
def Fetch_Data():
    #Removes the unncessary data from the file.
    file_path = interim_csv_file
    with open(file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
    with open(file_path, "w", encoding="UTF-8") as file:
        check = "M1GMG"
        for line in lines:
            if check in line:
                file.write(line)

"""
def File_Conversion():
    #Converts the Hopper.txt fixed width file to out.csv delimited file
    IN_FILE = initial_file
    OUT_FILE = interim_csv_file
    RANGES = ((0, 10), (18, 19), (45, 18), (66, 19), (88, 19), (114, 19),
              (136, 19), (157, 19), (179, 19), (203, 19), (223, 10))
    try:
        rfp = open(IN_FILE, 'r', encoding="UTF-8")
    except IOError:
        print("Could not read from", IN_FILE)
        raise SystemExit

    try:
        wfp = open(OUT_FILE, 'w', encoding="UTF-8")
    except IOError:
        print("Could not write to", OUT_FILE)
        raise SystemExit
    for line in rfp:
        parts = []
        for rng in RANGES:
            parts.append(line[rng[0]:rng[0] + rng[1]].strip())
        wfp.write(",".join(parts) + "\n")

    rfp.close()
    wfp.close()
"""
def Add_Date_Time():
    # Date and time column are added to the hopper file
    ReadFile = interim_csv_file
    DateStamp = [str(input("Enter date of Hopper file (YYYY-MM-DD): "))]
    TimeStamp = [str(input("Enter time of Hopper file (HH:MM): "))]
    destination_file = final_file
    with open(ReadFile, "r+", encoding="UTF-8") as f_in, open(destination_file, 'w', encoding="UTF-8") as f_out:
        reader = csv.reader(f_in, delimiter=',')
        FileWriter = csv.writer(f_out)
        for line in reader:
            FileWriter.writerow(line + DateStamp + TimeStamp)
    rm(interim_csv_file)
    rm(initial_file)


def Push_Data_Into_Table():
    my_cursor.execute("use Hopper")
    my_cursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Hopper.csv' into table File_History fields terminated by ',' lines terminated by '\n'")
    mydb.commit()


File_Selection()

if path.exists(initial_file):
    File_Conversion()
else:
    print("Cant locate the text file to convert to csv file")


if path.exists(interim_csv_file):
    Fetch_Data()
else:
    print("Cant find to fetch the data")


if path.exists(final_file):
    rm(Path(final_file))
    Add_Date_Time()
else:
    Add_Date_Time()

Push_Data_Into_Table()
"""
File_Selection()
File_Conversion()