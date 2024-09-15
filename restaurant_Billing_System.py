from tkinter import *
from tkinter import messagebox
import random, os, tempfile
from ttkwidgets.autocomplete import AutocompleteCombobox
from prettytable import PrettyTable

foodQuantities = [
     {},
     {},
     {}
]


entriesName=[
    {},
    {},
    {}
]

nameAndPrice =[
    {
        "Butter Chicken Bliss": 350,
        "Rogan Josh Delight": 400,
        "Paneer Tikka Masala": 320,
        "Lamb Biryani Royale": 450,
        "Chole Bhature Feast": 180,
        "Malai Kofta Majesty": 300,
        "Dal Makhani Supreme": 250,
        "Shahi Paneer Delight": 340,
        "Chicken Tandoori": 360,
        "Goan Fish Curry": 420,
        "Grilled Salmon Elegance": 550,
        "Beef Stroganoff Supreme": 480,
        "Chicken Alfredo Delight": 380,
        "Vegetable Lasagna": 350,
        "Lamb Shank Splendor": 520
    },
    {
        "Burger": 150,
        "Pizza": 300,
        "Sandwich": 120,
        "French Fries": 80,
        "Hot Dog": 130,
        "Chicken Nuggets": 150,
        "Fried Chicken": 180,
        "Veg Wrap": 100,
        "Cheese Nachos": 140,
        "Chicken Wings": 170,
        "Mozzarella Sticks": 160,
        "Quesadilla": 150,
        "Tacos": 140,
        "Buffalo Wings": 180,
        "Garlic Bread": 110,
        "Corn Dog": 120,
        "Loaded Fries": 130,
        "Milkshake": 120,
        "Soft Pretzel": 100
    },
    {
        "Coca-Cola": 60,
        "Pepsi": 60,
        "Sprite": 60,
        "Fanta": 60,
        "Lemonade": 70,
        "Iced Tea": 70,
        "Coffee": 80,
        "Espresso": 90,
        "Latte": 100,
        "Cappuccino": 100,
        "Hot Chocolate": 90,
        "Green Tea": 70,
        "Smoothie": 130,
        "Juice (Orange)": 80,
        "Juice (Apple)": 80,
        "Mineral Water": 50,
        "Sparkling Water": 70,
        "Mocktail": 140,
        "Beer": 150,
        "Wine": 250,
        "Corn Dog": 120,
        "Loaded Fries": 130,
        "Soft Pretzel": 100

    }
]
nameList=[list(nameAndPrice[0].keys()),list(nameAndPrice[1].keys()),list(nameAndPrice[2].keys())]

# Combine all keys from each dictionary into a single list
options = [key for category in nameAndPrice for key in category.keys()]


def pTable():
    table = PrettyTable()
    table.field_names = ['s.no', 'name', 'quantity', 'price']
    # Add rows to the table
    j = 1
    for i in range(3):
        for key, value in foodQuantities[i].items():
            if key in nameAndPrice[i]:  # Ensure the key exists in dictionary p
                total = value * nameAndPrice[i][key]
                table.add_row([j, key, value, total])
                j += 1

    # Customize the table appearance
    table.vertical_char = ' '  # Set vertical separator to a space
    table.horizontal_char = '-'  # Set horizontal separator (optional)
    table.junction_char = '-'  # Set junction (cross) character to a space

    # Align columns
    table.align['s.no'] = 'l'  # Right align
    table.align['name'] = 'l'  # Left align
    table.align['quantity'] = 'r'  # Right align
    table.align['price'] = 'r'  # Right align

    # Set max width for columns
    table.max_width['s.no'] = 1  # Fix width of the s.no column
    table.max_width['name'] = 14  # Fix width of the name column
    table.max_width['quantity'] = 8  # Fix width of the quantity column
    table.max_width['total_price'] = 5  # Fix width of the total_price column

    return table

def clearItem():
    for i in range(3):
        for key in foodQuantities[i]:
            entriesName[i][key].delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    firstCategoryPriceEntry.delete(0,END)
    secondCategoryPriceEntry.delete(0,END)
    thirdCategoryPriceEntry.delete(0,END)
    taxEntry.delete(0,END)
    totalBillEntry.delete(0,END)
    combobox.delete(0,END)
    quantityEntry.delete(0,END)
    searchBillEntry.delete(0,END)
    for items in foodQuantities:
        items.clear()



def total():
    totalFood = 0
    totalDrink = 0
    totalCake = 0

    for category in range(len(entriesName)):
        for entry in entriesName[category]:
            foodNameEntry = entriesName[category][entry]
            try:
                quantity = int(foodNameEntry.get())
            except ValueError:
                quantity = 0

            if quantity > 0:
                totalFood += quantity*nameAndPrice[category][entry]
                foodQuantities[category][entry] = quantity
            # if category == 0:
            #     totalFood += quantity*nameAndPrice[category][entry]
            #     if quantity > 0:
            #         foodQuantities[0][entry] = quantity
            # elif category == 1:
            #     totalDrink += quantity*nameAndPrice[category][entry]
            #     if quantity > 0:
            #         foodQuantities[1][entry] = quantity
            # elif category == 2:
            #     totalCake += quantity*nameAndPrice[category][entry]
            #     if quantity > 0:
            #         foodQuantities[2][entry] = quantity

    firstCategoryPriceEntry.delete(0, END)
    firstCategoryPriceEntry.insert(0, f'{totalFood}')

    secondCategoryPriceEntry.delete(0, END)
    secondCategoryPriceEntry.insert(0, f'{totalDrink}')

    thirdCategoryPriceEntry.delete(0, END)
    thirdCategoryPriceEntry.insert(0, f'{totalCake}')

    global totalAmount, tax
    tax = (totalFood + totalDrink + totalCake) * 0.05
    totalAmount = totalFood + totalDrink + totalCake + tax

    taxEntry.delete(0,END)
    taxEntry.insert(0,f'{tax} RS')

    totalBillEntry.delete(0,END)
    totalBillEntry.insert(0,f'{totalAmount} RS')

def save_bill():
    global billNumber
    result = messagebox.askyesno("Configure","Do You Want To Save The Bill?")
    if result:
        bill_content=textArea.get(1.0,END)

        if not os.path.exists('bills'):   # check bill file is present or not if not then create
            os.mkdir('bills')

        file=open(f'bills/{billNumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number: {billNumber} is saved successfully')
        billNumber=random.randint(1000,10000)
        clearItem()


def billArea():
    total()
    textArea.delete(1.0, END)
    if nameEntry.get()=="" or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif firstCategoryPriceEntry.get()=='' and secondCategoryPriceEntry.get()=='' and thirdCategoryPriceEntry.get()=='':
        messagebox.showerror('Error','First Press Total Button')
    elif firstCategoryPriceEntry.get()=='0' and secondCategoryPriceEntry.get()=='0' and thirdCategoryPriceEntry.get()=='0':
        messagebox.showerror('Error','No Product Are Selected')
    else:
        textArea.insert(END, '\t     ** Welcome Customer **\n')
        textArea.insert(END, f'Bill Number: {billNumber}\n')
        textArea.insert(END, f'Customer Name: {nameEntry.get()}\n')
        textArea.insert(END, f'Customer Phone Number: {phoneEntry.get()}\n')
        textArea.insert(END, f'{pTable()}\n')  # function inside calculation file
        textArea.insert(END, f'tax:\t\t\t{tax}\n')
        textArea.insert(END, f'Total Amount:\t\t\t{totalAmount}\n')
        save_bill()


#Frontend
def closeWindow():
    root.destroy()


def searchBill():
    if searchBillEntry.get()=='':
        messagebox.showerror('Error', 'Please Enter Bill Number')
    else:
        for i in os.listdir('bills/'):
            if i.split('.')[0]==searchBillEntry.get():
                f=open(f'bills/{i}','r')
                textArea.delete(1.0,END)
                for data in f:
                    textArea.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror('Error',f' Bill Number {searchBillEntry.get()} not found')


def clearTextArea():
    textArea.delete(1.0,END)
    clearItem()


def printBill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill Not Found')
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')

def addToCart():
    q = quantityEntry.get()
    itemName = combobox.get()

    if itemName=='':
        messagebox.showerror('error', f'please select item')
    elif q=='':
        messagebox.showerror('error', f'please enter quantity   ')
    elif itemName in options:
        for disses in entriesName:
            if itemName in disses:
                disses[itemName].delete(0,END)
                disses[itemName].insert(0, q)

    # elif itemName in nameList[0]:
    #     entriesName[0][itemName].delete(0,END)
    #     entriesName[0][itemName].insert(0,q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    # elif itemName in nameList[1]:
    #     entriesName[1][itemName].delete(0, END)
    #     entriesName[1][itemName].insert(0,q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    # elif itemName in nameList[2]:
    #     entriesName[2][itemName].delete(0, END)
    #     entriesName[2][itemName].insert(0, q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    else:
        messagebox.showerror('error',f'{itemName} is not found')


root = Tk()
root.title("Billing System")
root.geometry("1370x800")
root.overrideredirect(True)


bgColor = 'grey20'
fColor = 'times new roman'
labelWidth=16
billNumber=random.randint(1000,10000)

headingFrame = LabelFrame(root)
headingFrame.pack(fill=X)
headingLabel = Label(headingFrame, text="Billing System", font=("Helvetica", 30, 'bold')
                     , bg=bgColor, fg='gold', bd=7, relief=GROOVE)
headingLabel.pack(fill=X)

closeButton = Button(headingLabel,text="X",font=('arial', 16, 'bold'), bg="red", fg='white', bd=3,command=closeWindow)
closeButton.pack(side=RIGHT)


# FRAME Customer details
customer_details_frame = LabelFrame(root, text='Customer Details', font=(fColor, 15, 'bold'),
                                    bg=bgColor, fg='gold', bd=5)
customer_details_frame.pack(fill=X, pady=3)

nameLabel = Label(customer_details_frame, text='Name', font=(fColor, 15, 'bold')
                  , fg='white', bg=bgColor)
nameLabel.grid(row=0, column=0, padx=20, pady=2)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=2, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabelLabel = Label(customer_details_frame, text='Mobile', font=(fColor, 15, 'bold')
                        , fg='white', bg=bgColor)
phoneLabelLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=2, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

searchBillLabel = Label(customer_details_frame, text='Search Bill', font=(fColor, 15, 'bold')
                   , fg='white', bg=bgColor)
searchBillLabel.grid(row=0, column=4, padx=(290, 20), pady=2)

searchBillEntry = Entry(customer_details_frame, font=('arial', 15), bd=2, width=18)
searchBillEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='Search', font=('arial', 12, 'bold'), bg="blue", fg="white", bd=0,
                      highlightthickness=0,command=searchBill)
searchButton.grid(row=0, column=6, padx=8)


##Frame search items
searchItemFrame = LabelFrame(root, text='Items', font=(fColor, 20, 'bold'),  bg=bgColor, fg='gold', bd=0)
searchItemFrame.pack(fill=X)

searchItemLabel = Label(searchItemFrame,text='Search Item:', font=(fColor, 15, 'bold') , fg='white', bg=bgColor)
searchItemLabel.grid(row=0, column=0, padx=20, pady=2)

def addToCart():
    q = quantityEntry.get()
    itemName = combobox.get()

    if itemName=='':
        messagebox.showerror('error', f'please select item')
    elif q=='':
        messagebox.showerror('error', f'please enter quantity   ')
    elif itemName in options:
        for disses in entriesName:
            if itemName in disses:
                disses[itemName].delete(0,END)
                disses[itemName].insert(0, q)
                messagebox.showinfo('Success', f' {itemName} is added successfully')

    # elif itemName in nameList[0]:
    #     entriesName[0][itemName].delete(0,END)
    #     entriesName[0][itemName].insert(0,q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    # elif itemName in nameList[1]:
    #     entriesName[1][itemName].delete(0, END)
    #     entriesName[1][itemName].insert(0,q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    # elif itemName in nameList[2]:
    #     entriesName[2][itemName].delete(0, END)
    #     entriesName[2][itemName].insert(0, q)
    #     messagebox.showinfo('Success', f' {itemName} is added successfully')
    else:
        messagebox.showerror('error',f'{itemName} is not found')
def on_select(event):
    global selected_option
    selected_option = combobox.get()


combobox = AutocompleteCombobox(searchItemFrame, completevalues=options,height=30)
combobox.bind("<<ComboboxSelected>>",on_select )
combobox.grid(row=0,column=1,padx=20,pady=2)

quantityEntry = Entry(searchItemFrame, font=('arial', 10), bd=1, width=5)
quantityEntry.grid(row=0, column=2, padx=20, pady=2, ipady=1)

addToCartButton = Button(searchItemFrame, text='Add to Cart', font=('arial', 10, 'bold'), bd=0, highlightthickness=0,
                        bg="blue", fg="white", command=addToCart)
addToCartButton.grid(row=0,column=3,padx=20,pady=2)

##FRAME items
itemsFrame = LabelFrame(root)
itemsFrame.pack(fill=X,pady=0)

def label(frame):
    def fillFrame(j):
        i=0
        for key in nameList[j]:
            labelName = Label(frame, text=nameList[j][i], font=(fColor, 15, 'bold'), fg='white',
                              bg=bgColor, width=labelWidth, anchor='w')
            labelName.grid(row=i, column=0, pady=8, padx=10)

            entriesName[j][nameList[j][i]] = Entry(frame,font=('arial', 13), bd=5, width=3)
            entriesName[j][nameList[j][i]].grid(row=i, column=1, padx=20, pady=8, sticky='e')
            i+=1
    if frame==first_frame:
        fillFrame(0)
    elif frame==Second_frame:
        fillFrame(1)
    else:
        fillFrame(2)


#FRAME first

first_item_frame = LabelFrame(itemsFrame, text='Main Course', font=(fColor, 15, 'bold'), bg=bgColor, fg='gold', bd=5)
first_item_frame.grid(row=0, column=0)

canvas1 = Canvas(first_item_frame, bg=bgColor, width=290, height=410)
canvas1.pack(side=LEFT, fill=BOTH, expand=True)

itemsScrollbar = Scrollbar(first_item_frame, orient=VERTICAL, command=canvas1.yview)
itemsScrollbar.pack(side=RIGHT, fill=Y)

first_frame = Frame(canvas1, bg=bgColor)

# Configure the canvas to work with the scrollbar
canvas1.create_window((0, 0), window=first_frame, anchor='nw')
canvas1.config(yscrollcommand=itemsScrollbar.set)

# Bind the third_frame to resize when the canvas changes
first_frame.bind("<Configure>", lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))

label(first_frame)


#second frame

second_item_frame = LabelFrame(itemsFrame, text='Fast-Food', font=(fColor, 15, 'bold'), bg=bgColor, fg='gold', bd=5)
second_item_frame.grid(row=0, column=1)


canvas2 = Canvas(second_item_frame, bg=bgColor, width=290, height=410)
canvas2.pack(side=LEFT, fill=BOTH, expand=True)

itemsScrollbar = Scrollbar(second_item_frame, orient=VERTICAL, command=canvas2.yview)
itemsScrollbar.pack(side=RIGHT, fill=Y)

Second_frame = Frame(canvas2, bg=bgColor)

# Configure the canvas to work with the scrollbar
canvas2.create_window((0, 0), window=Second_frame, anchor='nw')
canvas2.config(yscrollcommand=itemsScrollbar.set)

# Bind the third_frame to resize when the canvas changes
Second_frame.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

label(Second_frame)


#FRAME third

third_item_frame = LabelFrame(itemsFrame, text='Beverage', font=(fColor, 15, 'bold'), bg=bgColor, fg='gold', bd=5)
third_item_frame.grid(row=0, column=2)


canvas3 = Canvas(third_item_frame, bg=bgColor, width=290, height=410)
canvas3.pack(side=LEFT, fill=BOTH, expand=True)

itemsScrollbar = Scrollbar(third_item_frame, orient=VERTICAL, command=canvas3.yview)
itemsScrollbar.pack(side=RIGHT, fill=Y)

third_frame = Frame(canvas3, bg=bgColor)

# Configure the canvas to work with the scrollbar
canvas3.create_window((0, 0), window=third_frame, anchor='nw')
canvas3.config(yscrollcommand=itemsScrollbar.set)

# Bind the third_frame to resize when the canvas changes
third_frame.bind("<Configure>", lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

label(third_frame)

# Function to scroll one frame at a time
def _on_mouse_wheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")



# Bind the mouse scroll event to each canvas individually
canvas1.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", lambda event: _on_mouse_wheel(event, canvas1)))
canvas2.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", lambda event: _on_mouse_wheel(event, canvas2)))
canvas3.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", lambda event: _on_mouse_wheel(event, canvas3)))

# Unbind the mouse scroll when the cursor leaves the canvas
canvas1.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))
canvas2.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))
canvas3.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))

#FRAME billing area
billingAreaFrame = Frame(itemsFrame, bd=8, relief=GROOVE)
billingAreaFrame.grid(row=0, column=3)

billingAreaLabel = Label(billingAreaFrame, text='Billing Area',font=('times new roman', 15, 'bold')
                         , bd=7, relief=GROOVE)
billingAreaLabel.pack(fill=X)

billingScrollbar = Scrollbar(billingAreaFrame,orient=VERTICAL)
billingScrollbar.pack(side=RIGHT, fill=Y)
textArea = Text(billingAreaFrame, height=21, width=45, yscrollcommand=billingScrollbar.set)
textArea.pack()
billingScrollbar.config(command=textArea.yview)

##FRAME BILL MENU
billMenuFrame = LabelFrame(root, text='Bill Menu', font=(fColor, 15, 'bold'), bg=bgColor, fg='gold', bd=5)
billMenuFrame.pack(fill='both', expand=True)

#first column
firstCategoryPriceLabel = Label(billMenuFrame, text='Main Course Price', font=(fColor, 14, 'bold'), fg='white', bg=bgColor)
firstCategoryPriceLabel.grid(row=0, column=0, padx=20, pady=0,sticky='w')

firstCategoryPriceEntry = Entry(billMenuFrame, font=('arial', 10), bd=5, width=20,)
firstCategoryPriceEntry.grid(row=0, column=1, padx=20, pady=0)

secondCategoryPriceLabel = Label(billMenuFrame, text='Fast-Food Price', font=(fColor, 14, 'bold'), fg='white', bg=bgColor)
secondCategoryPriceLabel.grid(row=1, column=0, padx=20, pady=0,sticky='w')

secondCategoryPriceEntry = Entry(billMenuFrame, font=('arial', 10), bd=5, width=20)
secondCategoryPriceEntry.grid(row=1, column=1, padx=20, pady=0)

thirdCategoryPriceLabel = Label(billMenuFrame, text='Beverage', font=(fColor, 14, 'bold'), fg='white', bg=bgColor)
thirdCategoryPriceLabel.grid(row=2, column=0, padx=20, pady=0,sticky='w')

thirdCategoryPriceEntry = Entry(billMenuFrame, font=('arial', 10), bd=5, width=20)
thirdCategoryPriceEntry.grid(row=2, column=1, padx=20, pady=0)


####


totalFrame = Frame(billMenuFrame, bd=0, bg=bgColor,relief=GROOVE)
totalFrame.grid(row=0, column=2, rowspan=3)

taxLabel = Label(totalFrame, text='Tax',font=(fColor, 14, 'bold'), fg='white', bg=bgColor)
taxLabel.grid(row=0, column=0, padx=20, pady=0,sticky='w')

taxEntry = Entry(totalFrame, font=('arial', 12), bd=5, width=14)
taxEntry.grid(row=0, column=1, padx=20, pady=4)

totalBillLabel = Label(totalFrame,text='Total Bill',font=(fColor, 18, 'bold'), fg='white', bg=bgColor)
totalBillLabel.grid(row=1, column=0, padx=20, pady=0,sticky='w')

totalBillEntry = Entry(totalFrame,font=('arial', 17), bd=5, width=10)
totalBillEntry.grid(row=1, column=1, padx=20, pady=4)

#FRAME button
buttonFrame = Frame(billMenuFrame, bd=6, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButtton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg=bgColor, fg='white',
                      bd=5, width=12,pady=17, command=total)
totalButtton.grid(row=0,column=0,padx=4)

billButtton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg="green", fg='white',
                     bd=5, width=12,pady=17,command=billArea)
billButtton.grid(row=0,column=1,padx=4)

PrintButtton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg="red", fg='white',
                      bd=5, width=8,pady=17, command=printBill)
PrintButtton.grid(row=0,column=2,padx=4)

ClearButtton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg="orange", fg='white',
                      bd=5, width=8,pady=17, command=clearTextArea)
ClearButtton.grid(row=0,column=3,padx=4)

root.mainloop()



