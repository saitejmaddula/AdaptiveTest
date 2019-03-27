from tkinter import  *
from _overlapped import NULL
import random
import mysql.connector 
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
mycursor=cnx.cursor();
curdblevel=1;
curoslevel=1;
curproglevel=1;
database={0:[],1:[],2:[]}
os={0:[],1:[],2:[]}
prog={0:[],1:[],2:[]}
def available():
    global database
    global os
    global prog
    global mycursor
    query=("Select qid from questionbank where qid like 'DE%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    database[0]=DM    
    query=("Select qid from questionbank where qid like 'DM%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    database[1]=DM 
    query=("Select qid from questionbank where qid like 'DH%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    database[2]=DM 
    query=("Select qid from questionbank where qid like 'OE%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    os[0]=DM    
    query=("Select qid from questionbank where qid like 'OM%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    os[1]=DM 
    query=("Select qid from questionbank where qid like 'OH%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    os[2]=DM 
    query=("Select qid from questionbank where qid like 'PE%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    prog[0]=DM    
    query=("Select qid from questionbank where qid like 'PM%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    prog[1]=DM 
    query=("Select qid from questionbank where qid like 'PH%' ")
    mycursor.execute(query)
    DM=[]
    for i in mycursor:
        DM=DM+[i[0]]
    prog[2]=DM 


chance=1
def getquestion():
    global chance
    if chance == 1:
        q=random.choice(database[curdblevel])
        database[curdblevel].remove(q)
    if chance == 2:
        q=random.choice(os[curoslevel])
        os[curoslevel].remove(q)
    if chance == 3:
        q=random.choice(prog[curproglevel])
        prog[curproglevel].remove(q)
    chance=(chance+1)%3 + 1
    q="'"+str(q)+"'"
    s="Select * from questionbank where qid="+q
    query=(s)
    mycursor.execute(query)
    for i in mycursor:
        question,option1,option2,option3,option4,answer=i[1],i[2],i[3],i[4],i[5],i[6]
        break
    print(q)
    return (question,option1,option2,option3,option4,answer)
           
            
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))
    

app = Tk()
app.geometry("1500x1500")
op1=Button()
op2=Button()
op3=Button()
op4=Button()
frame=Frame(app)
frame.place(relx=0.3,rely=0.2,width=500,height=500)
fr=Frame(app)
report=Frame()
l = Label(frame,text="Welcome")
l.place(x=225,y=70)
name=Label(frame,text="Name")
name.place(x=150,y=100)
nm_entry=Entry(frame)
nm_entry.place(x=200,y=100)
k=Label(frame,text="Reg.No")
k.place(x=144,y=130)
reg_entry=Entry(frame)
reg_entry.place(x=200,y=130)
m=Label(frame,text="Email")
m.place(x=150,y=160)
email_entry=Entry(frame)
email_entry.place(x=200,y=160)
i=1

def nxtpressed():
    global op_finish,op_next,l,i,op1,op2,op3,op4,op_next,q
    op_next.place_forget()
    op1.place_forget()
    op2.place_forget()
    op3.place_forget()
    op4.place_forget()
    q.place_forget()
    i=i+1
    if(i<15):
        newwin()
    elif(i==15):
        newwin()
        op_next['state']=DISABLED
        op_finish.place(relx=0.5,rely=0.15+l)
        
        
def callop(ops,cans):
    global op1,op2,op3,op4,curdblevel,curoslevel,curproglevel,chance
    lb=[]
    lb=[op1,op2,op3,op4]
    lb[cans-1]["bg"]="green"
    if(ops!=cans):
        lb[ops-1]["bg"]="red"
    if ops==cans:
        if chance==2:
            if curdblevel==0 or curdblevel==1:
                curdblevel+=1
        if chance==3:
            if curoslevel==0 or curoslevel==1:
                curoslevel+=1
        if chance==1:
            if curproglevel==0 or curproglevel==1:
                curproglevel+=1                
                
        
def finpressed():
        report.place(x=0,y=0,width=1500,height=1500)
        title=Label(report,text="Report",font=('Courier',20))
        title.place(relx=0.46,rely=0.06)
def newwin():
    global op1,op2,op3,op4,op_next,q,op_finish,l,i
    d={}
    question,option1,option2,option3,option4,answer=getquestion()
    d={'A':1,'B':2,'C':3,'D':4}
    fr.place(x=0,y=0,width=1500,height=1500)
    q=Label(fr,text="Q"+str((i))+question,borderwidth=2,relief="solid",padx=10,pady=10,wraplengt=800,font=("Courier", 18))
    q.place(relx=0.15,rely=0.1)
    op1=Button(fr,text=option1,font=('Courier',18),wraplengt=800,command=lambda:callop(1,d[answer]))
    op2=Button(fr,text=option2,font=('Courier',18),wraplengt=800,command=lambda:callop(2,d[answer]))
    op3=Button(fr,text=option3,font=('Courier',18),wraplengt=800,command=lambda:callop(3,d[answer]))
    op4=Button(fr,text=option4,font=('Courier',18),wraplengt=800,command=lambda:callop(4,d[answer]))
    op_next=Button(fr,text="Next",font=('Courier',18),command=nxtpressed)
    op_finish=Button(fr,text="Finish",font=('Courier',18),command=finpressed)
    l=0;
    q.update()
    l=l+q.winfo_height()/1400
    op1.place(relx=0.15,rely=0.11+l)
    
    op1.update()
    l=l+op1.winfo_height()/1400
    op2.place(relx=0.15,rely=0.11+l)
    
    op2.update()
    l=l+op2.winfo_height()/1400
    op3.place(relx=0.15,rely=0.11+l)
    
    op3.update()
    l=l+op3.winfo_height()/1400
    op4.place(relx=0.15,rely=0.11+l)
    
    op4.update()
    l=l+op4.winfo_height()/1400
    op_next.place(relx=0.15,rely=0.15+l)
    
    
    
    
    
    
b=Button(frame,text="Begin Test",command=newwin)

b.place(x=225,y=190)
        
available()        
app.mainloop()