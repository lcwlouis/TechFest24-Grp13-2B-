import tkinter as tk

def generate_prompt():
    prod_name = name.get()
    prod_desc = desc.get()
    key_sell_pts = key_pts.get()
    ta = tar_aud.get()
    des_style = des_sty.get()
    captions = caption.get()
    global prompt
    prompt = "Create an advertisement showcasing " + prod_desc 
    prompt += " of the brand "
    prompt += prod_name
    prompt += " using "
    prompt += des_style
    prompt += " style. The illustration should highlight "
    prompt += key_sell_pts
    prompt += " and appeal to "
    prompt += ta
    prompt += ". It should also contain the captions \""
    prompt += captions
    prompt += "\""
    prompt += " in a modern, legible font. "
    print(prompt)

master = tk.Tk()

fields = ["Name of product", "Product description", "Key selling points", "Target audience", "Design style", "Captions"]

for i in range(len(fields)):
    tk.Label(master, text=fields[i]).grid(row=i)

name = tk.Entry(master)
desc = tk.Entry(master)
key_pts = tk.Entry(master)
tar_aud = tk.Entry(master)
des_sty = tk.Entry(master)
caption = tk.Entry(master)

params = [name, desc, key_pts, tar_aud, des_sty, caption]

for i in range(len(params)):
    params[i].grid(row=i, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=len(params), 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Submit', command=generate_prompt).grid(row=len(params), 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()