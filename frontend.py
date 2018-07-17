from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Book Directory")
root.geometry("470x220")

#defining fuctions for buttons

import backend

def view_all():
    data=backend.view_books()
    booklist.delete(0,END)
    if data:
      for row in data:
         booklist.insert(END,row)
    else:
      messagebox.showinfo("Error","Empty Book Directory.")
 
def search_entry():
    data=backend.search_books(t.get(),a.get(),y.get(),i.get())
    booklist.delete(0,END)
    if data:
      for row in data:
         booklist.insert(END,row)
    else:
      messagebox.showinfo("Message","No Match Found.")

def add_entry():
    if (t.get() is not ''):
         backend.add_book(t.get(),a.get(),y.get(),i.get())
         view_all()
    else:
         messagebox.showinfo("Error","Title of Book required.")

def update_selected():
    backend.update_book(selected_book[0],t.get(),a.get(),y.get(),i.get())
    messagebox.showinfo("Success","Book Updated.")
    view_all()

def delete_selected():
    backend.delete_book(selected_book[0])
    titleE.delete(0, END)
    authorE.delete(0, END)
    yearE.delete(0, END)
    isbnE.delete(0, END)
    messagebox.showinfo("Success","Book Deleted.")
    view_all()

#fuction for fetching values of selected list item
def selected_list_item(event):
    global selected_book
    selected_book=booklist.get(booklist.curselection()[0])
    #adding values of selected option into the entry boxes
    titleE.delete(0, END)
    titleE.insert(END, selected_book[1])

    authorE.delete(0, END)
    authorE.insert(END, selected_book[2])

    yearE.delete(0, END)
    yearE.insert(END, selected_book[3])

    isbnE.delete(0, END)
    isbnE.insert(END, selected_book[4])    
    

#frame 1 for label and entry
f1=Frame(root)
f1.pack(side=TOP,fill=X)

#defining textvariales for entries
t=StringVar()#for title
a=StringVar()#for author_name
y=StringVar()#for year
i=StringVar()#for isbn

titleL=Label(f1,text="Title")
titleL.grid(row=0,column=0)
titleE=Entry(f1,textvariable=t)
titleE.grid(row=0,column=1)


authorL=Label(f1,text="Author")
authorL.grid(row=0,column=3)
authorE=Entry(f1,textvariable=a)
authorE.grid(row=0,column=4)

yearL=Label(f1,text="Year")
yearL.grid(row=2,column=0)
yearE=Entry(f1,textvariable=y)
yearE.grid(row=2,column=1)

isbnL=Label(f1,text="ISNB")
isbnL.grid(row=2,column=3)
isbnE=Entry(f1,textvariable=i)
isbnE.grid(row=2,column=4)


#frame 2 for list and scroll bar
f3=Frame(root)
f3.pack(fill=Y,side=LEFT)

scrollbar=Scrollbar(f3)
scrollbar.pack(side=RIGHT,padx=12,fill=Y,expand=TRUE)

booklist=Listbox(f3,width=40,height=10,selectmode=EXTENDED,yscrollcommand=scrollbar.set)
booklist.pack(fill=X)

booklist.bind('<<ListboxSelect>>', selected_list_item)

scrollbar.configure(relief=GROOVE,command=booklist.yview)


#frame 3 for buttons
f3=Frame(root)
f3.pack(fill=Y, side=RIGHT)

viewB=Button(f3,text='View All',activebackground='green' , activeforeground='white', command=view_all)
viewB.pack(fill=X)

searchB=Button(f3,text='Search Entry',activebackground='green' , activeforeground='white', command=search_entry)
searchB.pack(fill=X)

addB=Button(f3,text='Add Entry',activebackground='green' , activeforeground='white', command=add_entry)
addB.pack(fill=X)

updateB=Button(f3,text='Update Selected',activebackground='green' , activeforeground='white',command=update_selected)
updateB.pack(fill=X)

deleteB=Button(f3,text='Delete Selected',activebackground='green' , activeforeground='white', command=delete_selected)
deleteB.pack(fill=X)

closeB=Button(f3,text='Close',activebackground='green' , activeforeground='white',command=root.destroy)
closeB.pack(fill=X)

root.mainloop()



#command=lambda :backend.add_entry(t.get(),a.get(),i.get(),y.get())
