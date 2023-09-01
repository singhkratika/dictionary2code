# Code for Dictionary App
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('1000x626')
root.resizable(0,0)
root.title('Dictionary Application')

lstword=['Parrot','Patriot','Apple','Banana','Computer','RAM']
lstmeaning=['Tota','Deshbhakt','A Fruit','A Fruit','A Device','Random Access Memory']

def search():
 w=word.get()
 try:
  i=lstword.index(w)
  textarea.insert(END,lstmeaning[i])
  textarea.config(state=DISABLED)
 except:
  messagebox.showerror('Error', 'Word does not exist')
  entword.delete(0,END)
  textarea.delete(1.0,END)

def clear():
 textarea.config(state=NORMAL)
 entword.delete(0,END)
 textarea.delete(1.0,END)

def iexit():
 res=messagebox.askyesno('Confirm','Do you want to exit?')
 if res==True:
  root.destroy()
 else:
  pass

bgimage=PhotoImage('dic.jpg')
bgimage=Image.resize((300,400),Image.LANCZOS)
lblbg=Label(root,image=bgimage)
lblbg.place(x=0,y=0)

lblword=Label(root,text='Enter Word',font=('castellar',29,'bold'),fg='red3',bg='whitesmoke')
lblword.place(x=530,y=20)

word=StringVar()
entword=Entry(root,font=('Arial',23,'bold'),bd=8,relief=GROOVE,justify=CENTER,textvariable=word)
entword.place(x=510,y=80)

btnsearch=Button(root,text='Search',font=('Arial',18,'bold'),bd=5,relief=GROOVE,command=search)
btnsearch.place(x=630,y=150)

lblmeaning=Label(root,text='Meaning',font=('castellar',29,'bold'),fg='red3',bg='whitesmoke')
lblmeaning.place(x=580,y=240)

textarea=Text(root,font=('Arial',18,'bold'),height=8,width=34,bd=5,relief=GROOVE)
textarea.place(x=480,y=300)

clearimage=PhotoImage(file='clear.png')
btnclear=Button(root,image=clearimage,bd=0,bg='whitesmoke',command=clear)
btnclear.place(x=660,y=555)

exitimage=PhotoImage(file='exit.png')
btnexit=Button(root,image=exitimage,bd=0,bg='whitesmoke',command=iexit)
btnexit.place(x=790,y=555)


root.mainloop()