from tkinter import*
root=Tk()
root.geometry("400x400")
button1=Button(text="BREAKFAST",width=20,height=5,bg="green",relief="solid").place(x=30,y=50)
button2=Button(text="LUNCH",width=20,height=5,bg="green").place(x=220,y=50)
button3=Button(text="SNACKS",width=20,height=5,bg="green").place(x=30,y=200)
button4=Button(text="DINNER",width=20,height=5,bg="green").place(x=220,y=200)
root.mainloop()