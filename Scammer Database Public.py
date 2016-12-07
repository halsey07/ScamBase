import datetime
import sqlite3
import time
import os
now = datetime.datetime.now()




def menu(): 
    print ("="*60)
    print ("Welcome to the Scammer Database")
    print ("="*60)
    print ("This program was made by OG HorizoN for the SSL Discord")
    print ("="*60)
    print ("Press 1 to store a scammer")
    print ("\n")
    print ("Press 2 to view the scammer list")
    print ("\n")
    print ("Press 3 to delete a scammer")
    print ("\n")
    print ("Press 4 to EXIT")
    print ("\n")
    print ("Press 5 to install the database (FIRST USE)")
    print ("\n")

    
    Select = input("Select an option ")

    if Select == "1":
        add()
    elif Select == "2":
        view()
    elif Select == "3":
        delete()
    elif Select == "4":
        exit()
    elif Select == "5":
        install()
    else:
        print("Not a valid input... please try again:")
        menu()

def add():
    conn = sqlite3.connect("ScamBase.db")
    c= conn.cursor()
    print ("<<<Adding scammer>>>")
    print ("\n")
    company_name = input("Please input the company name: ")
    number = input("Please input the phone number you dialled: ")
    etc = input("Please input any other information we need to know: ")
    date=now
    c.execute("""INSERT INTO ScamBase
               (company_name,number,etc,date)
               VALUES(?,?,?,?)""",(company_name,number,etc,date))
    conn.commit()
    print("\n")
    print("Scammer",company_name,"Added on",now)
    print ("\n")
    menu()

def view():
    conn = sqlite3.connect("ScamBase.db")
    c= conn.cursor()
    c.execute("""SELECT * FROM ScamBase""")
    rows = c.fetchall()

    for eachRow in rows:
        print("\nID:{0}\nCompany Name:{1}\nNumber:{2}\nETC Info:{3}\nDate:{4}".format(eachRow[0],eachRow[1],eachRow[2],eachRow[3],eachRow[4]))
    print("\n")
    input("Press enter to return to menu ")
    print ("\n")
    menu()

def delete() :
    conn = sqlite3.connect("ScamBase.db")
    c= conn.cursor()
    Id=input("Enter the ID of the scammer to delete ")
    c.execute("DELETE FROM ScamBase WHERE ID=?", (Id,))
    conn.commit()
    print("Scammer",Id,"deleted from database")
    print ("\n")
    menu()

def install() :
    os.remove("ScamBase.db")
    open("MakeDatabase.py")
    menu()


menu()


