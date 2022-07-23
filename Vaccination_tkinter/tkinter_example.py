from tkinter_logic import*

lbl_title = tkinter.Label(screen,text="VACCINATION REPORT",font=("arial",14,"bold"),bg="sky blue",fg="green")
lbl_title.grid(row=0,column=5)

firstname = tkinter.Entry(screen,textvariable= first_box)
firstname.grid(row=100, column=14)

lastname = tkinter.Entry(screen,textvariable= last_box)
lastname.grid(row=180, column=14)

email = tkinter.Entry(screen,textvariable= email_box)
email.grid(row=260, column=14)

number = tkinter.Entry(screen,textvariable= number_box)
number.grid(row=330, column=14)

v_status = tkinter.Entry(screen,textvariable= v_status_box)
v_status.grid(row=410, column=14)


btn = tkinter.Button(screen,text="SUBMIT",bg="blue",fg="white",height=1,width=10,font=("arial", 12, "bold"),activebackground="pink",activeforeground="blue",command=submit)
btn.grid(row=480, column=5)

lbl = tkinter.Label(screen,text="FIRST NAME", font=("arial", 10, "bold"), bg="sky blue")
lbl.grid(row=100, column=0)

lbl1 = tkinter.Label(screen,text="LAST NAME", font=("arial", 10, "bold"), bg="sky blue")
lbl1.grid(row=180, column=0)

lbl2 = tkinter.Label(screen,text="EMAIL", font=("arial", 10, "bold"), bg="sky blue")
lbl2.grid(row=260, column=0)

lbl3 = tkinter.Label(screen,text="CONTACT NUMBER", font=("arial", 10, "bold"), bg="sky blue")
lbl3.grid(row=330, column=0)

lbl4 = tkinter.Label(screen,text="VACCINATION DOZE", font=("arial", 10, "bold"), bg="sky blue")
lbl4.grid(row=410, column=0)

screen.mainloop()