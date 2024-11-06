from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random

from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+250+220")


#titlw
        lbl_title =Label(self.root,text="ROOM BOOKING  DETAILS",font=("FORTE", 30, "bold"), bg="BLACK",fg="white")
        lbl_title.place (x=0,y=0,width =1590,height=40)

        
        img2=Image.open(r"C:\Users\user\Desktop\New folder (2)\francesca-tosolini-hCU4fimRW-c-unsplash.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=150,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("Times New Roman", 15, "bold"))
        labelframeleft.place(x=5,y=50,width=525,height=450)
        #floor

        lbl_floor=Label(labelframeleft,text="Floor",font=("Times New Roman", 15, "bold"),padx=2,pady=6)      
        lbl_floor.grid(row=0,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft, width=22,font=("Times New Roman", 15, "bold"))
        entry_floor.grid(row=0,column=1,sticky=W) 
#room no

        lbl_floor=Label(labelframeleft,text="Room No.",font=("Times New Roman", 15, "bold"),padx=2,pady=6)      
        lbl_floor.grid(row=1,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft, width=22,font=("Times New Roman", 15, "bold"))
        entry_floor.grid(row=1,column=1,sticky=W) 
#room type
        lbl_floor=Label(labelframeleft,text="Room Type",font=("Times New Roman", 15, "bold"),padx=2,pady=6)      
        lbl_floor.grid(row=2,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft, width=22,font=("Times New Roman", 15, "bold"))
        entry_floor.grid(row=2,column=1,sticky=W) 

#button
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=450,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)
#table
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("Times New Roman", 15, "bold"))
        Table_frame.place(x=600,y=55,width=600,height=350)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.room_Table=ttk.Treeview(Table_frame,column=("floor","room no.","room type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("floor",text="Floor")
        self.room_Table.heading("room no.",text="Room No.")
        self.room_Table.heading("room type",text="Room Type")
        
       

        self.room_Table["show"]="headings"

        self.room_Table.column("floor",width=100)
        self.room_Table.column("room no.",width=100)
        self.room_Table.column("room type",width=100)
        
        self.room_Table.pack(fill=BOTH,expand=1)
        














if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()