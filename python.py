from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from customer import Cust_Win
from details import DetailsRoom
from room import Roombooking




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")

        img1=Image.open(r"C:\Users\user\Desktop\hotel mng\hh\roberto-nickson-MA82mPIZeGI-unsplash.jpg")
        img1=img1.resize((1250,160),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1350,height=150)

        lbl_title =Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("FORTE", 30, "bold"), bg="BLACK",fg="white")
        lbl_title.place (x=0,y=140,width =1350,height=50)

        main_frame=Frame(self.root,bd=8,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1350,height=620)

        lbl_menu =Label(main_frame,text="MENU",font=("TIMES NEW ROMAN", 20, "bold"), bg="BLACK",fg="gold" ,bd=5,relief=RIDGE)

        lbl_menu.place(x=0,y=0,width=230)

        btn_frame=Frame(self.root,bd=8,relief=RIDGE)
        btn_frame.place(x=0,y=235,width=238,height=190)


        cust_btn=Button (btn_frame ,text="CUSTOMER",command=self.cust_details,width=22,font=("TIMES NEW ROMAN", 15, "bold"), bg="BLACK",fg="gold" ,bd=0)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button (btn_frame ,text="ROOM",command=self.roombooking,width=22,font=("TIMES NEW ROMAN", 15, "bold"), bg="BLACK",fg="gold" ,bd=0)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button (btn_frame ,text="DETAIL",command=self.DetailsRoom,width=22,font=("TIMES NEW ROMAN", 15, "bold"), bg="BLACK",fg="gold" ,bd=0)
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button (btn_frame ,text="REPORT",width=22,font=("TIMES NEW ROMAN", 15, "bold"), bg="BLACK",fg="gold" ,bd=0)
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button (btn_frame ,text="LOGOUT",width=22,font=("TIMES NEW ROMAN", 15, "bold"), bg="BLACK",fg="gold" ,bd=0)
        logout_btn.grid(row=4,column=0,pady=1)

        img2=Image.open(r"C:\Users\user\Desktop\hh\people-2593251_1280.jpg")
        img2=img2.resize((1250,490),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(main_frame,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1210,height=490)

        
        img3=Image.open(r"C:\Users\user\Desktop\hh\people-2593251_1280.jpg")
        img3=img3.resize((240,120),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img2)
        lblimg2=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=210)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)  


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root) 
    root.mainloop()

