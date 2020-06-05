from tkinter import *

import DB_operation
#Building a GUI window to make an order

def widgets_create():
	global root
	global size
	global dough_ty
	global toppings #ingridients

	widgets = []
	Size_radio_buttons = []
	dough_t = []
	ingridients = [] #toppings

	#labels creation
	headline = Label(root, text="Make an Order", font="Arial 22 bold")
	size_label = Label(root, text="Size:", font="Arial 12 bold")
	dough_type_label = Label(root, text="type:", font="Arial 12 bold")
	Ingridients_label = Label(root, text="Ingridients:", font="Arial 12 bold")
	submit_button = Button(root, text="submit:", padx=30, pady=10, bg="yellow", command=submit_form)

	#pizza size buttons
	L = Radiobutton(root, text="L", variable=size, value="L")
	M = Radiobutton(root, text="M", variable=size, value="M")
	S = Radiobutton(root, text="S", variable=size, value="S")

	#dough type
	deep_dish = Radiobutton(root, text="Deep dish", variable=dough_type, value="Deep dish")
	fluffy = Radiobutton(root, text="fluffy", variable=dough_type, value="fluffy")
	neapolitan = Radiobutton(root, text="neapolitan", variable=dough_type, value="neapolitan")

	#Ingridients 
	
	mushroom = Checkbutton(root, text="mushroom", variable=toppings[0], onvalue="mushroom", offvalue="")
	ham = Checkbutton(root, text="ham", variable=toppings[1], onvalue="ham", offvalue="")
	tomato = Checkbutton(root, text="tomato", variable=toppings[2], onvalue="tomato", offvalue="")

	onion = Checkbutton(root, text="onion", variable=toppings[3], onvalue="onion", offvalue="")
	chicken = Checkbutton(root, text="chicken", variable=toppings[4], onvalue="chicken", offvalue="")
	pepper = Checkbutton(root, text="pepper", variable=toppings[5], onvalue="pepper", offvalue="")

	tuna = Checkbutton(root, text="tuna", variable=toppings[6], onvalue="tuna", offvalue="")
	corn = Checkbutton(root, text="corn", variable=toppings[7], onvalue="corn", offvalue="")
	olives  = Checkbutton(root, text="olives", variable=toppings[8], onvalue="olives", offvalue="")

	
	#Labels appending

	widgets.append(headline)
	widgets.append(size_label)
	widgets.append(dough_type_label)
	widgets.append(Ingridients_label)
	widgets.append(submit_button)

	#SIZE Radiobuttons appendig
	Size_radio_buttons.append(L)
	Size_radio_buttons.append(M)
	Size_radio_buttons.append(S)

	#dough type appending
	dough_t.append(deep_dish)
	dough_t.append(fluffy)
	dough_t.append(neapolitan)

	#Ingridients appending
	ingridients.append(mushroom)
	ingridients.append(ham)
	ingridients.append(tomato)

	ingridients.append(onion)
	ingridients.append(chicken)
	ingridients.append(pepper)

	ingridients.append(tuna)
	ingridients.append(corn)
	ingridients.append(olives)
	
	return widgets, Size_radio_buttons, dough_t, ingridients


#Getting data from form and assigning data to database



def submit_form():
	global size, dough_type, toppings
	ordered_toppings = []
	#filtering toppings list
	for i in toppings:
		if i.get() != "":
			ordered_toppings.append(i.get())

	
	print("size: ", size.get())
	print("type: ", dough_type.get())
	print("toppings", ordered_toppings)
	print(" ")

	clear_widgets()

	def convert_toppings_to_string(ordered_toppings):
		toppings_in_text = ""
		for top in ordered_toppings:
			toppings_in_text += top +"; "
		print(toppings_in_text)
		return toppings_in_text
		

	ordered_toppings = convert_toppings_to_string(ordered_toppings)
	#values to send to DB
	sql_size = str(size.get())
	sql_type = str(dough_type.get())

	#toppings are actually in string

	DB_operation.sent_DB(sql_size, sql_type, ordered_toppings)

def clear_widgets():
	global toppings
	for x in toppings:
		x.set("")


root = Tk()
root.title("Pizza ordering")

#radio buttons vars
size = StringVar()
size.set("S")

dough_type = StringVar()
dough_type.set("fluffy")

#toppings checkbuttons vars
toppings=[]
for i in range(9):
	toppings.append(StringVar())


widgets = widgets_create()[0]
size_buttons = widgets_create()[1]
dough_buttons = widgets_create()[2]
ingridients = widgets_create()[3]

#headline
widgets[0].grid()

#Size grid
widgets[1].grid(row=2, column=0)
size_buttons[2].grid(row=2, column=1)
size_buttons[1].grid(row=2, column=2)
size_buttons[0].grid(row=2, column=3)

#dough_type
widgets[2].grid(row=3, column=0)
dough_buttons[0].grid(row=3, column=1)
dough_buttons[1].grid(row=3, column=2)
dough_buttons[2].grid(row=3, column=3)

#Break Line

break_line = Label(root, text=" ")
break_line.grid(row=4)

#Ingridients
widgets[3].grid(row=5, columnspan=3, sticky=W)

ingridients[0].grid(row=6, column=1, sticky=W)
ingridients[1].grid(row=7, column=1, sticky=W)
ingridients[2].grid(row=8, column=1, sticky=W)

ingridients[3].grid(row=6, column=2, sticky=W)
ingridients[4].grid(row=7, column=2, sticky=W)
ingridients[5].grid(row=8, column=2, sticky=W)

ingridients[6].grid(row=6, column=3, sticky=W)
ingridients[7].grid(row=7, column=3, sticky=W)
ingridients[8].grid(row=8, column=3, sticky=W)

#Submit button
widgets[4].grid(row=9, column=3, sticky=E)


root.mainloop()



