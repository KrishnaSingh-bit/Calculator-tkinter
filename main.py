
from tkinter import *

def insert(element):
    entry.insert(END,f"{element}")

def equals():
    r = entry.get()
    try:
        k = eval(r)
    except Exception:
        k = "⚠️ Error"
    entry.config(validate="none")
    entry.delete(0,END)
    entry.insert(END,k)
    entry.config(validate="key")


def AC():
    entry.delete(0,END)

def CE():
    r = entry.get()
    entry.delete(len(r)-1,END)

def hist(*args):
    try:
        new = str(eval(k.get()))
    except:
        new = ""
    his_var.set(new)

def Alpha_rem(char,new_val):
    if char.isalpha():
        return False
    if new_val == "":
        return True
    if len(new_val) == 1 and not new_val[0].isdigit():
        return False
    return True


window = Tk()
window.title("Calculator v2 (tkinter)")
window.geometry("390x500")
window.grid()
window.resizable(False, False)

window.config(bg="#ADEBB3")

icon = PhotoImage(file='image.png')
window.iconphoto(True, icon)

k = StringVar()
his_var = StringVar()
k.trace_add("write",hist)

noalpha = (window.register(Alpha_rem), "%S","%P")

entry = Entry(window, textvariable = k,validate="key",validatecommand=noalpha,width=13,font=("arial",40),bg = "#6BDB76",fg ="#0D3311",relief="flat",justify="right")
entry.grid(row = 0,column= 0,columnspan=17,sticky="nsew",padx=0,pady=0)


History = Label(window,textvariable = his_var ,width=24,font=("arial",20),bg = "#6BDB76", fg = "#0D3311",relief="flat",anchor="e")
History.grid(row = 1,column= 0,columnspan=17,sticky="nsew",padx=0,pady=0)

movin = Label(window,text="Calculator by Krishna" ,width=1,font=("Cascadia Code",20),bg = "#ADEBB3", fg = "#0D3311",relief="flat",anchor="center")
movin.grid(row = 6,column= 0,columnspan=17,sticky="nsew",padx=0,pady=0)

oneB = Button(window,
                text= "1",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(1), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

twoB = Button(window,
                text= "2",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(2), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

threeB = Button(window,
                text= "3",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(3), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

fourB = Button(window,
                text= "4",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(4), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

fiveB = Button(window,
                text= "5",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(5), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

sixB = Button(window,
                text= "6", font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(6), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

sevenB = Button(window,
                text= "7",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(7), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

eightB = Button(window,
                text= "8",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(8), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

nineB = Button(window,
                text= "9",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(9), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

zeroB = Button(window,
                text= "0",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(0), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

pointB = Button(window,
                text= ".",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("."), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

plusB = Button(window,
                text= "+",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("+"), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

minusB = Button(window,
                text= "-",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("-"), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

divideB = Button(window,
                text= "÷",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("/"), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

multiplyB = Button(window,
                text= "×",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("*"), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

preparaB = Button(window,
                text= "(",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert("("), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

posparaB = Button(window,
                text= ")",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= lambda:insert(")"), 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

equalsB = Button(window,
                text= "=",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= equals, 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

AcB = Button(window,
                text= "AC",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= AC, 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)

CeB = Button(window,
                text= "CE",  font=("arial", 16), width=4, height=2,
                fg= "#0D3311",bg= "#ADEBB3", relief= "flat",
                command= CE, 
                activebackground= '#6BDB76',activeforeground= "#0D3311",
                state= NORMAL)


oneB.grid(row = 4,column= 2,sticky="nsew",ipadx=10, ipady=10)
twoB.grid(row = 4,column= 1,sticky="nsew",ipadx=10, ipady=10)
threeB.grid(row = 4,column= 0,sticky="nsew",ipadx=10, ipady=10)
fourB.grid(row = 3,column= 2,sticky="nsew",ipadx=10, ipady=10)
fiveB.grid(row = 3,column= 1,sticky="nsew",ipadx=10, ipady=10)
sixB.grid(row = 3,column= 0,sticky="nsew",ipadx=10, ipady=10)
sevenB.grid(row = 2,column= 2,sticky="nsew",ipadx=10, ipady=10)
eightB.grid(row = 2,column= 1,sticky="nsew",ipadx=10, ipady=10)
nineB.grid(row = 2,column= 0,sticky="nsew",ipadx=10, ipady=10)
zeroB.grid(row = 5,column= 0,sticky="nsew",ipadx=10, ipady=10)
pointB.grid(row = 5,column= 1,sticky="nsew",ipadx=10, ipady=10)
plusB.grid(row = 4,column= 3,sticky="nsew",ipadx=10, ipady=10)
minusB.grid(row = 5,column= 3,sticky="nsew",ipadx=10, ipady=10)
divideB.grid(row = 2,column= 3,sticky="nsew",ipadx=10, ipady=10)
multiplyB.grid(row = 3,column= 3,sticky="nsew",ipadx=10, ipady=10)
preparaB.grid(row = 4,column= 4,sticky="nsew",ipadx=10, ipady=10)
posparaB.grid(row = 5,column= 4,sticky="nsew",ipadx=10, ipady=10)
equalsB.grid(row = 5,column= 2,sticky="nsew",ipadx=10, ipady=10)
AcB.grid(row = 3,column= 4,sticky="nsew",ipadx=10, ipady=10)
CeB.grid(row = 2,column= 4,sticky="nsew",ipadx=10, ipady=10)



window.mainloop()
