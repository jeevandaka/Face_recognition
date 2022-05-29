from email import message
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class login_Window:
    def __init__(self,root) :
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

    # ********** Back ground *******
        img1 = Image.open(r"images for project/login_bg2.jpg")
        img1= img1.resize((1500,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl1=Label(self.root,image=self.photoimg1)
        first_lbl1.place(x=0,y=0,width=1370,height=800)

    # *********** login fram **********
        frame=Frame(self.root,bg="black")
        frame.place(x=570,y=130,width=340,height=450)


        img2=Image.open(r"images for project/login_logo.png")
        img2= img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        first_lbl2.place(x=705,y=140,width=90,height=90)

        start_lbl = Label(frame,text="Get Start",font=("times new roman",20,"bold"),fg="white",bg="black")
        start_lbl.place(x=120,y=100)

    # ********* credentials ********
        username = Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=65,y=140)

        self.textuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.textuser.place(x=40,y=170,width=270)

        password = Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=65,y=215)

        self.textpassword=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.textpassword.place(x=40,y=245,width=270)

    # ************Icon images**********

        img3=Image.open(r"images for project/login_logo.png")
        img3= img3.resize((20,20),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        first_lbl3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        first_lbl3.place(x=610,y=274,width=25,height=25)


        img4=Image.open(r"images for project/login_icon2.jpg")
        img4= img4.resize((20,20),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        first_lbl4=Label(image=self.photoimg4,bg="black",borderwidth=0)
        first_lbl4.place(x=610,y=349,width=25,height=25)

    # *********** login button *************
        login_button=Button(frame,text="Login",command=self.login,font=("time new roman",15,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg='white',bg="red")
        login_button.place(x=110,y=300,width=120,height=30)

    # *********** register button *************
        register_button = Button(frame,text="New User Register",font=("time new roman",10,"bold"),cursor="hand2",borderwidth=0,relief=RIDGE,fg='white',bg="black")
        register_button.place(x=15,y=350,width=160)

    # *********** forgetpass button *************
        forget_button = Button(frame,text="Forget Password",font=("time new roman",10,"bold"),cursor="hand2",borderwidth=0,relief=RIDGE,fg='white',bg="black")
        forget_button.place(x=10,y=375,width=160)

    # *********** register button *************
        # register_button = Button(frame,text="Login",font=("time new roman",15,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg='white',bg="red")
        # register_button.place(x=110,y=300,width=120,height=30)
    
    def login(self):
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="kapu" and self.textpassword.get()=="ashu":
            messagebox.showinfo("Success","Welcome to project")
        else:
            messagebox.showerror("Error","Invalid username and password ")










if __name__ == "__main__":
    root=Tk()
    app=login_Window(root)
    root.mainloop()