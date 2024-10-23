from tkinter import*
import MySQLdb as mysql
root=Tk()
root.geometry("400x400")
root.configure(bg="#353333")
def connec():
    mydb=mysql.connect(host="localhost",user="root",password="rpj15310102",database="hotel")
    cursor = mydb.cursor()
def type1():
    f = Frame(root, bg="#333333")
    f.place(x=0, y=0, width=400, height=200)
    label1 = Label(f, text="NAME:", font=('Arial', 18, 'bold')).pack(anchor="w", side=LEFT, padx=30, expand=YES)
    text1 = Text(f, width=200, height=2, relief="groove").pack(anchor="w", side=LEFT, padx=5, expand=YES)
    ff = Frame(root, bg="#333333")
    ff.place(x=0, y=200, width=400, height=100)
    label2 = Label(ff, text="TABLE:", font=('Arial', 18, 'bold')).pack(anchor="n", side=LEFT, padx=30, expand=YES)
    text2 = Text(ff, width=20, height=1.5, relief="solid").pack(anchor="n", side=LEFT, padx=5, expand=YES)
    fff = Frame(root, bg="#333333")
    fff.place(x=0, y=300, width=400, height=100)

    button2 = Button(fff, text="QUIT", relief="raised", command=root.quit).pack(side=RIGHT, padx=20, ipadx=20,
                                                                                expand=YES)
    button1 = Button(fff, text="SUBMIT", relief="raised", command=type2).pack(side=RIGHT, padx=10, ipadx=20, expand=YES)
def type2():
    root.configure(bg="#353333")
    f1=Frame(root,bg="#333333")
    f1.place(x=0, y=0, width=400, height=400)
    button3 = Button(text="INDIAN", width=20, height=5, bg="gold",command=type3).place(x=30, y=50)
    button4 = Button(text="MEXICAN", width=20, height=5, bg="slateblue3").place(x=220, y=50)
    button5 = Button(text="CHINESE", width=20, height=5, bg="orange").place(x=30, y=200)
    button6 = Button(text="ITALIAN", width=20, height=5, bg="green").place(x=220, y=200)
    button11 = Button(text="QUIT", relief="raised", command=root.quit).place(x=150,y=350)
    button12 = Button(text="SUBMIT", relief="raised", command=type1).place(x=220,y=350)
def type3():
        f3 = Frame(root,bg="#333333")
        f3.place(x=0, y=0, width=400, height=400)
        button7 = Button(text="BREAKFAST", width=20, height=5, bg="yellow", relief="solid",command=type5).pack(side=LEFT,expand=YES)
        button8 = Button(text="LUNCH", width=20, height=5, bg="yellow").pack(side=LEFT,expand=YES)
        button9 = Button(text="SNACKS", width=20, height=5, bg="yellow").pack(side=LEFT,expand=YES)
        button10 = Button(text="DINNER", width=20, height=5, bg="yellow").pack(side=LEFT,expand=YES)
        button11=Button(text="BACK", width=10, height=2, bg="WHITE",command=type2).pack(side=RIGHT,anchor=S,expand=YES)
def type5():

    f4 = Frame(root, bg="#333333")
    f4.place(x=0, y=0, width=400, height=400)

f = Frame(root,bg="#333333",relief=SUNKEN)
f.place(x=0, y=0, width=400, height=200)
labFrame = LabelFrame(f, text="Personal info")
label1=Label(f,text="NAME:",font=('Arial', 18, 'bold')).pack(anchor="w",side=LEFT,padx=30,expand=YES)
text1=Text(f,width=200,height=2,relief="groove").pack(anchor="w",side=LEFT,padx=5,expand=YES)
labFrame.pack()
ff = Frame(root,bg="#333333")
ff.place(x=0, y=200, width=400, height=100)
label2=Label(ff,text="TABLE:",font=('Arial', 18, 'bold')).pack(anchor="n",side=LEFT,padx=30,expand=YES)
text2=Text(ff,width=20,height=1.5,relief="solid").pack(anchor="n",side=LEFT,padx=5,expand=YES)
fff = Frame(root,bg="#333333")
fff.place(x=0, y=300, width=400, height=100)

button2=Button(fff,text="QUIT",relief="raised",command=root.quit).pack(side=RIGHT,padx=20,ipadx=20,expand=YES)
button1=Button(fff,text="SUBMIT",relief="raised",command=type2).pack(side=RIGHT,padx=10,ipadx=20,expand=YES)
root.mainloop()
