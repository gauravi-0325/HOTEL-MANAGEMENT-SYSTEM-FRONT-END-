from tkinter import *
from tkinter import ttk
import random

from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+250+220")

#title
        lbl_title =Label(self.root,text="ROOM BOOKING  DETAILS",font=("FORTE", 30, "bold"), bg="BLACK",fg="white")
        lbl_title.place (x=0,y=0,width =1190,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking details",padx=2,font=("Times New Roman", 15, "bold"))
        labelframeleft.place(x=5,y=45,width=475,height=590)
#customer contact
        
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("Times New Roman", 15, "bold"),padx=2,pady=6)      
        lbl_cust_contact.grid(row=0,column=1)

        entry_contact=ttk.Entry(labelframeleft, width=22,font=("Times New Roman", 15, "bold"))
        entry_contact.grid(row=0,column=1,sticky=W) 

        #Fetch data Button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="FetchData",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=330,y=3)


        #checkin date
        check_in_date=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Check in date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)  
        txt_check_in_date=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txt_check_in_date.grid(row=1,column=1)

        #checkout date

        lbl_check_out=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Check out date:",padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W) 
        txt_check_out=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txt_check_out.grid(row=2,column=1)

        # room type
        label_Roomtype=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Room type:",padx=2,pady=6)
        label_Roomtype.grid(row=3,column=0,sticky=W) 

        combo_Roomtype=ttk.Combobox(labelframeleft,font=("Times New Roman", 15, "bold"),width=27,state="readonly")
        combo_Roomtype["value"]=("Single","Double","Luxury")
        combo_Roomtype.current(0)
        combo_Roomtype.grid(row=3,column=1)

        #available room
        lblRoomavailable=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Available Room",padx=2,pady=6)
        lblRoomavailable.grid(row=4,column=0,sticky=W) 
        txtRoomavailable=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtRoomavailable.grid(row=4,column=1)

        #meal

        lblMeal=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="MEAL:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W) 
        txtMeal=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtMeal.grid(row=5,column=1)
        # no of days

        lblNoofdays=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="No Of Days:",padx=2,pady=6)
        lblNoofdays.grid(row=6,column=0,sticky=W) 
        txtNoofdays=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtNoofdays.grid(row=6,column=1)

        #pay tax
        lblPaidtax=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Paid tax:",padx=2,pady=6)
        lblPaidtax.grid(row=7,column=0,sticky=W) 
        txtPaidtax=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtPaidtax.grid(row=7,column=1)
        #sub total
        lblSubtotal=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Sub total:",padx=2,pady=6)
        lblSubtotal.grid(row=8,column=0,sticky=W) 
        txtSubtotal=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtSubtotal.grid(row=8,column=1)

#total cost
        lblTotalcost=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Total Cost:",padx=2,pady=6)
        lblTotalcost.grid(row=9,column=0,sticky=W) 
        txtTotalcost=ttk.Entry(labelframeleft,font=("Times New Roman", 15, "bold"),width=29 )
        txtTotalcost.grid(row=9,column=1)
        #bill button

        btnBill=Button(labelframeleft,text="Bill",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        






#button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=430,width=450,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #TABEL FRAME
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("Times New Roman", 15, "bold"))
        Table_frame.place(x=435,y=280,width=860,height=260)
        
        lblSearchBy=Label(Table_frame,text="Search By :",font=("Times New Roman", 15, "bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.Search_var=StringVar

        combo_Search=ttk.Combobox(Table_frame,textvariable=self.Search_var,font=("Times New Roman", 15, "bold"),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("Times New Roman", 15, "bold"),width=18)
        txtSearch.grid(row=0,column=2,padx=3)
        
        btnSearch=Button(Table_frame,text="Search",font=("Times New Roman", 11, "bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="ShowAll",font=("Times New Roman", 11, "bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #show data table
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="Contact")
        self.room_Table.heading("checkin",text="Check-in")
        self.room_Table.heading("checkout",text="Check-out")
        self.room_Table.heading("roomtype",text="Roomtype")
        self.room_Table.heading("roomavailable",text="Room No")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfdays",text="NoOfDays")
       

        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin",width=100)
        self.room_Table.column("checkout",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("roomavailable",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfdays",width=100)
        self.room_Table.pack(fill=BOTH,expand=1)

    def Fetch_contact(self):
      if self.var_contact.get()=="":
         messagebox.showerror("Error","please enter contact number",parent=self.root)


        
        



        




if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()