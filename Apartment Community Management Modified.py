from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.linked_list = None  

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
#Linked list
class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

    def insert_linked_list(node, key):
        if node.linked_list is None:
            node.linked_list = LinkedListNode(key)
        else:
            current = node.linked_list
            while current.next:
                current = current.next
            current.next = LinkedListNode(key)

    def print_linked_list(head):
        current = head
        while current:
            print(current.key, end="\n")

            current = current.next
        print()

    def store_linked_list(head):

        L = []
        current = head
        while current:
            L.append(current.key)

            current = current.next

        return L

    def search(head,user):
        if head is None:
            return None
        pos=1
        curr=head
        while curr is not None:
            if curr.key[0]==user:
                return curr.key
            pos=pos+1
            curr=curr.next
        return None
    
        
#Insertion
root = Node("Spik and Span")
root.left = Node("Magenta")
root.right = Node("Turquoise")
LinkedListNode.insert_linked_list(root.left, ['Tariq','Tariq@123','Tariq','Magenta','M101','9010588157','tariqsknsp@gmail.com','Rs.0','A'])
LinkedListNode.insert_linked_list(root.left, ['Syed','4FIU98kF','Syed','Magenta','M102','7452409304','syedsns@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Vijay','couJpE9B','Vijay','Magenta','M103','6385095923','vijaysns@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.left, ['Sandhya','HgDrbRaS','Sandhya','Magenta','M104','9718092648','sandhyasns@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Geetha','7ujv2VX4','Geetha','Magenta','M105','9534112806','geethasns@gmail.com','10000','R'])

LinkedListNode.insert_linked_list(root.left, ['','','','Magenta','M201','','','',''])
LinkedListNode.insert_linked_list(root.left, ['Murari','nMAkWJsH','Murari','Magenta','M202','8103990774','murarisns@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.left, ['Arya','MqoVOAFL','Arya','Magenta','M203','6116446764','aryasns@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Santhosh','ViTh24th','Santhosh','Magenta','M204','9510184203','santhosh@gmail.com','15000','R'])
LinkedListNode.insert_linked_list(root.left, ['Nandha','QQ6pt0zB','Nandha','Magenta','M205','9394176641','nandha@gmail.com','5000','R'])

LinkedListNode.insert_linked_list(root.left, ['Jyotsana ','WNs481ac','Jyotsana ','Magenta','M301','8947561238','jyotsana @gmail.com','15000','R'])
LinkedListNode.insert_linked_list(root.left, ['Javed','E2z8YsrX','Javed','Magenta','M302','8101490656','javed@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Kamal','qqnjOLJ7','Kamal','Magenta','M303','7863501905','kamal@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.left, ['Niraj','Eihnghkq','Niraj','Magenta','M304','6374852648','niraj@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Aparna','4eMVC79J','Aparna','Magenta','M305','9368524170','aparna@gmail.com','0','R'])

LinkedListNode.insert_linked_list(root.left, ['Mohammed','MVSxWgFx','Mohammed','Magenta','M401','9571384206','mohammed@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.left, ['','','','Magenta','M402','','','',''])
LinkedListNode.insert_linked_list(root.left, ['Lavanya','QUuI7D6f','Lavanya','Magenta','M403','8523691470','lavanya@gmail.com','25000','R'])
LinkedListNode.insert_linked_list(root.left, ['Mithali','4FIU98kF','mithali','Magenta','M404','7452409304','mithali@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Kumari','mZXKGq8A','Kumari','Magenta','M405','9510234786','kumari@gmail.com','0','R'])
                                      
LinkedListNode.insert_linked_list(root.left, ['','','','Magenta','M501','','','',''])
LinkedListNode.insert_linked_list(root.left, ['Khalid','v7N39GQJ','Khalid','Magenta','M502','8856974100','khalid@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Anandi','kZCH0hH1','Anandi','Magenta','M503','9638527410','anandi@gmail.com','25000','R'])
LinkedListNode.insert_linked_list(root.left, ['Tharini','ELejwBFa','Tharini','Magenta','M504','9837492003','tharini@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Rijja','Rijja@123','Rijja','Magenta','M505','9856592423','rijjasknsn@gmail.com','Rs.0','A'])


LinkedListNode.insert_linked_list(root.left, ['Nisha','s2x9tWbo','Nisha','Magenta','M','8547963251','nisha@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Harry','htBVSOWu','Harry','Magenta','6B','9004157633','harry@gmail.com','15000','R'])
LinkedListNode.insert_linked_list(root.left, ['Nanditha','dxB1YbX9','Nanditha','Magenta','6C','8067431298','nanditha@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.left, ['','','','Magenta','6D','','','',''])
LinkedListNode.insert_linked_list(root.left, ['Pavani','4mFZkPXc','Pavani','Magenta','6E','8585747496','pavani@gmail.com','5000','R'])

LinkedListNode.insert_linked_list(root.left, ['Abhinandha','QQ6pt0zB','Abhinandha','Magenta','7A','9394176641','abhinandha@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.left, ['Nikhil','cfK1EULo','Nikhil','Magenta','7B','8558966370','nikhil@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Hema','IXyArRQX','Hema','Magenta','7C','7282414605','hema@gmail.com','25000','R'])
LinkedListNode.insert_linked_list(root.left, ['Pramitha','IKUoP5fT','Pramitha','Magenta','7D','7909101310','pramitha@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.left, ['Varshigan','CAZKdh6X','Varshigan','Magenta','7E','8866992201','varshigan@gmail.com','5000','R'])
                              
LinkedListNode.insert_linked_list(root.left, ['Sowmya','f6S6qmt8','Sowmya','Magenta','8A','8192734065','sowmya@gmail.com','10000','R'])                              
LinkedListNode.insert_linked_list(root.left, ['Babar','9RUvzUj9','Babar','Magenta','8B','7538942160','babar@gmail.com','25000','R'])
LinkedListNode.insert_linked_list(root.left, ['Zeenath','z186qGgt','Zeenath','Magenta','8C','6451264875','zeenath@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Meghana','AdSiwixf','Meghana','Magenta','8D','9045687230','meghana@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.left, ['Jothi','M580pudq','Jothi','Magenta','8E','6378952014','jothi@gmail.com','0','R'])
                              
LinkedListNode.insert_linked_list(root.left, ['Shriya','4RfySh08','Shriya','Magenta','9A','7288122209','shriya@gmail.com','25,000','R'])
LinkedListNode.insert_linked_list(root.left, ['Abinath','Na08RftU','Abinath','Magenta','9B','9787933062','abinath@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Navin','IEtfAgIb','Navin','Magenta','9C','8485166623','navin@gmail.com','15,000','R'])
LinkedListNode.insert_linked_list(root.left, ['Harvin','Ic8BmC7x','Harvin','Magenta','9D','9723202528','harvin@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Rakshitha','Rakshi@123','Rakshitha','Magenta','9E','9696853120','rakshitha@gmail.com','0','A'])
                              
LinkedListNode.insert_linked_list(root.left, ['Sethuraman','Qd4LOdCK','Sethuraman','Magenta','10A','9570897558','sethuraman@gmail.com','10,000','R'])
LinkedListNode.insert_linked_list(root.left, ['Vaibhav','HMI8zkUh','Vaibhav','Magenta','10B','8043600721','vaibhav@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.left, ['','','','Magenta','10C','','','',''])
LinkedListNode.insert_linked_list(root.left, ['Sruthi','s7QWIKss','Sruthi','Magenta','10D','9125436874','sruthi@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.left, ['Thaman','IakEvFqo','Thaman','Magenta','10E','9430294302','thaman@gmail.com','15000','R'])
                              

LinkedListNode.insert_linked_list(root.right, ['Lalit','LuW8WC1A','Lalit','Turquoise','T101','7130292116','lalit@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['','','','Turquoise','1B','','','',''])
LinkedListNode.insert_linked_list(root.right, ['Srija','MZ2tko8r','Srija','Turquoise','1C','9307229055','srija@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Nyla','Kjk0mov5','Nyla','Turquoise','1D','8305776726','nyla@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['Swapnil','5eUdqQyr','Swapnil','Turquoise','1E','9389310063','swapnil@gmail.com','5000','R'])
                              
LinkedListNode.insert_linked_list(root.right, ['Deepan','pXj8inQm','Deepan','Turquoise','2A','9726269715','deepan@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Varshini','iLjayIgh','Varshini','Turquoise','2B','7117238989','varshini@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Laxman','wFIXCFkU','Laxman','Turquoise','2C','7053668115','laxman@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Rindhya','gFL65ErG','Rindhya','Turquoise','2D','9483384913','rindhya@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Venkatesh','0Ybr47lc','Venkatesh','Turquoise','2E','9437439762','venkatesh@gmail.com','0','R'])
                              
LinkedListNode.insert_linked_list(root.right, ['Rebecca','QynRwZvX','Rebecca','Turquoise','3A','7251524079','rebecca@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['','','','Turquoise','3B','','','',''])
LinkedListNode.insert_linked_list(root.right, ['Akash','30u4SqpU','Akash','Turquoise','3C','7063164225','akash@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['John','qqftdv3z','John','Turquoise','3D','8513841553','john@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Mrudul','m0LkN0wC','Mrudul','Turquoise','3E','8182329725','mrudul@gmail.com','5000','R'])
                              
LinkedListNode.insert_linked_list(root.right, ['Goutham','XqgNBj2I','Goutham','Turquoise','4A','9440863512','goutham@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Mayank','G9vpL29B','Mayank','Turquoise','4B','9083735583','mayank@gmail.com','15000','R'])
LinkedListNode.insert_linked_list(root.right, ['Sharan','njaqyVeG','Sharan','Turquoise','4C','8439972861','sharan@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Shristi','SQoQQUAP','Shristi','Turquoise','4D','7080796468','shristi@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Rajesh','38ktluag','Rajesh','Turquoise','4E','8840271199','rajesh@gmail.com','0','R'])
                              
LinkedListNode.insert_linked_list(root.right, ['Vinay','mRexSLGl','Vinay','Turquoise','5A','7520770947','vinay@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Neelash','tZj9sGzf','Neelash','Turquoise','5B','8738751172','neelash@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Swathi','OsCgT0fP','Swathi','Turquoise','5C','7086328404','swathi@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['Arjun','8HFdkHAj','Arjun','Turquoise','5D','8891412576','arjun@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Rohith','Rohith@123','Rohith','Turquoise','5E','7524402456','rohith@gmail.com','0','A'])

LinkedListNode.insert_linked_list(root.right, ['Divya','EFdnHkXy','Divya','Turquoise','6A','9933354635','divya@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Arun','053iqLuX','Arun','Turquoise','6B','8850669755','arun @gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Tejaswini','T3AzDDvh','Tejaswini','Turquoise','6C','9881598619','tejaswini@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['Chandar','x3l2DX6I','Chandar','Turquoise','6D','6794803512','chandar@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Adharsh','n14b1r4q','Adharsh','Turquoise','6E','8534365903','adharsh@gmail.com','0','R'])	

LinkedListNode.insert_linked_list(root.right, ['Aaryan','1F5WmfQt','Aaryan','Turquoise','7A','8285626484','aaryan@gmail.com','5000','R'])		
LinkedListNode.insert_linked_list(root.right, ['Nitin','veGVXsTo','Nitin','Turquoise','7B','9032807836','nitin	@gmail.com','15000','R'])	
LinkedListNode.insert_linked_list(root.right, ['Kunal','AgmW9t2T','Kunal','Turquoise','7C','8889608602','kunal@gmail.com','10000','R'])		
LinkedListNode.insert_linked_list(root.right, ['Nithya','J9HpqODb','Nithya','Turquoise','7D','7590301090','nithya@gmail.com','0','R'])		
LinkedListNode.insert_linked_list(root.right, ['Mithun','ehgeB4Fi','Mithun','Turquoise','7E','9750569581','mithun@gmailcom','15000','R'])		

LinkedListNode.insert_linked_list(root.right, ['','','','Turquoise','8A','','','',''])
LinkedListNode.insert_linked_list(root.right, ['Priyan','UODjZ6pW','Priyan','Turquoise','8B','6832021023','priyan@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['Rajasri','Rajasri@123','Rajasri','Turquoise','8C','9790722911','rajasri@gmail.com','0','A'])
LinkedListNode.insert_linked_list(root.right, ['Sangavi','CpaaS8St','Sangavi','Turquoise','8D','8585969630','sangavi@gmail.com','25000','R'])
LinkedListNode.insert_linked_list(root.right, ['Pranav','hPJZliro','Pranav','Turquoise','8E','9623020046','pranav@gmail.com','15000','R'])
                   
LinkedListNode.insert_linked_list(root.right, ['Gowri','1G1VBmM2','Gowri','Turquoise','9A','6487987456','gowri@gmailcom','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Saathviga','hxhFNKUA','Turquoise','9B','9003125402','saathviga@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Ram','akR2u8JR','Ram','Turquoise','9C','8675420100','ram@gmail.com','5000','R'])
LinkedListNode.insert_linked_list(root.right, ['','','','Turquoise','9D','','','',''])
LinkedListNode.insert_linked_list(root.right, ['Krishna','WhHuPfkc','Krishna','Turquoise','9E','800063002','krishna@gmail.com','20000','R'])
                   
LinkedListNode.insert_linked_list(root.right, ['Rakesh','VausRsV9','Rakesh','Turquoise','10A','9639639630','rakesh@gmail.com','15000','R'])
LinkedListNode.insert_linked_list(root.right, ['Shreenithi','mL6QhdQ8','Shreenithi','Turquoise','10B','8528520008','shreenithi@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Anitha','GfMbv2so','Anitha','Turquoise','10C','7417418520','anitha@gmail.com','10000','R'])
LinkedListNode.insert_linked_list(root.right, ['Nilaa','wSkb0Ppi','Nilaa','Turquoise','10D','9340104391','nilaa@gmail.com','0','R'])
LinkedListNode.insert_linked_list(root.right, ['Karthik','UqYF0k7W','Karthik','Turquoise','10E','7516258987','karthik@gmail.com','5000','R'])

root.PrintTree()
Magenta = LinkedListNode.store_linked_list(root.left.linked_list)
Turquoise = LinkedListNode.store_linked_list(root.right.linked_list)

user=''
code=''

#Check
def check_adm():
    global user
    global code
    user_input = user.get()
    code_input = code.get()
    y = LinkedListNode.search(root.left.linked_list, user_input)
    z = LinkedListNode.search(root.right.linked_list, user_input)
    if (y is not None and user_input == y[0] and y[0] != '' and code_input == y[1]and y[8]=='A')or(z is not None and user_input == z[0] and z[0] != '' and code_input == z[1] and z[8]=='A' ):
       return adm_Profile()
    else:
        return error()

def check_res():
    global user
    global code
    global y
    global z
    user_input = user.get()
    code_input = code.get()
    y = LinkedListNode.search(root.left.linked_list, user_input)
    z = LinkedListNode.search(root.right.linked_list, user_input)
    if (y is not None and user_input == y[0] and y[0] != '' and code_input == y[1])or(z is not None and user_input == z[0] and z[0] != '' and code_input == z[1] and z[8]=='R' ):
        return res_Profile()
    else:
        return error()

def error():
    messagebox.showerror('Invalid Login', 'Username or Passsword is incorrect.\n Try Again')

#Home Page
def home_page():
    
    root=Tk()
    root.title("Apartment Home Page")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    image_path=PhotoImage(file="Apartment.png")
    bg_image=Label(root,image=image_path)
    bg_image.place(relheight=1,relwidth=1)

    text_label=Label(root,text='Welcome to Spik N Span',bg='white',font=('Georgie',24))
    text_label.pack(pady=50)

    button1 = Button(width=15,text="ADMIN LOGIN",bg='white',border=0,font=('Georgie',12),command=admin) 
    button1.pack(pady=20)
 
    button2 = Button( width=15,text = "RESIDENT LOGIN",bg='white',border=0,font=('Georgie',12),command=resident) 
    button2.pack(pady = 20)

    button3 = Button(width=15, text = "GUEST LOGIN",bg='white',border=0,font=('Georgie',12),command=guest)  
    button3.pack(pady = 20)
    
  
    root.mainloop()
    
#Admin login
def admin():
    
    global user
    global code
    
    root=Toplevel()
    root.title("Admin Login")
    root.configure(bg='#fff')
    root.geometry("925x500+400+200")

    root.resizable(False,False)

    img=PhotoImage(file="logo edit.png")
    Label(root,image=img,bg='white').place(x=50,y=50)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=50)

    heading=Label(frame,text='Admin Login',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light ',24,'bold'))
    heading.place(x=65,y=10)

    u=Label(frame,text='Username:',fg='black',font=('Microsoft YaHei UI light',11))
    u.place(x=30,y=80)

    username=StringVar()
    
    user=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11),textvariable=username)
    user.place(x=30,y=110)
    

    v=Label(frame,text='Password:',fg='black',font=('Microsoft YaHei UI light',11))
    v.place(x=30,y=150)

    password=StringVar()

    code=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11),textvariable=password)
    code.place(x=30,y=180)
    Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=check_adm).place(x=35,y=250)

    root.mainloop()

#Resident login
def resident():
    
    global user
    global code
    root=Toplevel()
    root.title("Resident Login")
    root.configure(bg='#fff')
    root.geometry("925x500+400+200")

    root.resizable(False,False)

    img=PhotoImage(file="logo edit.png")
    Label(root,image=img,bg='white').place(x=50,y=50)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=50)

    heading=Label(frame,text='Resident Login',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light ',24,'bold'))
    heading.place(x=65,y=10)

    u=Label(frame,text='Username:',fg='black',font=('Microsoft YaHei UI light',11))
    u.place(x=30,y=80)

    username=StringVar()
    
    user=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11),textvariable=username)
    user.place(x=30,y=110)
    

    v=Label(frame,text='Password:',fg='black',font=('Microsoft YaHei UI light',11))
    v.place(x=30,y=150)

    password=StringVar()

    code=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11),textvariable=password)
    code.place(x=30,y=180)
    Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=check_res).place(x=35,y=250)
 
    root.mainloop()

#Resident Home Page
def res_Profile():
    root=Toplevel()
    global y
    global z
    root.title("Resident Profile")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    image_path=PhotoImage(file="Apartment.png")
    bg_image=Label(root,image=image_path)
    bg_image.place(relheight=1,relwidth=1)

    frame=Frame(root,width=725,height=450,bg="white")
    frame.place(x=100,y=25)
    heading=Label(frame,text='PROFILE',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light ',24,'bold'))
    heading.place(x=60,y=25)

    img=PhotoImage(file="logo.png")
    Label(frame,image=img,bg='#fff').place(x=25,y=80)

    u=Label(frame,text='NAME:',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    u.place(x=300,y=100)
    a=Label(frame,text=y[0] if z == None else z[0] ,width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    a.place(x=450,y=100)

    v=Label(frame,text='BLOCK NAME:',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    v.place(x=300,y=140)
    b=Label(frame,text=y[3] if z == None else z[3] ,width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    b.place(x=450,y=140)

    w=Label(frame,text='FLAT NO:',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    w.place(x=300,y=180)
    c=Label(frame,text=y[4] if z == None else z[4] ,width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    c.place(x=450,y=180)

    x=Label(frame,text='PHONE NO:',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    x.place(x=300,y=220)
    d=Label(frame,text=y[5] if z == None else z[5] ,width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    d.place(x=450,y=220)

    r=Label(frame,text='Email ID:',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    r.place(x=300,y=260)
    d=Label(frame,text=y[6] if z == None  else z[6] ,width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    d.place(x=450,y=260)
    
    k=Label(frame,text='MAINTENANCE :',width=14,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    k.place(x=300,y=300)
    f=Label(frame,text=y[7] if z == None else z[7],width=20,bg='white',fg='black',font=('Microsoft YaHei UI light',13))
    f.place(x=450,y=300)
    
    root.mainloop()

#Admin Profile
def adm_Profile():
    root=Toplevel()
    root.geometry("925x500+400+200")
    root.title("Admin Home Page")
    root.resizable(False, False)
    bg_img = PhotoImage(file="Apartment.png")

    label1 = Label(root, image=bg_img)
    label2 = Label(root, text="Welcome Admin!", font=("Georgie", 24, 'bold'), bg= 'white')

    label1.pack()
    label2.place(x=150, y=230)

    frame1 = Frame(root, height=450, width=450, bg= "light grey")
    frame1.place(x=500, y=80)

    button1 = Button(frame1, text="Add Resident", width=20, bg='white', border=0, font=('Georgie', '12'),command=add_resident)
    button2 = Button(frame1, text="Remove Resident", width=20, bg='white', border=0, font=('Georgie', '12'))
    button3 = Button(frame1, text="Show Residents", width=20, bg='white', border=0, font=('Georgie', '12'), command=res_details)
    button4 = Button(frame1, text="Maintenance Status", width=20, bg='white', border=0, font=('Georgie', '12'))
    button5 = Button(frame1, text="Edit Maintenance", width=20, bg='white', border=0, font=('Georgie', '12'),command=edit_maint)

    button1.grid(row=1, column=0, pady=20, padx=20)
    button2.grid(row=2, column=0, pady=20)
    button3.grid(row=3, column=0, pady=20)
    button4.grid(row=4, column=0, pady=20)
    button5.grid(row=5, column=0, pady=20)
    
    root.mainloop()
""""
def delete_resi():
    global entry
    global enter
    root=Toplevel()
    
    root.title("Delete resident")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    img_path=PhotoImage(file="Apartment.png")
    img=Label(root,image=img_path)
    img.place(relheight=1,relwidth=1)


    frame=Frame(root,width=725,height=450,bg="white")
    frame.place(x=100,y=25)
    heading=Label(frame,text='DELETE RESIDENT',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light ',24,'bold'))
    heading.place(x=200,y=25)

    u=Label(frame,text='BLOCK NAME:',width=15,fg='black',font=('Microsoft YaHei UI light',13))
    u.place(x=100,y=130)

    v=Label(frame,text='FLAT NUMBER:',width=15,fg='black',font=('Microsoft YaHei UI light',13))
    v.place(x=100,y=210)

    blname=StringVar()
    entry=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11), textvariable=blname)
    entry.place(x=300,y=130)

    flat=StringVar()
    enter=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11), textvariable=flat)
    enter.place(x=300,y=210)

    but=Button(frame,text="SUBMIT",bg='#FF69B4',fg='white',font=('Microsoft YaHei UI light ',14),command=check_res)
    but.place(x=300,y=300)
    root.mainloop()
    
def check_res():
    global y
    global z
    global entry
    global enter
    user_input = entry.get()
    code_input = enter.get()
    y = LinkedListNode.store_linked_list(root.left.linked_list)
    z = LinkedListNode.store_linked_list(root.right.linked_list)
    if code_input==y[4]:
         y[0]=''
         y[1]=''
         y[2]=''
         y[5]=''
         y[6]=''
         y[7]=''
         y[8]=''
         print(y)
    elif code_input==z[4]:
         z[0]=''
         z[1]=''
         z[2]=''
         z[5]=''
         z[6]=''
         z[7]=''
         z[8]=''
         print(z)
         return new_page()
        
def new_page():
    root=Toplevel()
    label=Label(root,text='Resident deleted successfully',width=40,fg='black',font=('Microsoft YaHei UI light',13))
    label.place(x=150,y=150)
    root.mainloop()
""" 
    

def res_details():

    root = Toplevel()
    root.title("Residents")
    root.geometry("925x500+400+200")

    root.resizable(False, False)

    frame1 = Frame(root, height=400, width=720)
    frame1.place(x=100, y=50)

    img_path = PhotoImage(file="Apartment.png")
    label1 = Label(root, image=img_path)

    label2 = Label(frame1, text="RESIDENT'S DETAILS", fg='#57a1f8', bg='white',
                   font=('Microsoft YaHei UI light ', 24, 'bold'))

    # Labels placement
    label1.pack()
    label2.place(x=200, y=20)

    # Treeview initialisation
    treeview = ttk.Treeview(frame1, columns=['fl', 'name', 'num', 'mail'])
    treeview.column('#0', width=120, anchor='center', stretch=False)
    treeview.column('name', width=120, anchor='center', stretch=False)
    treeview.column('num', width=120, anchor='center', stretch=False)
    treeview.column('mail', width=170, anchor='center', stretch=False)
    treeview.column('fl', width=100, anchor='center', stretch=False)

    # Column Headers
    treeview.heading('#0', text="Block Name")
    treeview.heading('name', text="Name")
    treeview.heading('mail', text="Email ID")
    treeview.heading('num', text="Contact No")
    treeview.heading('fl', text="Flat No")

    # TreePlacement
    treeview.place(x=50, y=100)

    # Blocks
    treeview.insert('', '0', 'Block1', text="Magenta")
    treeview.insert('', '1', 'Block2', text="Turquoise")

    # Block1 insertion
    for i in Magenta:
        treeview.insert('Block1', 'end', values=[i[4],i[0],i[5],i[6]])

    # Block2 insertion
    for j in Turquoise:
        treeview.insert('Block2', 'end', values=[j[4],j[0],j[5],j[6]])

    scrollbar = ttk.Scrollbar(treeview, orient=VERTICAL, command=treeview.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    treeview.config(yscrollcommand=scrollbar.set)

    # Style
    style = ttk.Style(root)
    (style.theme_use("default"))

    # Overlay of Frame
    frame1.lift()

    root.mainloop()


def edit_maint():
    global entry
    global enter
    root=Toplevel()
    root.title("Edit maintainance")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    img_path=PhotoImage(file="Apartment.png")
    img=Label(root,image=img_path)
    img.place(relheight=1,relwidth=1)


    frame=Frame(root,width=725,height=450,bg="white")
    frame.place(x=100,y=25)
    heading=Label(frame,text='EDIT MAINTAINANCE',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light ',24,'bold'))
    heading.place(x=200,y=25)

    u=Label(frame,text='NAME:',width=15,fg='black',font=('Microsoft YaHei UI light',13))
    u.place(x=100,y=130)

    v=Label(frame,text='MAINTAINANCE:',width=15,fg='black',font=('Microsoft YaHei UI light',13))
    v.place(x=100,y=210)

    name=StringVar()
    entry=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11), textvariable=name)
    entry.place(x=300,y=130)

    maint=StringVar()
    enter=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Microsoft YaHei UI light',11), textvariable=maint)
    enter.place(x=300,y=210)

    but=Button(frame,text="SUBMIT",bg='#FF69B4',fg='white',font=('Microsoft YaHei UI light ',14),command=check_main)
    but.place(x=300,y=300)
    root.mainloop()

def check_main():
    global y
    global z
    global entry
    global enter
    user_input = entry.get()
    code_input = enter.get()
    y= LinkedListNode.search(root.left.linked_list, user_input)
    z= LinkedListNode.search(root.right.linked_list, user_input)
    if user_input==y[0]:
         y[7]=code_input
         print(y)
    elif code_input==z[0]:
        z[7]=code_input
    return next_page

def next_page():
    root=Toplevel()
    label=Label(root,text='Maintenance updated',width=40,fg='black',font=('Microsoft YaHei UI light',13))
    label.place(x=150,y=150)
    root.mainloop()
    
#Guest Home Page
def guest():
    root=Toplevel()
    root.title("Guest Home Page")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    image_path=PhotoImage(file="Apartment.png")
    img=Label(root,image=image_path)
    img.place(relheight=1,relwidth=1)

    frame=Frame(root,width=360,height=360,bg='white')
    frame.place(x=75,y=115)

    frames=Frame(root,width=360,height=360,bg='white')
    frames.place(x=500,y=115)

    img=PhotoImage(file="Contact us.png")
    width, height = 120,120
    img = img.subsample(int(img.width() // width), int(img.height() // height))
    Label(frame,image=img,bg='#fff').place(x=95,y=50)

    lab=Label(frame,text='For details contact:\n Tariq​ \n 9019901122 \n ​spiknspan@gmail.com​ \n Spik And Span \n Kalaivanar Street \n Ramnagar North Extn \n Madipakkam \n Chennai–600091',width=40,height=10)
    lab.place(x=40,y=170)

    lab1=Label(frames,text="VACANT HOUSES",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    lab1.place(x=60,y=40)

    label=Label(root,text="SPIK AND SPAN",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    label.place(x=350,y=15)

    labels=Label(root,text="GUEST LOGIN",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    labels.place(x=350,y=60)
    
# Treeview initialization
    treeview = ttk.Treeview(frames, columns=['fl'])
    treeview.column('#0', width=120, anchor='center', stretch=False)
    treeview.column('fl', width=120, anchor='center', stretch=False)

    # Column Headers
    treeview.heading('#0', text="Block name")
    treeview.heading('fl', text="Flat no")

    # TreePlacement
    treeview.place(x=55, y=90)

    # Blocks
    treeview.insert('', '0', 'Block1', text="Magenta")
    treeview.insert('', '1', 'Block2', text="Turquoise")


    #Block1 insertion
    for i in Magenta:
        if i[0]=='':
           treeview.insert('Block1','end',values=i[4])

    #Block2 insertion
    for j in Turquoise:
        if j[0]=='':
           treeview.insert('Block2','end',values=j[4])

    scrollbar = ttk.Scrollbar(frames, orient=VERTICAL, command=treeview.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    treeview.config(yscrollcommand=scrollbar.set)

    # Style
    style = ttk.Style(root)
    style.theme_use("default")

    frames.lift()
    root.mainloop()

def add_resident():

    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7
    global entry8

    root = Toplevel()
    root.geometry("925x500+400+200")
    root.title("Add Residents")
    root.resizable(False, False)


    image_path=PhotoImage(file="Apartment.png")
    img=Label(root,image=image_path)
    img.place(relheight=1,relwidth=1)
        
    frame=Frame(root,width=800,height=400,bg="white")
    frame.place(x=70,y=50)

    name= StringVar()
    flatno= StringVar()
    blockname= StringVar()
    username= StringVar()
    password= StringVar()
    phone = StringVar()
    email_id = StringVar()
    maintenance= StringVar()

    label1=Label(frame, text="Add Residents", fg="#57a1f8", font=("bold", 24)).place(x=300, y=40)
    label2=Label(frame, text="Name", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=120)
    label3=Label(frame, text="Flat No", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=170)
    label4=Label(frame, text="Block Name", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=220)
    label5=Label(frame, text="User Name", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=270)
    label6=Label(frame, text="Password", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=420, y=120)
    label7=Label(frame, text="Email ID", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=420, y=170)
    label8=Label(frame, text="Phone NO", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=420, y=220)
    label9=Label(frame, text="Maintenance", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=420, y=270)

    entry1=Entry(frame, textvariable=name).place(x=250, y=120)
    entry2=Entry(frame, textvariable=flatno).place(x=250, y=170)
    entry3=Entry(frame, textvariable=blockname).place(x=250, y=220)
    entry4=Entry(frame, textvariable=username).place(x=250, y=270)
    entry5=Entry(frame, textvariable=password).place(x=550, y=120)
    entry6=Entry(frame, textvariable=phone).place(x=550, y=170)
    entry7=Entry(frame, textvariable=email_id).place(x=550, y=220)
    entry8=Entry(frame, textvariable=maintenance).place(x=550, y=270)

    button1=Button(frame, text="Submit", bg="light pink", fg="white",font=("Microsoft YaHei UI light", 13,'bold'),command=addlist)
    button1.place(x=350, y=350)
    root.mainloop()

def addlist():
    global y
    global z
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7
    global entry8

    
        
    name=entry1.get()
    flat=entry2.get()
    block=entry3.get()
    username= entry4.get()
    passwo= entry5.get()
    phone=entry6.get()
    mail=entry7.get()
    maintain=entry8.get()
    
    y= LinkedListNode.search(root.left.linked_list,flat)
    z= LinkedListNode.search(root.right.linked_list, flat)
    if code_input==y[4]:
        y[0]=name
        y[1]=username
        y[2]=passwo
        y[3]=block
        y[5]=phone
        y[6]=mail
        y[7]=maintain
        y[8]='R'
    elif code_input==z[4]:
        z[0]=name
        z[1]=username
        z[2]=passwo
        z[3]=block
        z[5]=phone
        z[6]=mail
        z[7]=maintain
        z[8]='R'
    return messagebox.showinfo('RESIDENT ADDED SUCCESSFULLY')

home_page()






