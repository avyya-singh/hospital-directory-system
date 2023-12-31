import pickle
import os
from os import remove, rename


class hospital(object):
    def __int__(h):
        h.hid = 0
        h.hname = ""
        h.address = 0
        h.city = ""
        h.state = ""
        h.area = ""
        h.pin_code = 0
        h.dt_of_estb = ""
        h.email_id = ""
        h.contact1 = 0
        h.contact2 = 0
        h.ambulance_no = 0
        h.bed_no = 0
        h.specz = ""
        h.director = ""
        h.vax = ""
        h.categ = ""


    def add_rec(h):
        h.hid = int(input("Hospital Number ID: "))
        h.hname = input("Hospital Name: ")
        h.address = input("Hospital Address: ")
        h.city = input("City: ")
        h.state = input("State: ")
        h.area = input("Area: ")
        h.pin_code = int(input("Pin Code: "))
        h.dt_of_estb = input("Date Of Establishment: ")
        h.email_id = input("Email ID: ")
        h.contact1 = int(input("Contact No.: "))
        h.contact2 = int(input("Alternate Contact No.: "))
        h.ambulance_no = int(input("Ambulance No.: "))
        h.bed_no = int(input("Bed count: "))
        h.specz = input("Specialization: ")
        h.director = input("Name of Director: ")
        h.vax = input("Covid Vaccine (y/n): ")
        h.categ = input("Ctaegory (Govt / Pvt): ")


    def disp_rec(h):
        print("Hospital Number ID: ", h.hid)
        print("Hospital Name: ", h.hname)
        print("City: ", h.city)
        print("State: ", h.state)
        print("Are: ", h.area)
        print("Pin Code: ", h.pin_code)
        print("Date Of Establishment: ", h.dt_of_estb)
        print("Email ID: ", h.email_id)
        print("Contact No.: ", h.contact1)
        print("Alternate Contact No.: ", h.contact2)
        print("Ambulance No.: ", h.ambulance_no)
        print("Bed count: ", h.bed_no)
        print("Specialization: ", h.specz)
        print("Name of Director: ", h.director)
        print("Covid Vaccine (y/n): ", h.vax)
        print("Ctaegory (Govt / Pvt): ", h.categ)


    def display_rec(h):
        print("%-10s" % h.hid, "%-10s" % h.hname, "%-10s" % h.address, "%-10s" % h.city, "%-10s" % h.state,
              "%-10s" % h.area, "%-10s" % h.pin_code, "%-10s" % h.dt_of_estb, "%-10s" % h.email_id,
              "%-10s" % h.contact1, "%-10s" % h.contact2, "%-10s" % h.ambulance_no, "%-10s" % h.bed_no,
              "%-10s" % h.specz, "%-10s" % h.director, "%-10s" % h.vax, "%-10s" % h.categ)


    def modify_rec(h):
        h.hid = int(input("New Hospital Number ID: "))
        h.hname = input("New Hospital Name: ")
        h.address = input("New Hospital Address: ")
        h.city = input("New City: ")
        h.state = input("New State: ")
        h.area = input("New Area: ")
        h.pin_code = int(input("New Pin Code: "))
        h.dt_of_estb = input("New Date Of Establishment: ")
        h.email_id = input("New Email ID: ")
        h.contact1 = int(input("New Contact No.: "))
        h.contact2 = int(input("New Alternate Contact No.: "))
        h.ambulance_no = int(input("New Ambulance No.: "))
        h.bed_no = int(input("New Bed count: "))
        h.specz = input("New Specialization: ")
        h.director = input("New Name of Director: ")
        h.vax = input("New Covid Vaccine (y/n): ")
        h.categ = input("New Ctaegory (Govt / Pvt): ")




def write_record():
    try:
        rec = hospital()
        file = open("hospital.dat", "ab")
        rec.add_rec()
        pickle.dump(rec, file)
        file.close()
        print("Record added in file")
        input("Press any key to cont ....")
    except:
        pass


def display_all():
    print(40 * "=")
    print("\nHospital Records\n")
    print(40 * "=")
    try:
        file = open("hospital.dat", "rb")
        while True:
            rec = pickle.load(file)
            rec.display_rec()




    except EOFError:
        file.close()
        print(40 * "=")
        input("Press any key to cont ....")
    except IOError:
        print("file could not be opened")




# SEARCH CATEGORY
def search_hid():
    try:
        z=0
        print(40*"=")
        print("Record Searching By Hospital ID.")
        print(40*"=")
        n=int(input("Enter Hospital ID to search: "))
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.hid==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")




def search_hname():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By Hospital Name.")
        print(40*"=")
        n=input("Enter Hospital Name to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.hname==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")




def search_city():
    try:    
        z=0
        print(40*"=")
        print("\n Record Searching By Hospital City.")
        print(40*"=")
        n=input("Enter Hospital City to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.city==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")


def search_state():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By Hospital state.")
        print(40*"=")
        n=input("Enter Hospital state to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.state==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")


def search_specz():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By specialization.")
        print(40*"=")
        n=input("Enter specialization to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.specz==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")


def search_cat():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By category.")
        print(40*"=")
        n=input("Enter category to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.categ==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")


def search_vax():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By covid vaccine.")
        print(40*"=")
        n=input("Enter covid vaccine to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.vax==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")


def search_area():
    try:
        z=0
        print(40*"=")
        print("\n Record Searching By area.")
        print(40*"=")
        n=input("Enter area to search: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.area==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")




# COUNT CATEGORY
count = 0
def countall():
    count = 0
    print(40*"=")
    print("\nHospital Records\n")
    print(40*"=")
    try:
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            count += 1


    except EOFError:
        file.close()
       
    except IOError:
        print("file could not be opened")
    print("Total Number of record are: ", count)
    input("Press any key to cont ....")


def countcity():
    try:
        count =0
        z=0
        print(40*"=")
        print("Record Count By City.")
        print(40*"=")
        n=input("Enter City: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.city==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


def countstate():
    try:
        count = 0
        z=0
        print(40*"=")
        print("Record Count By State.")
        print(40*"=")
        n=input("Enter state: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.state==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


def countspz():
    try:
        count = 0
        z=0
        print(40*"=")
        print("Record Count By specialzation.")
        print(40*"=")
        n=input("Enter specialzation: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.specz==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


def countcat():
    try:
        count = 0
        z=0
        print(40*"=")
        print("Record Count By category.")
        print(40*"=")
        n=input("Enter category: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.categ==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


def countvax():
    try:
        count = 0
        z=0
        print(40*"=")
        print("Record Count By vaccine.")
        print(40*"=")
        n=input("Enter vaccine: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.vax==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


def countarea():
    try:
        count = 0
        z=0
        print(40*"=")
        print("Record Count By area.")
        print(40*"=")
        n=input("Enter area: ")
        file=open("hospital.dat","rb")
        while True:
            rec=pickle.load(file)
            if(rec.area==n):
                z=1
                count += 1
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
       
    except IOError:
        print("file could not be opened")
    print("Total number of records are: ", count)
    input("Press any key to cont ....")


# EDIT CATEGORY
def modify_hid():
    z = 0
    try:
        n = int(input("Enter hospital number to modify: "))
        file = open("hospital.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.hid == n):
                z = 1
                print("Enter new data: ")
                rec.modify_rec()
                pickle.dump(rec, temp)
                print("Record updated")
            else:
                pickle.dump(rec, temp)


    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")
    except IOError:
        print("File could not be opened")


    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")




def modify_hname():
    z = 0
    try:
        n = input("Enter hospital name to modify: ")
        file = open("hospital.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.hname == n):
                z = 1
                print("Enter new data: ")
                rec.modify_rec()
                pickle.dump(rec, temp)
                print("Record updated")
            else:
                pickle.dump(rec, temp)


    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")
    except IOError:
        print("File could not be opened")


    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")




# INSERT CATEGORY
def insertafterhid():
    try:
        file = open('hospital.dat', 'rb')
        temp = open('temp.dat', 'wb')
        shid = int(input('enter hospital id: '))
        file.seek(0)
        while True:
            rec = pickle.load(file)
            current_pos = file.tell()
            if (rec.hid == shid):
                rec.add_rec()
                file.seek(current_pos + 1)
                pickle.dump(rec,temp)
                break
    except EOFError:
        file.close()
        temp.close()
    except IOError:
        print("File could not be opened")
       
    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")




def insertbeforerhid():
    try:
        file = open('hospital.dat', 'rb')
        temp = open('temp.dat', 'wb')
        shid = int(input('enter hospital id: '))
        file.seek(0)
        while True:
            rec = pickle.load(file)
            current_pos = file.tell()
            if (rec.hid == shid):
                rec.add_rec()
                file.seek(current_pos - 1)
                pickle.dump(rec,temp)
                break
    except EOFError:
        file.close()
        temp.close()
    except IOError:
        print("File could not be opened")
       
    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")




# DELETE CATEGORY
def delete_hid():
    z = 0
    try:
        n = int(input("Enter hospital no to delete: "))
        file = open("hospital.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.hid == n):
                z = 1
                print("record to delete found and details are")
                rec.disp_rec()
            else:
                pickle.dump(rec, temp)


    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")
    except IOError:
        print("File could not be opened")


    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")


def delete_hname():
    z = 0
    try:
        n = int(input("Enter hospital name to delete: "))
        file = open("hospital.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.hname == n):
                z = 1
                print("record to delete found and details are")
                rec.disp_rec()
            else:
                pickle.dump(rec, temp)


    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")
    except IOError:
        print("File could not be opened")


    os.remove("hospital.dat")
    os.rename("temp.dat", "hospital.dat")
    input("Press any key to cont ....")


while True:
    print(40 * "=")
    print("""            Main Menu
            ---------


           1. Add record.
           2. Display all records.
           3. Search record.
           4. Count records.
           5. Edit record.
           6. Insert record.
           7. Delete record.
           8. Exit.
    """)
    print(40 * "=")
    ch = int(input("Enter your choice: "))
    print(40 * "=")
    if (ch == 1):
        write_record()
    elif (ch == 2):
        display_all()
    elif (ch == 3):
        print("""Search on the bases of:
        1. Hospital id
        2. Name
        3. City
        4. State
        5. Specialization
        6. Category
        7. Vaccination
        8. Area
        9. Exit
        """)
        n = int(input("Enter Search option: "))
        if (n == 1):
            search_hid()
        elif (n == 2):
            search_hname()
        elif (n == 3):
            search_city()
        elif (n == 4):
            search_state()
        elif (n == 5):
            search_specz()
        elif (n == 6):
            search_cat()
        elif (n == 7):
            search_vax()
        elif (n == 8):
            search_area()
        elif (n == 9):
            print("End.")
            break
        else:
            print("Invalid choice.")


    elif (ch == 4):
        print("""Count on the bases of:
        1. All records
        2. City
        3. State
        4. Specialization
        5. Category
        6. Vaccination
        7. Area
        8. Exit
        """)
        n = int(input("Enter Search option: "))
        if (n == 1):
            countall()
        elif (n == 2):
            countcity()
        elif (n == 3):
            countstate()
        elif (n == 4):
            countspz()
        elif (n == 5):
            countcat()
        elif (n == 6):
            countvax()
        elif (n == 7):
            countarea()
        elif (n == 8):
            print("End.")
            break
        else:
            print("Invalid choice.")


    elif (ch == 5):
        print("""Edit on the bases of:
        1. Hospital Number
        2. Hospital Name
        3. Exit
        """)
        n = int(input("Enter Search option: "))
        if (n == 1):
            modify_hid()
        elif (n == 2):
            modify_hname()
        elif (n == 3):
            print("End.")
            break
        else:
            print("Invalid choice.")


    elif (ch == 6):
        print("""Insert:
        1. After hospital number
        2. Before hospital number
        3. Exit
        """)
        n = int(input("Enter Search option: "))
        if (n == 1):
            insertafterhid()
        elif (n == 2):
            insertbeforerhid()
        elif (n == 3):
            print("End.")
            break
        else:
            print("Invalid choice.")


    elif (ch == 7):
        print("""Delete on basis of:
        1. Hospital number
        2. Hospital Name
        3. Exit
        """)
        n = int(input("Enter Search option: "))
        if (n == 1):
            delete_hid()
        elif (n == 2):
            delete_hname()
        elif (n == 3):
            print("End.")
            break
        else:
            print("Invalid choice.")


    elif (ch == 8):
        print("End")
        break
    else:
        print("Invalid choice.")
