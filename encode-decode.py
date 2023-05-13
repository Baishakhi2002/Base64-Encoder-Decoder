from tkinter import *
import base64

# initialize window
root = Tk()
root.geometry('1080x780')
root.resizable(0, 0)

# title of the window
root.title("Akash - Message Encode and Decode")

# label

Label(root, text='ENCODE DECODE', font='Times 20 bold', fg='Blue').pack(side=TOP)
Label(root, text='DADDY', font='Times 12 bold', fg='Red').pack(side=BOTTOM)

# define variables

Text = StringVar()
mode = StringVar()
Result = StringVar()


# ######define function#####


# function to encode
def encode(message):
    enc = []
    for i in range(len(message)):
        enc.append(chr((ord(message[i])) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# function to decode
def decode(message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        dec.append(chr((256+ord(message[i])) % 256))

    return "".join(dec)


# Function to exit window
def close():
    root.destroy()


# Function to reset
def reset():
    Text.set("")
    mode.set("")
    Result.set("")


# Function to Select Mode
def selection():
    select = "You selected the option "+str(mode.get())
    label.config(text=select, fg='Red')


S1 = Radiobutton(root, font='Consolas 20 bold', text="base64 encode", variable=mode, value='Encode', command=selection)
S1.pack(side=TOP)

S2 = Radiobutton(root, font='Consolas 20 bold', text="base64 decode", variable=mode, value='Decode', command=selection)
S2.pack(side=TOP)

label = Label(root)
label.pack()


# Function To Result
def r():
    if mode.get() == 'Encode':
        Result.set(encode(Text.get()))

    elif mode.get() == 'Decode':
        Result.set(decode(Text.get()))
    else:
        Result.set('Please Choose A Option')


# ################### Label and Button #############

# Message
Label(root, font='Consolas 20 bold', text='MESSAGE').place(x=300, y=145)
Entry(root, font='Consolas 18', textvariable=Text, bg='ghost white').place(x=430, y=150)

# result
Entry(root, font='Consolas 18 bold', textvariable=Result, bg='ghost white').place(x=430, y=205)

# #####result button
Button(root, font='Consolas 18 bold', text='RESULT', padx=2, bg='LimeGreen', command=r).place(x=300, y=205)

# reset button
Button(root, font='Consolas 18 bold', text='RESET', width=6, command=reset,
       bg='Red', padx=2, pady=2).place(x=480, y=285)

# exit button
Button(root, font='Consolas 18 bold', text='EXIT', width=6, command=close,
       bg='OrangeRed', padx=2, pady=2).place(x=600, y=285)
root.mainloop()
