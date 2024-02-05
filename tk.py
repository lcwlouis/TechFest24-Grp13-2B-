import tkinter as tk
import mainOpenAI


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
    prompt += ". Include in the image the text \""
    prompt += captions
    prompt += "\""
    prompt += " in a modern, legible font. "
    print(prompt)

    image_prompts,image_urls,captions=mainOpenAI.generate_advertisement(prompt, number_of_images=1)

    # Display the images and captions
    for i in range(1):
        print("Set ", i+1, ":\n")
        print("Image prompt (debug): ", image_prompts[i])
        print("Image url: ", image_urls[i])
        print(captions[i])

master = tk.Tk()

fields = ["Name of product", "Product description", "Key selling points", "Target audience", "Image style", "Captions"]

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