import tkinter
import datetime

screen = tkinter.Tk()
screen.title("VACCINATION")
screen.geometry("500x300")
screen.configure(bg="sky blue")

first_box = tkinter.StringVar()
last_box = tkinter.StringVar()
email_box = tkinter.StringVar()
number_box = tkinter.StringVar()
v_status_box = tkinter.StringVar()


def submit():

    d = datetime.datetime.now()
    cur_date=str(d)
    cur_date=d.date()
    file_name=str(cur_date)+".txt"
    file=open(file_name,"a")


    fname = first_box.get()
    lname = last_box.get()
    Email = email_box.get()
    m_number = number_box.get()
    v_doze = v_status_box.get()
    
    first_box.set("")
    last_box.set("")
    email_box.set("")
    number_box.set("")
    v_status_box.set("")

    print("Data Successfully Submit")
    file.write("===================================\n")
    file.write("First Name: "+ fname)
    file.write("\n")
    file.write("Last Name: " + lname)
    file.write("\n")
    file.write("Mail Adress: " + Email)
    file.write("\n")
    file.write("Contact Number: " + str(m_number))
    file.write("\n")
    file.write("Vaccination Doze: " + v_doze)
    file.write("\n")

    file.close()
