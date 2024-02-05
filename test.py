import requests
import IPython.display as display

url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sbVINVg1R7udL7OIp3EXpOf3/user-BQLC8qhlzfOvLdEfCqpnzTlt/img-2GbsnQs2IVoH4GT2aVYOZ5hz.png?st=2024-02-05T02%3A52%3A59Z&se=2024-02-05T04%3A52%3A59Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-02-04T11%3A01%3A36Z&ske=2024-02-05T11%3A01%3A36Z&sks=b&skv=2021-08-06&sig=GPBw2av0FHRA61pItZmjPlStGS6rPRN9WNSYQ%2BHYV6k%3D"
display.Image(requests.get(url).content)