
# script that uses the OpenAI API to generate images based on user input and saves them to a local directory

# from openai import OpenAI
# from requests import get
# import os

# bias = 'add a bunny'

# def ai(query):
#     client = OpenAI()
#     response = client.images.generate(
#     model="dall-e-3",
#     prompt=query,
#     n=1,
#     size="1024x1024" 
#     )

#     return response

# while True:
#     query = input('Image to Create: ')
#     query = f'{query} {bias}'
#     os.system('clear')
#     response = ai(query)
#     pic_name = f'{response.created}.png'

#     response_image = get(response.data[0].url)
#     with open(pic_name, 'wb') as file:
#         file.write(response_image.content)

#     with open('gallery.html', 'a') as gallery:
#         gallery.write(f'<img style="height:200px; width:auto;" src="{pic_name}">')
    
#     print(query)
#     print(response_image)





import os
import uuid
from openai import OpenAI
from requests import get

bias = 'add a bunny'

def generate_image(query):
    try:
        client = OpenAI()
        response = client.images.generate(
            model="dall-e-3",
            prompt=query,
            n=1,
            size="1024x1024"
        )
        return response
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def save_image(response):
    pic_name = f"{uuid.uuid4()}.png"
    response_image = get(response.data[0].url)
    with open(pic_name, 'wb') as file:
        file.write(response_image.content)
    return pic_name

def generate_gallery_html(image_files):
    with open('gallery.html', 'w') as gallery:
        gallery.write("<html><body>")
        for image_file in image_files:
            gallery.write(f'<img style="height:200px; width:auto;" src="{image_file}">')
        gallery.write("</body></html>")

def main():
    image_files = []
    while True:
        query = input('Image to Create: ')
        if not query:
            print("Please enter a valid input")
            continue
        query = f'{query} {bias}'
        os.system('clear')
        response = generate_image(query)
        if response:
            pic_name = save_image(response)
            image_files.append(pic_name)
            generate_gallery_html(image_files)
            print(query)
            print(f"Image saved as {pic_name}")

if __name__ == "__main__":
    main()