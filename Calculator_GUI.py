from tkinter import *
expression = "" 
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 

def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 
	except: 
		equation.set(" error ") 
		expression = "" 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
if __name__ == "__main__": 
	gui = Tk() 
	gui.configure(background="Gray") 
	gui.title("Simple Calculator") 
	gui.geometry("365x410") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation, font=('Arial', 30), 
                          bd=10, insertwidth=4, width=14, borderwidth=4) 
	expression_field.grid(column=0,row=0, columnspan=4, padx=10, pady=10)
 
	button1 = Button(gui, text=' 1 \nOne', fg='black', bg='Light Gray', 
					command=lambda: press(1), height=3, width=10) 
	button1.grid(row=2, column=0, padx=5, pady=5) 

	button2 = Button(gui, text=' 2 \nTwo', fg='black', bg='Light Gray', 
					command=lambda: press(2), height=3, width=10) 
	button2.grid(row=2, column=1, padx=5, pady=5) 

	button3 = Button(gui, text=' 3\nThree ', fg='black', bg='Light Gray', 
					command=lambda: press(3), height=3, width=10) 
	button3.grid(row=2, column=2, padx=5, pady=5) 

	button4 = Button(gui, text=' 4 \nFour', fg='black', bg='Light Gray', 
					command=lambda: press(4), height=3, width=10) 
	button4.grid(row=3, column=0, padx=5, pady=5) 

	button5 = Button(gui, text=' 5 \nFive', fg='black', bg='Light Gray', 
					command=lambda: press(5), height=3, width=10) 
	button5.grid(row=3, column=1, padx=5, pady=5) 

	button6 = Button(gui, text=' 6 \nSix', fg='black', bg='Light Gray', 
					command=lambda: press(6), height=3, width=10) 
	button6.grid(row=3, column=2, padx=5, pady=5) 

	button7 = Button(gui, text=' 7\nSeven ', fg='black', bg='Light Gray', 
					command=lambda: press(7), height=3, width=10) 
	button7.grid(row=4, column=0, padx=5, pady=5) 

	button8 = Button(gui, text=' 8\nEight ', fg='black', bg='Light Gray', 
					command=lambda: press(8), height=3, width=10) 
	button8.grid(row=4, column=1, padx=5, pady=5) 

	button9 = Button(gui, text=' 9\nNine ', fg='black', bg='Light Gray', 
					command=lambda: press(9), height=3, width=10) 
	button9.grid(row=4, column=2, padx=5, pady=5) 

	button0 = Button(gui, text=' 0\nZero ', fg='black', bg='Light Gray', 
					command=lambda: press(0), height=3, width=22) 
	button0.grid(row=5, column=1,columnspan=2, padx=5, pady=5) 

	plus = Button(gui, text=' + \nSum', fg='black', bg='Light Gray', 
				command=lambda: press("+"), height=3, width=10) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - \nSub', fg='black', bg='Light Gray', 
				command=lambda: press("-"), height=3, width=10) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' *\nMulti ', fg='black', bg='Light Gray', 
					command=lambda: press("*"), height=3, width=10) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / \nDiv', fg='black', bg='Light Gray', 
					command=lambda: press("/"), height=3, width=10) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' =\nEqual ', fg='black', bg='Light Gray', 
				command=equalpress, height=3, width=23) 
	equal.grid(row=1, column=2, columnspan=2, padx=5, pady=5) 

	clear = Button(gui, text='Clear', fg='black', bg='Light Gray', 
				command=clear, height=3, width=22) 
	clear.grid(row=1, column=0, columnspan=2, padx=5, pady=5) 

	Decimal= Button(gui, text='.', fg='black', bg='Light Gray', 
					command=lambda: press('.'), height=3, width=10) 
	Decimal.grid(row=5, column=0, padx=5, pady=5) 
	gui.mainloop() 