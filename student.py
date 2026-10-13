import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk # pip instal pillow
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os



class Student:
    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        # variables 
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stdid=StringVar()
        self.var_std=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

#1st image  which defines the upper part of project 
        base=os.path.dirname(__file__)
        image_path=os.path.join(base,"backtrasing","stu.avif")

        img=Image.open(image_path)
        img=img.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        self.btn_1=Button(self.root,command=self.open_img,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2nd image which defines the upper part of project

        # base__2=os.path.dirname(__file__)
        image_path1=os.path.join(base,"backtrasing","OIP.webp")
        img2=Image.open(image_path1)
        img2=img2.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        self.btn_1=Button(self.root,command=self.open_img_2,image=self.photoimg2,cursor="hand2")
        self.btn_1.place(x=540,y=0,width=540,height=160)

        # 3rd image which defines the upper part of project 
        # base__3=os.path.dirname(__file__)
        image_path3=os.path.join(base,"backtrasing","PM.jpeg")
            
        img3=Image.open(image_path3)
        img3=img2.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        self.btn_3=Button(self.root,command=self.open_img_3,image=self.photoimg3,cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=160)

#background image which defines the background of the project 
        image_path4=os.path.join(base,"backtrasing","bac.jpg")
        img5=Image.open(image_path4)
        img5=img5.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_lbl=Label(self.root,image=self.photoimg5,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)

        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM" ,font=(" times new roman", 37 ,"bold"),fg="red", bg="gray")
        lbl_title.place(x=0,y=0,width=1530,height=70)

            # MANAGE THE FRAME 
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="brown")
        Manage_frame.place(x=10,y=55,width=1500,height=560)

        # left frame 
        Leftframe=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Students Information",font=("times new roman",12,"bold"),fg="red",bg="#2C3E50")
        Leftframe.place(x=10,y=10,width=660,height=550)

        # 1 image 
        
       # 1 image
        # 1 image

        image_path6 = os.path.join(base, "backtrasing", "college.jpg")

        img6 = Image.open(image_path6)
        img6 = img6.resize((650, 120), Image.Resampling.LANCZOS)

        self.photoimg6 = ImageTk.PhotoImage(img6)

        my_img = Label(
            Leftframe,
            image=self.photoimg6,
            bd=2,
            relief=RIDGE
        )

        my_img.place(x=0, y=0, width=650, height=120)



        # current course label frame information
        std_lbl_info_frame=LabelFrame(Leftframe,bd=4,relief=RIDGE,padx=2,text="Students Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="#4B3D3C")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=115)

        #labels and Combobox 
        # Department 

        lbl_dept=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)
        combo_dept=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dept["value"]=("Select Department","Computer ","IT","Civil")
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #  Course
        course_std=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,state="readonly",font=("arial",12,"bold"),width=17)
        com_txtcourse_std["value"]=("Select Course","B.Tech","B.Sc","MCA","BCA")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        #year of course and student 
        current_year=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Year",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_current_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,state="readonly",font=("arial",12,"bold"),width=17)
        com_txt_current_year["value"]=("Select the year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,sticky=W,padx=2)

        # Semeseter details to fill in 
        semester=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
        semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        comsemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem,state="readonly",font=("arial",12,"bold"),width=17)
        comsemester["value"]=("Select Semester","sem-1","sem-2","sem-3","sem-4","sem-5")
        comsemester.current(0)
        comsemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # students class label frame information
        std_lbl_class_frame=LabelFrame(Leftframe,bd=4,relief=RIDGE,padx=2,text="Students Class Information",font=("times new roman",12,"bold"),fg="red",bg="#47899B")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=235)

        # details about students 
        #stuennts id
        std_id=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Students_ID:",bg="white")
        std_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        std_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_stdid,font=("times new roman",12,"bold"),width=22)
        std_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #name of students 
        Name=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Students Name:",bg="white")
        Name.grid(row=0,column=2,padx=2,pady=7)

        txt_Name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std,width=22,font=("arial",12,"bold"))
        txt_Name.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #division
        div=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Class Division:",bg="white")
        div.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Roll no
        Roll=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Roll No:",bg="white")
        Roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,width=22,font=("arial",12,"bold"))
        txt_Roll.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        # Gender 
        gender=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Gender:",bg="white")
        gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)
                
        com_txt_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender["value"]=("Select Gender ","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # DOB
        dob=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="DOB:",bg="white")
        dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,width=22,font=("arial",12,"bold"))
        txt_dob.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Email
        email=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Email:",bg="white")
        email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,width=22,font=("arial",12,"bold"))
        txt_email.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        # phone
        phone=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Mob NO:",bg="white")
        phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,width=22,font=("arial",12,"bold"))
        txt_phone.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        # Address of the students 
        address=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Address:",bg="white")
        address.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(std_lbl_class_frame,width=22,textvariable=self.var_address,font=("arial",12,"bold"))
        txt_address.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        # Teachers
        teacher=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Teacher Name:",bg="white")
        teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,width=22,textvariable=self.var_teacher,font=("arial",12,"bold"))
        txt_teacher.grid(row=4,column=3,sticky=W,padx=2,pady=7)

            # button 
        btn_frame=Frame(Leftframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="gray",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)
        
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="gray",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="gray",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)
        
        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="gray",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)


               # ===================== RIGHT FRAME =====================

        RIGHTframe = LabelFrame(
            Manage_frame,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Students Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="#375D2A"
        )
        RIGHTframe.place(x=690, y=10, width=800, height=550)

        # ===================== RIGHT FRAME IMAGE =====================

        image_path7 = os.path.join(base, "backtrasing", "college.jpg")

        img7 = Image.open(image_path7)
        img7 = img7.resize((790, 200), Image.Resampling.LANCZOS)

        self.photoimg7 = ImageTk.PhotoImage(img7)

        my_img1 = Label(
            RIGHTframe,
            image=self.photoimg7,
            bd=2,
            relief=RIDGE
        )
        my_img1.place(x=0, y=0, width=790, height=200)

        # ===================== SEARCH FRAME =====================

        searchframe = LabelFrame(
            RIGHTframe,
            bd=4,
            relief=RIDGE,
            padx=2,
            text="Search Student Information",
            font=("times new roman", 12, "bold"),
            fg="red",
            bg="#6699CC"
        )
        searchframe.place(x=0, y=200, width=790, height=60)

        search_by = Label(
            searchframe,
            font=("arial", 11, "bold"),
            text="Search By",
            fg="black"
        )
        search_by.grid(row=0, column=0, sticky=W, padx=6)

        # ===================== SEARCH =====================

        self.var_com_search = StringVar()

        com_txt_search = ttk.Combobox(
            searchframe,
            textvariable=self.var_com_search,
            state="readonly",
            font=("arial", 12, "bold"),
            width=18
        )

        com_txt_search["value"] = (
            "Select Option",
            "Roll",
            "Phone",
            "Student_id"
        )

        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()

        txt_search = ttk.Entry(
            searchframe,
            textvariable=self.var_search,
            width=22,
            font=("arial", 12, "bold")
        )
        txt_search.grid(row=0, column=2, sticky=W, padx=5)

        btn_search = Button(
            searchframe,
            text="Search",
            command=self.search_data,
            font=("arial", 11, "bold"),
            width=14,
            bg="gray",
            fg="white"
        )
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(
            searchframe,
            command=self.fetch_data,
            text="Show_All",
            font=("arial", 11, "bold"),
            width=14,
            bg="gray",
            fg="white"
        )
        btn_showall.grid(row=0, column=4, padx=5)

        # ===================== TABLE FRAME =====================

        tabel_frame = Frame(
            RIGHTframe,
            bd=4,
            relief=RIDGE,
            bg="#6B2A8F"
        )
        tabel_frame.place(x=0, y=260, width=790, height=250)

        Scroll_x = ttk.Scrollbar(
            tabel_frame,
            orient=HORIZONTAL
        )

        Scroll_y = ttk.Scrollbar(
            tabel_frame,
            orient=VERTICAL
        )

        # ===================== STUDENT TABLE =====================

        self.student_table = ttk.Treeview(
            tabel_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher"
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        # ===================== HEADINGS =====================

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")

        self.student_table["show"] = "headings"

        # ===================== COLUMN WIDTH =====================

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind(
            "<ButtonRelease>",
            self.get_cursor
        )

        self.fetch_data()

    def add_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_stdid.get()=="" ):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashvi@ch#8273$",database="students")
                my_cursor=conn.cursor()  #we can write any name to sepecify it
                my_cursor.execute("insert into children values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_stdid.get(),
                                                                                                            self.var_std.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get()
                                                                                                         ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Seccess","Students have been added ",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # fetch functions
    def fetch_data(self):
        
        conn=mysql.connector.connect(host="localhost",user="root",password="yashvi@ch#8273$",database="students")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from children")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
# get cursor 
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_stdid.set(data[4])
        self.var_std.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])



    def update_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_stdid.get()=="" ):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("update","Are you sure update this children data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="yashvi@ch#8273$",database="students")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update children set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                self.var_std.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_stdid.get()
                                                                                                                                     ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()


                messagebox.showinfo("Success","children successelly updated ",parent=self.root)    

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#delete data
    def delete_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","All Fields are require")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delete this children")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="yashvi@ch#8273$",database="students") 
                    my_cursor=conn.cursor()
                    sql="delete from children where Student_id=%s"
                    value=(self.var_stdid.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","your data has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # Reset 
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select Course")
        self.var_year.set("select Year")
        self.var_sem.set("select Semester")
        self.var_std.set("")
        self.var_stdid.set("")
        self.var_div.set("Select Devision")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Errow","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="yashvi@ch#8273$",database="students") 
                my_cursor=conn.cursor()
                column=self.var_com_search.get()
                if column=="Select Option":
                    messagebox.showerror("Error","PI ease select search option",parent=self.root)
                    return
                sql="select * from children where " +column+ " LIKE %s"
                my_cursor.execute(sql,(str(self.var_search.get()) + "%",))
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                else:
                    messagebox.showinfo("Result","No record found")
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



# openimage
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open images ",filetypes=((" JPG File", "*.jpg"),("PNG File", "*.png"),("All files","*.*")))
        img=Image.open(fln)
        img_browse=img.resize((540,16),Image.ImageANTIALIAS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)
            

 #openimage
    def open_img_2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open images ",filetypes=((" JPG File", "*.jpg"),("PNG File", "*.png"),("All files","*.*")))
        img_1=Image.open(fln)
        img_browse_1=img_1.resize((540,16),Image.ImageANTIALIAS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse_1)
        self.btn_2.config(image=self.photoimg_browse)
            

 #openimage
    def open_img_3(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open images ",filetypes=((" JPG File", "*.jpg"),("PNG File", "*.png"),("All files","*.*")))
        img_3=Image.open(fln)
        img_browse_3=img_3.resize((540,16),Image.ImageANTIALIAS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse_3)
        self.btn_3.config(image=self.photoimg_browse)
            
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


