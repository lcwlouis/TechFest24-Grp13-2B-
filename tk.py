import tkinter as tk
import requests
import json
import os
from openai import OpenAI

OPENAI_API_KEY = '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'
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()
#from IPython.display import Image

# This app uses OpenAI's GPT-4 and DALL-E 3 API to generate the advertisement image and caption based on the user's input.
# It is designed to be an AI Agent, which can generate the advertisement image and captions.
# It will first take the input and pass it through GPT-4 to generate prompts for DALL-E 3 API to generate the final image and then generate the matching caption for the advertisement.

def get_imagePrompt_from_GPT4_API(user_prompt,
                                  previous_prompt="This was the first prompt, ignore this",
                                    model="gpt-4-0125-preview",
                                    ):
        response = client.chat.completions.create(
            model=model,
            messages=[
            {"role": "system", "content": "You are a professional instagram advertisement creating assistant. You are creating a prompt to change the styling of the advertisement image and to pass this to the DALL-E 3 API to generate the final image accounting for previously generated prompts. The user will provide the relevant pointers and description of the product to be advertised and the brand name and styling."},
            {"role": "user", "content": previous_prompt},
            {"role": "user", "content": user_prompt}
            ]
        )

        # ChatCompletion(id='chatcmpl-8okHgtvmH1tgdgxhaziyM7MOgcvu2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='To create an engaging advertisement for ShoeX, considering the unique selling propositions and target audience, the following styling prompt for the DALL-E 3 API would maximize the visual appeal while emphasizing the product\'s features:\n\n---\n\n**Prompt for DALL-E 3 API:**\n\nCreate a vibrant and youthful advertisement image featuring a pair of shoes from the brand \'ShoeX\'. Incorporate elements that reflect the innovative material of the shoes—highlighting that they are both waterproof and breathable. Set the scene in an urban environment reflective of Singapore, with recognizable landmarks subtly integrated to appeal to the student demographic. The shoes should be the focal point, displayed prominently in the center of the composition. \n\nDesign the shoes in a way that showcases the variety of colors available, perhaps by having multiple pairs in the background, but keep one pair in the forefront to draw immediate attention. The material of the shoes should have a distinct texture that suggests high-quality, waterproof, and breathable properties.\n\nInclude dynamic, youthful elements such as splashes of water or air bubbles around the shoes to symbolize their waterproof and breathable nature. The color palette should be bright and appealing, with a modern, stylish font announcing \'ShoeX\' prominently. Ensure the advertisement evokes a sense of innovation, durability, and comfort, targeting the lifestyle of active students in Singapore.\n\nLastly, add a tagline near the bottom or top of the image that reads: "Step into Innovation - Comfort for Every Splash and Dash". Make sure the overall styling resonates with a young, energetic audience, looking for stylish yet practical footwear for their daily activities.\n\n---\n\nThis prompt is designed to generate an image that not only highlights the unique features of ShoeX shoes but also visually communicates the brand\'s appeal to its target audience in a compelling way.', role='assistant', function_call=None, tool_calls=None))], created=1707105008, model='gpt-4-0125-preview', object='chat.completion', system_fingerprint='fp_f084bcfc79', usage=CompletionUsage(completion_tokens=357, prompt_tokens=140, total_tokens=497))

        return response.choices[0].message.content.strip()

def get_image_from_DALL_E_3_API(user_prompt,
                                image_dimension="1024x1024",
                                image_quality="standard",
                                model="dall-e-3",
                                nb_final_image=1):
    response = client.images.generate(
        model=model,
        prompt=user_prompt,
        size=image_dimension,
        quality=image_quality,
        n=nb_final_image,
    )
    image_url = response.data[0].url
    return image_url

def get_caption_from_GPT4_API(dalle_prompt,
                              user_prompt,
                              model="gpt-4-0125-preview",
                              ):
    response = client.chat.completions.create(
        model=model,
        messages=[
          {"role": "system", "content": "You are a professional instagram advertisement creating assistant. You will generate the 200 word captions with key summaries of selling points to be used in the advertisement including the formatting. The user will provide the relevant pointers and description of the product to be advertised and the brand name and styling."},
          {"role": "user", "content": "This is the image prompt" + dalle_prompt},
          {"role": "user", "content": user_prompt}
        ]
    )

    # based on the response we get the caption from the message content
    return response.choices[0].message.content.strip()

# Create a loop to generate 5 prompts and images and captions for the advertisement based on the user input
def generate_advertisement(user_prompt, number_of_images=5):
    image_prompts = []
    captions = []
    image_urls = []
    for i in range(number_of_images):
        if i == 0:
            image_prompt = get_imagePrompt_from_GPT4_API(user_prompt)
        else:
            image_prompt = get_imagePrompt_from_GPT4_API(user_prompt, image_prompts[-1])
        image_prompts.append(image_prompt)
        image_urls.append(get_image_from_DALL_E_3_API(image_prompt))
        captions.append(get_caption_from_GPT4_API(image_prompt, user_prompt))
    return image_prompts, image_urls, captions

# Test image prompt generation
# test_image_prompt = get_imagePrompt_from_GPT4_API("You are advertising a new brand of shoes. The brand name is 'ShoeX'. The shoes are made of a new material that is both waterproof and breathable. The shoes are available in 5 different colors and are designed for students in Singapore.")
# print(test_image_prompt)

# Test image generation
# test_image_url = get_image_from_DALL_E_3_API(test_image_prompt)
# print(test_image_url)


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

    image_prompts,image_urls,captions=generate_advertisement(prompt, number_of_images=1)

    # Display the images and captions
    for i in range(1):
        print("Set ", i+1, ":\n")
        print("Image prompt (debug): ", image_prompts[i])
        print("Image url: ", image_urls[i])
        print(captions[i])

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