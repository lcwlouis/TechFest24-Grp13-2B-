import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()

fields = ["Name of product", "Product description", "Key selling points", "Target audience", "Design style"]

for i in range(len(fields)):
    tk.Label(master, text=fields[i]).grid(row=i)

name = tk.Entry(master)
prod_desc = tk.Entry(master)
key_pts = tk.Entry(master)
tar_aud = tk.Entry(master)
des_sty = tk.Entry(master)

params = [name, prod_desc, key_pts, tar_aud, des_sty]

for i in range(len(params)):
    params[i].grid(row=i, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=len(params), 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=len(params), 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()