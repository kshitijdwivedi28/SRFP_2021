import tkinter

from pyparsing import opAssoc

root = tkinter.Tk()
root.title("SIMPLE CALCULATOR")

# Input from user
enter_data = tkinter.Entry(root, width = 40, borderwidth = 5)
enter_data.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

num1 = 0
num2 = 0
op = ""
 
def inp_btn(num):
    curr_inp = enter_data.get()
    enter_data.delete(0, tkinter.END)
    enter_data.insert(0, curr_inp + str(num))
    
    
def clr_btn():
    enter_data.delete(0, tkinter.END)
    
def add_btn():
    global num1 
    num1 = enter_data.get()
    enter_data.delete(0, tkinter.END)
    global op
    op = "+"
    
def sub_btn():
    global num1 
    num1 = enter_data.get()
    enter_data.delete(0, tkinter.END)
    global op
    op = "-"
    
def mul_btn():
    global num1 
    num1 = enter_data.get()
    enter_data.delete(0, tkinter.END)
    global op
    op = "*"
    

def div_btn():
    global num1 
    num1 = enter_data.get()
    enter_data.delete(0, tkinter.END)
    global op
    op = "/"
    
    
def res_btn():
    num2 = enter_data.get()
    enter_data.delete(0, tkinter.END)

    if op == "+" :
        enter_data.insert(0, (int(num1) + int(num2)))
    elif op == "-" :
        enter_data.insert(0, (int(num1) - int(num2)))
    elif op == "*" :
        enter_data.insert(0, (int(num1) * int(num2)))
    elif op == "/" :
        enter_data.insert(0, (int(int(num1) / int(num2))))
        
    
    

# Creating buttons
btn_1 = tkinter.Button(root, text = "1", padx = 40, pady = 20, command = lambda : inp_btn(1))
btn_2 = tkinter.Button(root, text = "2", padx = 40, pady = 20, command = lambda : inp_btn(2))
btn_3 = tkinter.Button(root, text = "3", padx = 40, pady = 20, command = lambda : inp_btn(3))
btn_4 = tkinter.Button(root, text = "4", padx = 40, pady = 20, command = lambda : inp_btn(4))
btn_5 = tkinter.Button(root, text = "5", padx = 40, pady = 20, command = lambda : inp_btn(5))
btn_6 = tkinter.Button(root, text = "6", padx = 40, pady = 20, command = lambda : inp_btn(6))
btn_7 = tkinter.Button(root, text = "7", padx = 40, pady = 20, command = lambda : inp_btn(7))
btn_8 = tkinter.Button(root, text = "8", padx = 40, pady = 20, command = lambda : inp_btn(8))
btn_9 = tkinter.Button(root, text = "9", padx = 40, pady = 20, command = lambda : inp_btn(9))
btn_0 = tkinter.Button(root, text = "0", padx = 40, pady = 20, command = lambda : inp_btn(0))

btn_plus = tkinter.Button(root, text = "+", padx = 40, pady = 20, command = add_btn)
btn_sub = tkinter.Button(root, text = "-", padx = 40, pady = 20, command = sub_btn)
btn_mul = tkinter.Button(root, text = "x", padx = 40, pady = 20, command = mul_btn)
btn_div = tkinter.Button(root, text = "/", padx = 40, pady = 20, command = div_btn)


btn_res = tkinter.Button(root, text = "RES", padx = 32.5, pady = 20, command = res_btn)
btn_clr = tkinter.Button(root, text = "CLR", padx = 32.5, pady = 20, command = clr_btn)




# Putting them on screen
btn_1.grid(row = 3, column = 0)
btn_2.grid(row = 3, column = 1)
btn_3.grid(row = 3, column = 2)

btn_4.grid(row = 2, column = 0)
btn_5.grid(row = 2, column = 1)
btn_6.grid(row = 2, column = 2)

btn_7.grid(row = 1, column = 0)
btn_8.grid(row = 1, column = 1)
btn_9.grid(row = 1, column = 2)

btn_0.grid(row = 4, column = 1)

btn_plus.grid(row = 5, column = 0, columnspan = 2)
btn_sub.grid(row = 5, column = 1, columnspan = 2)
btn_mul.grid(row = 6, column = 0, columnspan = 2)
btn_div.grid(row = 6, column = 1, columnspan = 2)

btn_res.grid(row = 7, column = 0, columnspan = 2)
btn_clr.grid(row = 7, column = 1, columnspan = 2)


root.mainloop()
















print("FINALLY DID IT, BY KSHITIJ DWIVEDI")