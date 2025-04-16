import tkinter as tk

def convert(C):
    C = float(C) 
    F=(C*9/5)+32
    return F

def cel():
    C = entry_c.get() 
    result = convert(C)
    label_r.config(text=f"Result: {result}")


Root=tk.Tk()
Root.title("Celsius to Fehrenheit")
Root.geometry("400x200")

label_c=tk.Label(Root, text="Enter Celsius")
label_c.grid(row=0, column=0, padx=5, pady=5)

entry_c=tk.Entry(Root, width=10)
entry_c.grid(row=0, column=1, pady=5, padx=5)

cvt_button=tk.Button(Root, text="Convert", command=cel)
cvt_button.grid(row=1, column=0, pady=10)

label_r=tk.Label(Root, text="result")
label_r.grid(row=2, column=0, pady=10)

Root.mainloop()


