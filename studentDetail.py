from cgitb import text
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import db_config

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")


        # ******************variables**************
        self.var_branch = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_course = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_div = StringVar()
        self.var_DOB = StringVar()
        self.var_gender = StringVar()
        self.var_Email = StringVar()
        self.var_phone = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher = StringVar()
        self.var_photo = StringVar()
        
        
        img = Image.open(r"images for project/background_face-1200x480.jpg")
        img= img.resize((1370,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=1370,height=150)

        # backgraund Image
        img1 = Image.open(r"images for project/images.png")
        img1= img1.resize((1370,1000),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl1=Label(self.root,image=self.photoimg1)
        first_lbl1.place(x=0,y=150,width=1370,height=1000)


        title_lbl = Label(first_lbl1,text="STUDENT MAMAGEMENT SYSTEM",bg="white",font=("times new roman",30,"bold"))
        title_lbl.place(x=0,y=0,width=1370,height=30)

        back_button=Button(first_lbl1,text="Back",command=self.Back_to_main,cursor="hand2")
        back_button.place(x=1265,y=0,width=90,height=30)


        # main frame
        mainFrame = Frame(first_lbl1,bd=2,bg="white")
        mainFrame.place(x=20,y=40,width=1320,height=500)

        # left label frame
        leftLabelFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        leftLabelFrame.place(x=10,y=5,width=680,height=480)

        # current courses of a student
        currentCourseFrame= LabelFrame(leftLabelFrame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        currentCourseFrame.place(x=5,y=0,width=670,height=120)

        # Branch 
        branchLabel = Label(currentCourseFrame,text="Branch",font=("times new roman",12,"bold"),bg="white")
        branchLabel.grid(row=0,column=0,padx=10)

        branchCombo = ttk.Combobox(currentCourseFrame,textvariable=self.var_branch,font=("times new roman",12,"bold"),state="readonly")
        branchCombo["values"]=("Select Branch" , "Computer Science Engineering", "Information technology", "Mechanical Engineering","Civil Engineering")
        branchCombo.current(0)
        branchCombo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Year
        yearLabel = Label(currentCourseFrame,text="Year",font=("times new roman",12,"bold"),bg="white")
        yearLabel.grid(row=0,column=2,padx=10)

        yearCombo = ttk.Combobox(currentCourseFrame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        yearCombo["values"]=("Select Year" , "2021-22", "2022-23", "2023-24","2024-25")
        yearCombo.current(0)
        yearCombo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Samester
        semesterLabel = Label(currentCourseFrame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semesterLabel.grid(row=1,column=0,padx=10)

        semesterCombo = ttk.Combobox(currentCourseFrame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        semesterCombo["values"]=("Select Semester" , "semester: 1", "semester: 2", "semester: 3","semester: 4")
        semesterCombo.current(0)
        semesterCombo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Course
        courseLabel = Label(currentCourseFrame,text="Course",font=("times new roman",12,"bold"),bg="white")
        courseLabel.grid(row=1,column=2,padx=10)

        courseCombo = ttk.Combobox(currentCourseFrame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        courseCombo["values"]=("Select Course" , "B.tech", "B.Sc.", "M.tech","M.Sc.")
        courseCombo.current(0)
        courseCombo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # class Student information
        currentStudentFrame= LabelFrame(leftLabelFrame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        currentStudentFrame.place(x=5,y=120,width=670,height=330)

        # Student id information
        studentIdLabel = Label(currentStudentFrame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentIdLabel.grid(row=0,column=0,padx=10,sticky=W)

        studentIdEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_ID,width=20,font=("times new roman",12,"bold"))
        studentIdEntry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Student name 
        studentNameLabel = Label(currentStudentFrame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentNameLabel.grid(row=0,column=2,padx=10,sticky=W)

        studentNameEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentNameEntry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Enrollment Number 
        inrollmentNumberLabel = Label(currentStudentFrame,text="Enrollment number:",font=("times new roman",12,"bold"),bg="white")
        inrollmentNumberLabel.grid(row=1,column=0,padx=10,sticky=W)

        inrollmentNumberEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        inrollmentNumberEntry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Class Division 
        classDivisionLabel = Label(currentStudentFrame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classDivisionLabel.grid(row=1,column=2,padx=10,sticky=W)

        DivisionIdEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        DivisionIdEntry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # DOB
        DOBLabel = Label(currentStudentFrame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOBLabel.grid(row=2,column=0,padx=10,sticky=W)

        DOBEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        DOBEntry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
        # Gender
        genderLabel = Label(currentStudentFrame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        genderLabel.grid(row=2,column=2,padx=10,sticky=W)

        genderEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        genderEntry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Email
        emailLabel = Label(currentStudentFrame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        emailLabel.grid(row=3,column=0,padx=10,sticky=W)

        emailEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_Email,width=20,font=("times new roman",12,"bold"))
        emailEntry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # phone number
        phonNumberLabel = Label(currentStudentFrame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phonNumberLabel.grid(row=3,column=2,padx=10,sticky=W)

        phoneNumberEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneNumberEntry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Address
        addressLabel = Label(currentStudentFrame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        addressLabel.grid(row=4,column=0,padx=10,sticky=W)

        addressEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_Address,width=20,font=("times new roman",12,"bold"))
        addressEntry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # Teacher name
        teacherNameLabel = Label(currentStudentFrame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacherNameLabel.grid(row=4,column=2,padx=10,sticky=W)

        teacherNameEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_Teacher,width=20,font=("times new roman",12,"bold"))
        teacherNameEntry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Redio button
        self.var_radio1=StringVar()
        picRedioBtn1= ttk.Radiobutton(currentStudentFrame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        picRedioBtn1.grid(row=5,column=0,padx=10,sticky=W)


        picRedioBtn2= ttk.Radiobutton(currentStudentFrame,variable=self.var_radio1,text="No photo sample",value="No")
        picRedioBtn2.grid(row=5,column=1,padx=10,sticky=W)

        # update or save buttons frame
        butn_frame=Frame(currentStudentFrame,bd=2,pady=3,relief=RIDGE,bg="white")
        butn_frame.place(x=0,y=200,width=660,height=100)
        
        
        save_Button=Button(butn_frame,command=self.addData,text="Save",font=("times new roman",13,"bold"),padx=10,width=14,bg="blue",fg="white")
        save_Button.grid(row = 0,column = 0)


        delete_Button=Button(butn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        delete_Button.grid(row = 0,column = 1)

        update_Button=Button(butn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        update_Button.grid(row = 0,column = 2)


        reset_Button=Button(butn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        reset_Button.grid(row = 0,column = 3)
        

        # take photo or update buttons
        take_frame=Frame(butn_frame,bd=2,pady=3,relief=RIDGE,bg="white")
        take_frame.place(x=0,y=33,width=655,height=40)

        takephoto_Button=Button(take_frame,text="Take Photo",command=self.generate_dataset,font=("times new roman",13,"bold"),width=30,bg="blue",fg="white")
        takephoto_Button.grid(row = 0,column = 0)


        updatePhoto_Button=Button(take_frame,text="Update Photo",font=("times new roman",13,"bold"),width=30,bg="blue",fg="white")
        updatePhoto_Button.grid(row = 0,column = 1)



        # right label frame
        rightLabelFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        rightLabelFrame.place(x=700,y=5,width=600,height=480)

        imgNormal = Image.open(r"images for project/background1.png")
        imgNormal= imgNormal.resize((600,140),Image.ANTIALIAS)
        self.photoimgNormal=ImageTk.PhotoImage(imgNormal)

        first_lblNormal=Label(rightLabelFrame,image=self.photoimgNormal)
        first_lblNormal.place(x=0,y=0,width=600,height=140)



        # *********** search system **************
        searchFrame= LabelFrame(rightLabelFrame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        searchFrame.place(x=5,y=140,width=590,height=70)


        searchLabel = Label(searchFrame,text="Search By: ",font=("times new roman",12,"bold"),bg="white")
        searchLabel.grid(row=0,column=0,padx=10)

        searchCombo = ttk.Combobox(searchFrame,font=("times new roman",12,"bold"),state="readonly",width=15)
        searchCombo["values"]=("Select","Roll No.","Phone No.")
        searchCombo.current(0)
        searchCombo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        searchEntry = ttk.Entry(searchFrame,width=20,font=("times new roman",12,"bold"))
        searchEntry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_Button=Button(searchFrame,text="Search",font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_Button.grid(row = 0,column = 3)

        showAll_Button=Button(searchFrame,text="Show All",font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_Button.grid(row = 0,column = 4)


        # *********** Table frame ************

        tableFrame=Frame(rightLabelFrame,bd=2,bg="white",relief=RIDGE)
        tableFrame.place(x=5,y=215,width=590,height=240)

        scroll_x=Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(tableFrame,orient=VERTICAL)

        self.studentTable = ttk.Treeview(tableFrame,column=("branch","year","sem","course","ID","name","roll","div","DOB","gender","Email","Phone","Address","Teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)

        self.studentTable.heading("branch",text="Branch")
        self.studentTable.heading("year",text="Year")
        self.studentTable.heading("sem",text="Semester")
        self.studentTable.heading("course",text="Course")
        self.studentTable.heading("ID",text="Student ID")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("roll",text="Enrollment Number")
        self.studentTable.heading("div",text="Class Division")
        self.studentTable.heading("DOB",text="DOB")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("Email",text="Email")
        self.studentTable.heading("Phone",text="Phone No.")
        self.studentTable.heading("Address",text="Address")
        self.studentTable.heading("Teacher",text="Teacher Name")
        self.studentTable.heading("photo",text="PhotoSampleStatus")
        self.studentTable["show"]="headings"

        self.studentTable.column("branch",width=100)
        self.studentTable.column("year",width=100)
        self.studentTable.column("sem",width=100)
        self.studentTable.column("course",width=100)
        self.studentTable.column("ID",width=100)
        self.studentTable.column("name",width=100)
        self.studentTable.column("roll",width=100)
        self.studentTable.column("div",width=100)
        self.studentTable.column("DOB",width=100)
        self.studentTable.column("gender",width=100)
        self.studentTable.column("Email",width=100)
        self.studentTable.column("Phone",width=100)
        self.studentTable.column("Address",width=100)
        self.studentTable.column("Teacher",width=100)
        self.studentTable.column("photo",width=100)
        
        

        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
        

    # ********** functions to add **********

    def addData(self):
        if(self.var_branch.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()==""):
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_branch.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_ID.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                                    
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
            
    # ****************** fetch data ********************

    def fetch_data(self):
        conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from new_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.studentTable.delete(*self.studentTable.get_children())
            for i in data:
                self.studentTable.insert("",END,values=i)
            conn.commit()
        conn.close()

    # *********** get cursor ************
    def get_cursor(self,event=""):
        cursor_focus = self.studentTable.focus()
        content=self.studentTable.item(cursor_focus)
        data=content["values"]



        self.var_branch.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_course.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_div.set(data[7]),
        self.var_DOB.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher.set(data[13]),
        self.var_radio1.set(data[14])


                
    #update function
    def update_data(self):
        if(self.var_branch.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update new_table set `branch`='%s' , `year`='%s' , `sem`='%s' , `course`='%s' , `name`='%s' , `roll`='%s' , `div`='%s' , `DOB`='%s' , `gender`='%s' ,`Email`='%s' , `Phone`='%s' , `Address`='%s' , `Teacher`='%s' , `photo`='%s' where `ID`='%s'"% (

                                                                                                                                                                                                                                self.var_branch.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_DOB.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_Address.get(),
                                                                                                                                                                                                                                self.var_Teacher.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_ID.get()
                                                                                                                                                                                                                            ))
                                                                                                                                                
                                                                                                                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



    #***************** reset function *************
    def reset_data(self):
        self.var_branch.set("Select Branch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_course.set("Select Course")
        self.var_ID.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_div.set("")
        self.var_DOB.set("")
        self.var_gender.set("")
        self.var_Email.set("")
        self.var_phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_photo.set("")

    # ************ delete function ********************
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
                    my_cursor=conn.cursor()
                    sql="delete from new_table where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deletes student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
                    
                    




    # *************** generate data set take photo sample************
    def generate_dataset(self):
        if(self.var_branch.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from new_table")
                myresult=my_cursor.fetchall()
                id=0
                # for x in myresult:
                #     id+=1
                my_cursor.execute("update new_table set `branch`='%s' , `year`='%s' , `sem`='%s' , `course`='%s' , `name`='%s' , `roll`='%s' , `div`='%s' , `DOB`='%s' , `gender`='%s' ,`Email`='%s' , `Phone`='%s' , `Address`='%s' , `Teacher`='%s' , `photo`='%s' where `ID`='%s'"% (

                                                                                                                                                                                                                                self.var_branch.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_DOB.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_Address.get(),
                                                                                                                                                                                                                                self.var_Teacher.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_ID.get()
                                                                                                                                                                                                                            ))
                id=self.var_ID.get()
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()    

                # ********load haarcascade from openCV**********

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling facto=1.3
                    # Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                
                cap=cv2.VideoCapture(0)

                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Student faces/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                                                                                                                                                                                                   # 
                    


    def Back_to_main(self):
        # self.old_window=Toplevel(self.root)
        # cv2.destroyAllWindows()
        self.root.destroy()
        # cv2.destroyWindow("")
        # self.app=Face_Recognition_System(self.new_window)


                                                                                                                                                                                            
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
