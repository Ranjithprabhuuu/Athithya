from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.checkbox import CheckBox
import random
import sqlite3
import mysql.connector
import datetime
Window.clearcolor=(1/255.0,70/255.0,70/255.0,1)
Window.size=(360,600)
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    def counter(self):
        SecondWindow.counter_no=self.ids.counter_no.text
        SecondWindow.waiter_name=self.ids.waiter_name.text
class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    checks = []
    quantity = []
    prices = []
    q = []



    def checkbox_checka(self,instance,value,item,price):


        if value==True:
            FourthWindow.checks.append(item)
            FourthWindow.prices.append(price)
        else:
            FourthWindow.checks.remove(item)
            FourthWindow.prices.remove(price)

    def texta(self):
        t2 = self.ids.textbox1_text.text
        FourthWindow.q.append(t2)
    def textb(self):
        t3=self.ids.textbox2_text.text
        FourthWindow.q.append(t3)
    def textc(self):
        t4=self.ids.textbox3.text
        FourthWindow.q.append(t4)
    def textd(self):
        t5 = self.ids.textbox4.text
        FourthWindow.q.append(t5)

    def place_order(self):
        print(FourthWindow.q)


        quantity=",".join(FourthWindow.q)
        checkss=",".join(FourthWindow.checks)
        string1=",".join(FourthWindow.prices)
        counter=SecondWindow.counter_no
        w_name=SecondWindow.waiter_name
        print(checkss)
        now=datetime.datetime.now()
        now1=now.strftime("%Y-%m-%d %H:%M:%S")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9686715002",
            database="athithya")
        cur=mydb.cursor()
        s="create table if not exists orderss(order_id int(10) PRIMARY KEY auto_increment,Dete varchar(500),waiter_name varchar(30),counter_no int(10),item varchar(150),price varchar(50),quantity varchar(50))"
        cur.execute(s)
        cur.execute("insert into orderss(Dete,waiter_name,counter_no,item,price,quantity)values('{}','{}',{},'{}','{}','{}')".format(now1,w_name,counter,checkss,string1,quantity))
        mydb.commit()
        print("ORDER PLACED")
        mydb.close()


class FifthWindow(Screen):
    checks = []
    quantity = []
    prices = []
    q = []

    def checkbox_checka(self, instance, value, item, price):

        if value == True:
            FifthWindow.checks.append(item)
            FifthWindow.prices.append(price)
        else:
            FifthWindow.checks.remove(item)
            FifthWindow.prices.remove(price)

    def texta(self):
        t2 = self.ids.textbox1_text.text
        FifthWindow.q.append(t2)

    def textb(self):
        t3 = self.ids.textbox2_text.text
        FifthWindow.q.append(t3)

    def textc(self):
        t4 = self.ids.textbox3.text
        FifthWindow.q.append(t4)

    def textd(self):
        t5 = self.ids.textbox4.text
        FifthWindow.q.append(t5)

    def place_order(self):
        print(FifthWindow.q)

        quantity = ",".join(FifthWindow.q)
        checkss = ",".join(FifthWindow.checks)
        string1 = ",".join(FifthWindow.prices)
        counter = SecondWindow.counter_no
        w_name = SecondWindow.waiter_name
        print(checkss)
        now = datetime.datetime.now()
        now1 = now.strftime("%Y-%m-%d %H:%M:%S")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9686715002",
            database="athithya")
        cur = mydb.cursor()
        cur.execute(
            "insert into orderss(Dete,waiter_name,counter_no,item,price,quantity)values('{}','{}',{},'{}','{}','{}')".format(
                now1, w_name, counter, checkss, string1, quantity))
        mydb.commit()
        print("ORDER PLACED")
        mydb.close()


class SixthWindow(Screen):
    checks = []
    quantity = []
    prices = []
    q = []

    def checkbox_checka(self, instance, value, item, price):

        if value == True:
            SixthWindow.checks.append(item)
            SixthWindow.prices.append(price)
        else:
            SixthWindow.checks.remove(item)
            SixthWindow.prices.remove(price)

    def texta(self):
        t2 = self.ids.textbox1_text.text
        SixthWindow.q.append(t2)

    def textb(self):
        t3 = self.ids.textbox2_text.text
        SixthWindow.q.append(t3)

    def textc(self):
        t4 = self.ids.textbox3.text
        SixthWindow.q.append(t4)

    def textd(self):
        t5 = self.ids.textbox4.text
        SixthWindow.q.append(t5)

    def place_order(self):
        print(SixthWindow.q)

        quantity = ",".join(SixthWindow.q)
        checkss = ",".join(SixthWindow.checks)
        string1 = ",".join(SixthWindow.prices)
        counter = SecondWindow.counter_no
        w_name = SecondWindow.waiter_name
        print(checkss)
        now = datetime.datetime.now()
        now1 = now.strftime("%Y-%m-%d %H:%M:%S")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#",
            database="athithya")
        cur = mydb.cursor()
        cur.execute(
            "insert into orderss(Dete,waiter_name,counter_no,item,price,quantity)values('{}','{}',{},'{}','{}','{}')".format(
                now1, w_name, counter, checkss, string1, quantity))
        mydb.commit()
        print("ORDER PLACED")
        mydb.close()
class SeventhWindow(Screen):
    checks = []
    quantity = []
    prices = []
    q = []

    def checkbox_checka(self, instance, value, item, price):

        if value == True:
            FourthWindow.checks.append(item)
            FourthWindow.prices.append(price)
        else:
            FourthWindow.checks.remove(item)
            FourthWindow.prices.remove(price)

    def texta(self):
        t2 = self.ids.textbox1_text.text
        FourthWindow.q.append(t2)

    def textb(self):
        t3 = self.ids.textbox2_text.text
        FourthWindow.q.append(t3)

    def textc(self):
        t4 = self.ids.textbox3.text
        FourthWindow.q.append(t4)

    def textd(self):
        t5 = self.ids.textbox4.text
        FourthWindow.q.append(t5)

    def place_order(self):
        print(FourthWindow.q)

        quantity = ",".join(FourthWindow.q)
        checkss = ",".join(FourthWindow.checks)
        string1 = ",".join(FourthWindow.prices)
        counter = SecondWindow.counter_no
        w_name = SecondWindow.waiter_name
        print(checkss)
        now = datetime.datetime.now()
        now1 = now.strftime("%Y-%m-%d %H:%M:%S")
        con = sqlite3.connect('orde')
        cur = con.cursor()
        cur.execute(
            "create table if not exists orderss(order_id integer PRIMARY KEY autoincrement,Dete varchar(500),waiter_name varchar(30),counter_no integer,item varchar(150),price int,quantity int)")
        cur.execute(
            "insert into orderss(Dete,waiter_name,counter_no,item,price,quantity)values('{}','{}',{},'{}','{}','{}')".format(
                now1, w_name, counter, checkss, string1, quantity))
        con.commit()
        print("ORDER PLACED")
        con.close()
class EighthWindow(Screen,):
    def view_order(self):
        r=()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9686715002",
            database="athithya")
        cur = mydb.cursor()
        cur.execute("select * from orderss order by order_id desc limit 1")
        rec=cur.fetchall()
        for i in rec:
            r=i

        print("ORDER ok")
        print(r)
        s=str(i[0])
        S=str(i[1])
        W=str(i[2])
        ss=str(i[3])
        s5=i[4]
        s6=i[5]
        s7=i[6]
        self.ids.orderid_label.text=s
        self.ids.date_label.text=S
        self.ids.counterno_label.text = ss
        print(s5)
        print(s6)
        n=len(s5)
        if n<7:

            i=str(s5)
            self.ids.item1.text=i
            p=str(s6)
            self.ids.price1.text=p
            q=str(s7)
            self.ids.quantity1.text=q
        else:
            s1=s5.split(",")
            s2=s6.split(",")
            s3=s7.split(",")
            print(s1)
            l=len(s1)
            if l==1:
                c=str(s1[0])
                self.ids.item1.text = c
                d=str(s2[0])
                self.ids.price1.text=d
                e=str(s3[0])
                self.ids.quantity1.text=e
            elif l==2:
                c = str(s1[0])
                self.ids.item1.text = c
                d = str(s2[0])
                self.ids.price1.text = d
                e = str(s3[0])
                self.ids.quantity1.text = e
                c1=str(s1[1])
                self.ids.item2.text = c1
                d1 = str(s2[1])
                self.ids.price2.text = d1
                e1 = str(s3[1])
                self.ids.quantity2.text = e1
            elif l==3:
                c = str(s1[0])
                self.ids.item1.text = c
                d = str(s2[0])
                self.ids.price1.text = d
                e = str(s3[0])
                self.ids.quantity1.text = e
                c1 = str(s1[1])
                self.ids.item2.text = c1
                d1 = str(s2[1])
                self.ids.price2.text = d1
                e1= str(s3[1])
                self.ids.quantity2.text = e1
                c2=str(s1[2])
                self.ids.item3.text = c2
                d2 = str(s2[2])
                self.ids.price3.text = d2
                e2 = str(s3[2])
                self.ids.quantity3.text = e2
            else:
                c = str(s1[0])
                self.ids.item1.text = c
                d = str(s2[0])
                self.ids.price1.text = d
                e = str(s3[0])
                self.ids.quantity1.text = e
                c1 = str(s1[1])
                self.ids.item2.text = c1
                d1 = str(s2[1])
                self.ids.price2.text = d1
                e1 = str(s3[1])
                self.ids.quantity2.text = e1
                c2 = str(s1[2])
                self.ids.item3.text = c2
                d2 = str(s2[2])
                self.ids.price3.text = d2
                e2 = str(s3[2])
                self.ids.quantity3.text = e2
                c3=str(s1[3])
                self.ids.item4.text = c3
                d3 = str(s2[3])
                self.ids.price4.text = d3
                e3 = str(s3[3])
                self.ids.quantity4.text = e3





class NinthWindow(Screen):
    pass


class MainWindow(ScreenManager):
    pass
class MyApp(App):
    def build(self):
       pass


class MyInterface(Widget):
     pass
MyApp().run()