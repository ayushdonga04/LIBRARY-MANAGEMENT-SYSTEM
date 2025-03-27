import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import *
from tkinter import ttk
import datetime as dt
import time
#mysql database connectivity
con=mysql.connector.connect(host="localhost",user="root",password="ayush@2005",database="lbmsystem",auth_plugin="mysql_native_password")
cur=con.cursor()

#cur.close()
#con.close()

top=tk.Tk()
top.title("LBM")
top.geometry("800x800")

lblframe=tk.LabelFrame(top,width=1280,height=30,borderwidth=5)
l1=tk.Label(lblframe,text="                                                  Library Management System                                             ",bg="blue",fg="yellow",font=("Times new roman",30))
l1.pack()
lblframe.pack()
searchframe=tk.Frame(top,width=1280,height=60)
searchframe.pack(fill="both")

lbltime=tk.Label(searchframe,bg="white",font=(30))

def clock():
    global dt1
    dt1=dt.datetime.now().strftime("%I:%M %p")
    lbltime.config(text= dt1)
    top.after(1000,clock)  
clock()
lbltime.pack(side=tk.LEFT)

lbldate=tk.Label(searchframe,bg="white",width=14,font=(30))
global dt2
dt2=dt.datetime.now().strftime("%d-%m-%y  %a")
lbldate.config(text= dt2)
lbldate.pack(side=tk.LEFT)



dataframe=tk.LabelFrame(top,width=1282,height=220,bd=1,bg="skyblue")
dataframe.pack(fill="both")
#Member Details
fname=tk.StringVar()
uid=tk.StringVar()
address=tk.StringVar()
city=tk.StringVar()
state=tk.StringVar()
email=tk.StringVar()
dob=tk.StringVar()
pincode=tk.StringVar()
mnumber=tk.StringVar()


lbl1=tk.Label(dataframe, text="Name",font=("30"),bg="skyblue")
lbl1.grid(row=0,column=0)
entry01=tk.Entry(dataframe,textvariable=fname,font=("30"))
entry01.grid(row=0,column=1)

lbl2=tk.Label(dataframe, text="User Id",font=("30"),bg="skyblue")
lbl2.grid(row=1,column=0)
entry02=tk.Entry(dataframe,textvariable=uid,font=("30"))
entry02.grid(row=1,column=1)


lbl3=tk.Label(dataframe, text="Mobile Number",font=("30"),bg="skyblue")
lbl3.grid(row=2,column=0)
entry03=tk.Entry(dataframe,textvariable=mnumber,font=("30"))
entry03.grid(row=2,column=1)


lbl4=tk.Label(dataframe, text="Address",font=("30"),bg="skyblue")
lbl4.grid(row=3,column=0)
entry04=tk.Entry(dataframe,textvariable=address,font=("30"))
entry04.grid(row=3,column=1)

lbl5=tk.Label(dataframe,text="DOB",font=("30"),bg="skyblue")
lbl5.grid(row=4,column=0)
entry05=tk.Entry(dataframe,textvariable=dob,font=("30"))
entry05.grid(row=4,column=1)

lbl6=tk.Label(dataframe,text="Didtrict",font=("30"),bg="skyblue")
lbl6.grid(row=5,column=0)
entry06=tk.Entry(dataframe,textvariable=city,font=("30"))
entry06.grid(row=5,column=1)

lbl7=tk.Label(dataframe,text="Pin Code",font=("30"),bg="skyblue")
lbl7.grid(row=6,column=0)
entry07=tk.Entry(dataframe,textvariable=pincode,font=("30"))
entry07.grid(row=6,column=1)

lbl8=tk.Label(dataframe,text="State",font=("30"),bg="skyblue")
lbl8.grid(row=7,column=0)
entry08=tk.Entry(dataframe,textvariable=state,font=("30"))
entry08.grid(row=7,column=1)

lbl9=tk.Label(dataframe, text="E-mail",font=("30"),bg="skyblue")
lbl9.grid(row=8,column=0)
entry09=tk.Entry(dataframe,textvariable=email,font=("30"))
entry09.grid(row=8,column=1)

#Book Details
bktitle=tk.StringVar()
bkid=tk.StringVar()
usrid=tk.StringVar
bksection=tk.StringVar()
bkprice=tk.StringVar()
bkfield=tk.StringVar()
bkauthor=tk.StringVar()
dorb=tk.StringVar()
lrf=tk.StringVar()

lbl1=tk.Label(dataframe, text="Title",font=("40"),bg="skyblue")
lbl1.grid(row=0,column=2)
entry11=tk.Entry(dataframe,textvariable=bktitle,font=("30"))
entry11.grid(row=0,column=3)

lbl2=tk.Label(dataframe, text="Book Id",font=("40"),bg="skyblue")
lbl2.grid(row=1,column=2)
entry12=tk.Entry(dataframe,textvariable=bkid,font=("30"))
entry12.grid(row=1,column=3)


lbl3=tk.Label(dataframe, text="User Id",font=("30"),bg="skyblue")
lbl3.grid(row=2,column=2)
entry13=tk.Entry(dataframe,textvariable=usrid,font=("30"))
entry13.grid(row=2,column=3)


lbl4=tk.Label(dataframe, text="Section",font=("30"),bg="skyblue")
lbl4.grid(row=3,column=2)
entry14=tk.Entry(dataframe,textvariable=bksection,font=("30"))
entry14.grid(row=3,column=3)

lbl5=tk.Label(dataframe,text="Book Price",font=("30"),bg="skyblue")
lbl5.grid(row=4,column=2)
entry15=tk.Entry(dataframe,textvariable=bkprice,font=("30"))
entry15.grid(row=4,column=3)

lbl6=tk.Label(dataframe,text="Subject/Field",font=("30"),bg="skyblue")
lbl6.grid(row=5,column=2)
entry16=tk.Entry(dataframe,textvariable=bkfield,font=("30"))
entry16.grid(row=5,column=3)

lbl7=tk.Label(dataframe,text="author",font=("30"),bg="skyblue")
lbl7.grid(row=6,column=2)
entry17=tk.Entry(dataframe,textvariable=bkauthor,font=("30"))
entry17.grid(row=6,column=3)

lbl8=tk.Label(dataframe,text="Return Data Of Book",font=("30"),bg="skyblue")
lbl8.grid(row=7,column=2)
entry18=tk.Entry(dataframe,textvariable=dorb,font=("30"))
entry18.grid(row=7,column=3)

lbl9=tk.Label(dataframe, text="Late Return Fine",font=("30"),bg="skyblue")
lbl9.grid(row=8,column=2)
entry19=tk.Entry(dataframe,textvariable=lrf,font=("30"))
entry19.grid(row=8,column=3)


#Add Book into the Library
def abook():
    sql="insert into abook VALUES(%s,%s,%s,%s,%s,%s)"
    val=(int(bid.get()),btitle.get(),int(section.get()),int(bprice.get()),field.get(),author.get())
    cur.execute(sql,val)
    con.commit()
    messagebox.showinfo("book show","book Record is inserted")
    listbox.insert(tk.END,btitle.get())

#Delete Book from the Library
def dbook():
    i=s1.get()
    sql1="select btitle from abook WHERE bid="+i
    cur.execute(sql1)
    ans=cur.fetchone()
    print(ans)
    idx=listbox.get(0,tk.END).index(ans)
    listbox.delete(idx)
    sql="delete from abook WHERE bid="+i
    cur.execute(sql)
    con.commit()
    messagebox.showinfo("delete","book deleted sucessfully")
def ud():
    i=s2.get()
    sql="select fname from user WHERE uid="+i
    cur.execute(sql)
    ans=cur.fetchone()
    sql="delete from user WHERE fname=%s"
    val=(ans)
    cur.execute(sql,val)
    con.commit()
    messagebox.showinfo("delete","user deleted sucessfully")
def dbc():
    dw=tk.Toplevel(top)
    dw.geometry("400x400")
    dw.title("delete window")
    dw.config(bg="black")
    global s1
    s1=tk.StringVar()
    global s2
    s2=tk.StringVar()
    label=tk.Label(dw,text="DELETE DATA",bg="red",font=("Times new roman",30)).pack()
    wf=Frame(dw,width=600,height=300)

    lbl=tk.Label(wf,text="delete user data",font=("Times new roman",20)).pack(padx=150)
    e2=tk.Entry(wf,font="(30)",textvariable=s2).pack(padx=150)
    btn=tk.Button(wf,fg="blue",bg="red",command=ud,text="DELETE").pack(padx=150)

    lbl=tk.Label(wf,text="delete book in library",font=("Times new roman",20)).pack(padx=150)
    e1=tk.Entry(wf,font="(30)",textvariable=s1).pack(padx=150)
    btn=tk.Button(wf,fg="blue",bg="red",command=dbook,text="DELETE").pack(padx=150)
    wf.pack()
    
l1=tk.Label(dataframe,text="        Add Book        ",bg="blue",fg="yellow",font=(30))
l1.grid(row=0,column=5)

btitle=tk.StringVar()
bid=tk.StringVar()
bprice=tk.StringVar()
field=tk.StringVar()
section=tk.StringVar()
author=tk.StringVar()
bookid=tk.StringVar()

lbl1=tk.Label(dataframe, text="Book Title",font=("30"),bg="skyblue")
lbl1.grid(row=2,column=5)
entry1=tk.Entry(dataframe,textvariable=btitle,font=("30"))
entry1.grid(row=2,column=6)

lbl2=tk.Label(dataframe, text="Book Id",font=("30"),bg="skyblue")
lbl2.grid(row=3,column=5)
entry2=tk.Entry(dataframe,textvariable=bid,font=("30"))
entry2.grid(row=3,column=6)

lbl3=tk.Label(dataframe, text="Section",font=("30"),bg="skyblue")
lbl3.grid(row=4,column=5)
entry3=tk.Entry(dataframe,textvariable=section,font=("30"))
entry3.grid(row=4,column=6)

lbl4=tk.Label(dataframe, text="Book Price ",font=("30"),bg="skyblue")
lbl4.grid(row=5,column=5)
entry4=tk.Entry(dataframe,textvariable=bprice,font=("30"))
entry4.grid(row=5,column=6)

lbl5=tk.Label(dataframe, text="Subject/Field",font=("30"),bg="skyblue")
lbl5.grid(row=6,column=5)
entry5=tk.Entry(dataframe,textvariable=field,font=("30"))
entry5.grid(row=6,column=6)

lbl6=tk.Label(dataframe, text="author",font=("30"),bg="skyblue")
lbl6.grid(row=7,column=5)
entry6=tk.Entry(dataframe,textvariable=author,font=("30"))
entry6.grid(row=7,column=6)
btn1=tk.Button(dataframe, text="ADD BOOK",command=abook,width=25,bg="blue")
btn1.grid(row=8,column=5)


#add data into the databas
def adddata():
    nm=bktitle.get()
    bookid=int(bkid.get())
    userid=uid.get()
    sect=bksection.get()
    bpri=int(bkprice.get())
    fi=bkfield.get()
    auth=bkauthor.get()
    rdate=dorb.get()
    lrfine=int(lrf.get())
    sql="insert into user (uid,fname,mnumber,address,dob,city,pincode,state,email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(uid.get(),fname.get(),mnumber.get(),address.get(),dob.get(),city.get(),int(pincode.get()),state.get(),email.get())
    cur.execute(sql,val)
    sql="insert into ibook (bid,bname,uid,section,bprice,field,author,dorb,lrf,breturn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(bookid,nm,userid,sect,bpri,fi,auth,rdate,lrfine,"no")
    cur.execute(sql,val)
    con.commit()
    messagebox.showinfo("show","Record is inserted")
#delete all data from database
def resetedata():
            entry01.delete(0, 'end')
            entry02.delete(0, 'end')
            entry03.delete(0, 'end')
            entry04.delete(0, 'end')
            entry05.delete(0, 'end')
            entry06.delete(0, 'end')
            entry07.delete(0, 'end')
            entry08.delete(0, 'end')
            entry09.delete(0, 'end')
            entry11.delete(0, 'end')
            entry12.delete(0, 'end')
            entry13.delete(0, 'end')
            entry14.delete(0, 'end')
            entry15.delete(0, 'end')
            entry16.delete(0, 'end')
            entry17.delete(0, 'end')
            entry18.delete(0, 'end')
            entry19.delete(0, 'end')


def newwindow():
    global s1
    s1=tk.StringVar()
    global s2
    s2=tk.StringVar()
    global s3
    s3=tk.StringVar()
    nw=tk.Toplevel(top)
    nw.title("new window")
    nw.geometry("400x400")
    nw.configure(bg="blue")
    label=tk.Label(nw,text="SHOW DATA",bg="red",font=("Times new roman",30)).pack()
    wf=Frame(nw)
    lbl=tk.Label(wf,text="show user data",font=("Times new roman",20)).pack(padx=150)
    e1=tk.Entry(wf,font="(30)",textvariable=s1).pack(padx=150)
    userid=s1.get()
    btn=tk.Button(wf,fg="blue",bg="red",command=showuser,text="SHOW").pack(padx=150)   
    

    lbl=tk.Label(wf,text="show both data",font=("Times new roman",20)).pack(padx=50,pady=(20,0))
    e1=tk.Entry(wf,font="(30)",textvariable=s3).pack(padx=150)
    btn=tk.Button(wf,fg="blue",bg="red",text="SHOW",command=showboth).pack(padx=150)

    lbl=tk.Label(wf,text="show no return book data",font=("Times new roman",20)).pack(padx=50,pady=(20,0))
    btn=tk.Button(wf,fg="blue",bg="red",text="SHOW",command=shownoreturn).pack(padx=150)
    wf.pack(padx=10,pady=30)

    dsf=tk.LabelFrame(nw,width="1282",height="220",bd=10)
    dsf.pack(fill="both",expand="yes")
    
    xsbotv=ttk.Scrollbar(dsf,orient="horizontal")
    ysbotv=ttk.Scrollbar(dsf,orient="vertical")
    global tv1
    tv1=ttk.Treeview(dsf,column=("name","uid","phno.","address","dob","district","pincode","state","email","bname","bid","uid","section","price"
                                      ,"field","author","return book date","late return fine","book return"),xscrollcommand = xsbotv.set,yscrollcommand = ysbotv.set)
    tv1.pack()
    tv1["show"]="headings"
    tv1.heading('#1',text="uname")
    tv1.heading('#2',text="user id")
    tv1.heading('#3',text="phone no.")
    tv1.heading('#4',text="address")
    tv1.heading('#5',text="dob")
    tv1.heading('#6',text="district")
    tv1.heading('#7',text="pincode")
    tv1.heading('#8',text="state")
    tv1.heading('#9',text="email")
    tv1.heading('#10',text="book name")
    tv1.heading('#11',text="book id")
    tv1.heading('#12',text="user id")
    tv1.heading('#13',text="section")
    tv1.heading('#14',text="book price")
    tv1.heading('#15',text="book author")
    tv1.heading('#16',text="field")
    tv1.heading('#17',text="return date of book") 
    tv1.heading('#18',text="late return fine")
    tv1.heading('#19',text="book return")

    tv1.column('#2',width=80)
    #tv1.column('#2',width=500)
    tv1.column('#6',width=80)
    tv1.column('#11',width=100)
    tv1.column('#12',width=100)
    tv1.column('#13',width=100)
    tv1.column('#14',width=100)
    tv1.column('#15',width=200)
    tv1.column('#16',width=200)
    tv1.column('#18',width=80)
    tv1.column('#17',width=200)
    tv1.column('#19',width=80)

    xsbotv.pack(fill = tk.X,expand="yes",side="bottom")
    xsbotv.config( command = tv1.xview )
    ysbotv.pack(side=tk.RIGHT,fill = tk.Y)
    #ysbotv.config(command = tv1.yview )

#new window order command functions
def shownoreturn():
    s1="select * from user INNER JOIN ibook ON user.uid=ibook.uid WHERE breturn='no'"
    cur.execute(s1)
    ans=cur.fetchall()
    ll=0 
    for e in ans:
        tv1.insert("",ll,value=e)
        ll=ll+1
    con.commit()
    if not ans:
        messagebox.showinfo("msg","all books are returned")
  
def showuser():
    userid=s1.get()
    sql1="select * from user WHERE uid="+userid 
    cur.execute(sql1)
    ans=cur.fetchall()
    for i in ans:
        tv1.insert("",tk.END,value=i)
    con.commit()
def showboth():
    usid=s3.get()
    sql1="select * from user INNER JOIN ibook ON user.uid=ibook.uid WHERE user.uid="+usid
    cur.execute(sql1)
    ans=cur.fetchall()
    j=0
    for i in ans:
        tv1.insert("",j,value=i)
        j=j+1
    con.commit()
def rbc():
    book=uuid.get()
    sql2="UPDATE ibook SET breturn='yes' WHERE uid="+book
    cur.execute(sql2)
    con.commit()
    book=uuid.get()
    sqld="DELETE FROM user WHERE uid="+book
    cur.execute(sqld)
    con.commit()
    messagebox.showinfo("br","Book is Returned")
def rw():
    global uuid
    uuid=tk.StringVar()
    rw=tk.Toplevel(top)
    rw.geometry("400x400")
    rw.configure(bg="black")
    label=tk.Label(rw,text="RETURN BOOK",bg="red",font=("Times new roman",30)).pack()

    wf=Frame(rw,width=600,height=300)
    lbl=tk.Label(wf,text="enter userid",font=("Times new roman",20)).pack(padx=150)
    e1=tk.Entry(wf,font="(30)",textvariable=uuid).pack(padx=150)
    btn=tk.Button(wf,fg="blue",bg="red",command=rbc,text="RETURN").pack(padx=150)
      
    wf.pack(padx=10,pady=30)
    
#btnframe   
btnframe =tk.LabelFrame(top,width="1200",height="300",bd=5)
btnframe.pack(fill="both",expand="yes")
btn1=tk.Button(btnframe, text="ADD DATA",bg="blue",command=adddata,width=23,font=("20"),fg="red")
btn1.pack(side=tk.LEFT)
btn2=tk.Button(btnframe, text="SHOW DATA",bg="blue",command=newwindow,width=23,font=("20"),fg="red")
btn2.pack(side=tk.LEFT)
btn3=tk.Button(btnframe, text="RESETE DATA",bg="blue",command=resetedata,width=23,font=("20"),fg="red")
btn3.pack(side=tk.RIGHT)
btn4=tk.Button(btnframe, text="BOOK RETURN",bg="blue",command=rw,width=23,font=("20"),fg="red")
btn4.pack(side=tk.RIGHT)
btn5=tk.Button(btnframe, text="DELETE DATA",bg="blue",command=dbc,width=25,font=("20"),fg="red")
btn5.pack(side=tk.RIGHT)

def listevent(a):

    op=1
    a=listbox.get(listbox.curselection())
    sql3="select * from abook WHERE btitle=%s"
    cpt=0
    cur.execute(sql3,(a))
    ans=cur.fetchall()
    for dt in ans:
        op=0
    tv.insert("",tk.END,values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
    con.commit()

#dataframe
datashowframe =tk.LabelFrame(top,width="1282",height="220",bd=10)
datashowframe.pack(fill="both",expand="yes")

sb = tk.Scrollbar(datashowframe)  
listbox = tk.Listbox(datashowframe, height=15,width=25,yscrollcommand = sb.set)  

sql1="select btitle from abook"
cur.execute(sql1)
allans=cur.fetchall()
for data in allans:
    listbox.insert(tk.END,data)


listbox.pack( side = tk.LEFT )
listbox.bind('<<ListboxSelect>>',listevent)
sb.pack(side = tk.LEFT, fill = tk.Y) 
sb.config( command = listbox.yview )


bookname=tk.StringVar()
def entry_event(event):
    if entry.get()=="book id":
        entry.delete(0, 'end')

def search_text(event):
    s=1
    sql="select btitle from abook"
    cur.execute(sql)
    ns=cur.fetchall()
    aobk=[item for tup in ns for item in tup]
    bt=bookname.get()
    for i in aobk:
        if bt==i:
            s=0
    if s==0:
        messagebox.showinfo("book","book is avilable in library")
    else:
        messagebox.showinfo("book","book is not avilable in library")


label=tk.Label(searchframe,text="search book",font="18")
entry=tk.Entry(searchframe,font="18",textvariable=bookname)
entry.insert(0, "book id")
entry.pack(side=tk.RIGHT)
entry.bind("<FocusIn>",entry_event)
entry.bind("<Return>",search_text)
label.pack(side="right")



sb1=tk.Scrollbar(datashowframe,orient="vertical")
tv=ttk.Treeview(datashowframe,column=("bname","bid","section","price","field","author"),yscrollcommand = sb1.set)
tv.pack()

sb1.pack(side=tk.RIGHT,fill = tk.Y,expand="yes")
sb1.config(command = tv.yview )

tv.heading("#1",text="book name",anchor='center')
tv.heading("#2",text="book id")
tv.heading("#3",text="section")
tv.heading("#4",text="book price")
tv.heading("#5",text="field")
tv.heading("#6",text="author",anchor='center')


tv['show'] = 'headings'

tv.column("#2",width=160)

tv.column("#3",width=160)

top.mainloop()
