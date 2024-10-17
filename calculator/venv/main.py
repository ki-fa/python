import tkinter as tk

calculation = ""
result = ""
def addToCalc(symbol):
    global calculation
    global result
    if(result != ""):
       result = ""
       clearField()
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def evalCalc():
    global result 
    try: 
        result = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, result)
    except:
        clearField()
        textResult.insert(1.0, "Error")

def clearField():    
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

textResult = tk.Text(root, height=1, width=24, font=("Arial", 24))
textResult.grid(columnspan=20)

btn1 = tk.Button(root, text='1', command=lambda: addToCalc(1), width=6, font=("Arial"))
btn1.grid(row=1, column=1)
btn2 = tk.Button(root, text='2', command=lambda: addToCalc(2), width=6, font=("Arial"))
btn2.grid(row=1, column=2)
btn3 = tk.Button(root, text='3', command=lambda: addToCalc(3), width=6, font=("Arial"))
btn3.grid(row=1, column=3)
btn4 = tk.Button(root, text='4', command=lambda: addToCalc(4), width=6, font=("Arial"))
btn4.grid(row=2, column=1)
btn5 = tk.Button(root, text='5', command=lambda: addToCalc(5), width=6, font=("Arial"))
btn5.grid(row=2, column=2)
btn6 = tk.Button(root, text='6', command=lambda: addToCalc(6), width=6, font=("Arial"))
btn6.grid(row=2, column=3)
btn7 = tk.Button(root, text='7', command=lambda: addToCalc(7), width=6, font=("Arial"))
btn7.grid(row=3, column=1)
btn8 = tk.Button(root, text='8', command=lambda: addToCalc(8), width=6, font=("Arial"))
btn8.grid(row=3, column=2)
btn9 = tk.Button(root, text='9', command=lambda: addToCalc(9), width=6, font=("Arial"))
btn9.grid(row=3, column=3)
btn0 = tk.Button(root, text='0', command=lambda: addToCalc(0), width=6, font=("Arial"))
btn0.grid(row=5, column=2)
btnp = tk.Button(root, text='+', command=lambda: addToCalc('+'), width=6, font=("Arial"))
btnp.grid(row=6, column=1)
btnm = tk.Button(root, text='-', command=lambda: addToCalc('-'), width=6, font=("Arial"))
btnm.grid(row=6, column=2)
btnd = tk.Button(root, text='/', command=lambda: addToCalc('/'), width=6, font=("Arial"))
btnd.grid(row=6, column=3)
btnm = tk.Button(root, text='*', command=lambda: addToCalc('*'), width=6, font=("Arial"))
btnm.grid(row=7, column=1)
btnEquals = tk.Button(root, text='=', command=lambda: evalCalc(), width=6, font=("Arial"))
btnEquals.grid(row=7, column=2)
btnClear= tk.Button(root, text='clear', command=lambda: clearField(), width=6, font=("Arial"))
btnClear.grid(row=7, column=3)
root.mainloop()
