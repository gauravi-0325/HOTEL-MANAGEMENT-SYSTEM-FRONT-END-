from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
#import mysql.connector

from tkinter import messagebox
#from mysql.connector import connection


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+250+220")

        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_natonality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

       
#title
        
        lbl_title =Label(self.root,text="ADD CUSTOMER DETAILS",font=("FORTE", 30, "bold"), bg="BLACK",fg="white")
        lbl_title.place (x=0,y=0,width =1295,height=40)

        img2=Image.open(r"C:\Users\user\Desktop\New folder (2)\francesca-tosolini-hCU4fimRW-c-unsplash.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=150,height=40)


         #customer detail
         
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",padx=2,font=("Times New Roman", 15, "bold"))
        labelframeleft.place(x=5,y=45,width=475,height=590)

        #entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, width=22,state="readonly",font=("Times New Roman", 15, "bold"))
       # entry_ref.grid(row=0,column=1) 
        
# cust ref

        lbl_cust_ref=Label(labelframeleft,text="customer ref",font=("Times New Roman", 15, "bold"),padx=2,pady=6)      
        lbl_cust_ref.grid(row=0,column=1)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, width=22,state="readonly",font=("Times New Roman", 15, "bold"))
        entry_ref.grid(row=0,column=1) 
        



#customer name

        cname=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)  
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("Times New Roman", 15, "bold"),width=29 )
        txtcname.grid(row=1,column=1)

        # mother name

        lblmname=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)  
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("Times New Roman", 15, "bold"),width=29)
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W) 

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("Times New Roman", 15, "bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

#postcode

        lblPostCode=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Post Code:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)  
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("Times New Roman", 15, "bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #mobile number


        lblMobile=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)  
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("Times New Roman", 15, "bold"),width=29)
        txtMobile.grid(row=5,column=1)

# email


        lblEmail=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="EMAIL:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)  
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("Times New Roman", 15, "bold"),width=29)
        txtEmail.grid(row=6,column=1)

#NATION

        lblNationality=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W) 

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_natonality,font=("Times New Roman", 15, "bold"),width=27,state="readonly")
        combo_Nationality["value"]=("INDIAN","AMERICAN","ASIAN","OTHERS")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
        
        #id 
        lblIdproof=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)

        combo_Idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("Times New Roman", 15, "bold"),width=27,state="readonly")
        combo_Idproof["value"]=("Aadhar Card","Driving License","Pan Card","OTHERS")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=8,column=1)
        
#id number

        lblIdnumber=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Id Number:",padx=2,pady=6)
        lblIdnumber.grid(row=9,column=0,sticky=W)  
        txtIdnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("Times New Roman", 15, "bold"),width=29)
        txtIdnumber.grid(row=9,column=1)
        #addresss

        lblAddress=Label(labelframeleft,font=("Times New Roman", 15, "bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)  
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("Times New Roman", 15, "bold"),width=29)
        txtAddress.grid(row=10,column=1)

#button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=430,width=450,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("Times New Roman", 15, "bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        #label frame


        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("Times New Roman", 15, "bold"))
        Table_frame.place(x=435,y=50,width=860,height=690)
        
        lblSearchBy=Label(Table_frame,text="Search By :",font=("Times New Roman", 15, "bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.Search_var=StringVar

        combo_Search=ttk.Combobox(Table_frame,textvariable=self.Search_var,font=("Times New Roman", 15, "bold"),width=15,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=80,width=850,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_details_Table.xview)
        scroll_y.config(command=self.Cust_details_Table.yview)

        self.Cust_details_Table.heading("ref",text="Refer No")
        self.Cust_details_Table.heading("name",text="Name")
        self.Cust_details_Table.heading("mother",text="Mother Name")
        self.Cust_details_Table.heading("gender",text="Gender")
        self.Cust_details_Table.heading("post",text="Post Code")
        self.Cust_details_Table.heading("mobile",text="Mobile")
        self.Cust_details_Table.heading("email",text="Email")
        self.Cust_details_Table.heading("nationality",text="Nationality")
        self.Cust_details_Table.heading("idproof",text="Idproof")
        self.Cust_details_Table.heading("idnumber",text="Idnumber")
        self.Cust_details_Table.heading("address",text="Address")
        


        self.Cust_details_Table["show"]="headings"
        self.Cust_details_Table.column("ref",width=100)
        self.Cust_details_Table.column("name",width=100)
        self.Cust_details_Table.column("mother",width=100)
        self.Cust_details_Table.column("gender",width=100)
        self.Cust_details_Table.column("post",width=100)
        self.Cust_details_Table.column("mobile",width=100)
        self.Cust_details_Table.column("email",width=100) 
        self.Cust_details_Table.column("nationality",width=100)
        self.Cust_details_Table.column("idproof",width=100)
        self.Cust_details_Table.column("idnumber",width=100)
        self.Cust_details_Table.column("address",width=100)
        self.Cust_details_Table.pack(fill=BOTH,expand=1)
       # self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()

    def add_data(self):
     
        if self.var_mobile.get()==""or self.var_mother.get()=="":
                messagebox.showerror("error","all fields are required")
        else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="nitya@123",database="management")
                    
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into customer values(%s,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                 
                                                                    self.var_ref.get(),
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get()
                                                                                          ))

             
                    
                    conn.commit()
                    #self.fetch_data()
                    conn.close()
                    messagebox.showinfo("success","customer has been added",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)                     
'''   def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nitya@123",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
             for i in rows:
                  self.Cust_details_Table.insert("",END,values=i)
             conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
     cursor_row=self.Cust_details_Table.focus()
     content=self.Cust_details_Table.item(cursor_row)
     row=content["values"]

     self.var_ref.set(row[0]),
     self.var_cust_name.set(row[1]),
     self.var_mother.set(row[2]),
     self.var_gender.set(row[3]),
     self.var_post.set(row[4]),
     self.var_mobile.set(row[5]),
     self.var_email.set(row[6]),
     self.var_nationality.set(row[7]),
     self.var_id_proof.set(row[8]),
     self.var_id_number.set(row[9]),
     self.var_address.set(row[10])

    def Update(self):
     if self.var_mobile.get()=="":
         messagebox.showerror("Error","Please enter mobile no.",parent=self.root)
     else:
              
         
        conn=mysql.connector.connect(host="localhost",username="root",password="nitya@123",database="management")
   
        my_cursor=conn.cursor()    
        my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,idproof=%s,address=%s where Ref=%s",(
          
                                                                    
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    #self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get(),
                                                                    self.var_ref.get()
                                                                                          ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details has been updated successfully..",parent=self.root)

    def Delete(self):
      Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
      if Delete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="nitya@123",database="management")
          my_cursor=conn.cursor() 
          query="delete from customer where Ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)   
      else:
          if not Delete:
               return
      conn.commit()
      self.fetch_data()
      conn.close()  
'''
'''def Reset(self):
    #self.var_ref.set(""),
     self.var_cust_name.set(""),
     self.var_mother.set(""),
    #self.var_gender.set(""),
     self.var_post.set(""),
     self.var_mobile.set(""),
     self.var_email.set(""),
    #self.var_nationality.set(""),
    #self.var_id_proof.set(""),
     self.var_id_number.set(""),
     self.var_address.set(""),

     x=random.randint(1000,9999)
     self.var_ref.set(str(x))


    #def Search(self):
     #conn=mysql.connector.connect(host="localhost",username="root",password="nitya@123",database="management")
     #my_cursor=conn.cursor()

     #my_cursor.execute("select * from customer where "+str(self.Search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'") 
     #rows=my_cursor.fetchall()
     #if len(rows)!=0: 
      #   self.Cust_details_Table.delete(self.Cust_details_Table.get_children())
       #  for i in rows:
        #      self.Cust_details_Table.insert("",END,values=i) 
         #conn.commit()
         #conn.close() '''    
         
if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()