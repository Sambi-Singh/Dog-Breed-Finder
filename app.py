import requests
from PIL import Image
import io

#To output images from an api, need Pillow library (PIL) Image module and io
#.get(imageUrl, accepting byte streams) will give you the iamge content
#in Image.open() you can only read files and thus it needs a path to work with, since the content
# of the image is just numbers we about to use io.BytesIO() to make a file object out of those
# numbers, this way our image can be opened without any issues happening
 
#Changing API!

headers = {
    "Content-Type": "application/json",
    "x-api-key": "live_TTOtPXQPFGZjBSfECkRVqfTUkGz5u3d7wXh0aZYXhaZ9YuEH7PQbBn0BD1NtjdmF"
}

response = requests.get("https://api.thedogapi.com/v1/images/search", headers=headers)
print(response.status_code)
print(response.json())
print(f"This dogs name is {response.json()[0]["breeds"][0]["name"]}")
#print(response.json()["breeds"][0]["name"])
breed_list = requests.get("https://dog.ceo/api/breeds/list/all")
if(breed_list.status_code == 200):
    print("WOrking!")
endpoint = requests.get("https://dog.ceo/api/breeds/image/random")
if endpoint.json()["status"] == "success":
    urlImage = endpoint.json()["message"]
    #img = Image.open(urlImage)
    #Get the image content, in bytes
    #stream, handles when data from the response object is read to the file, by default its
    # not done immeidatley, but if True then will automatically download content to file,
    # very useful for streaming, processing huge images, checking header content, etc.
    
    img_content = requests.get(urlImage, stream=True) #Hold response OBEJCT! Headers, Status code, etc!
    img = Image.open(io.BytesIO(img_content.content)) #.content gets us a sequence of bytes
    img.show()
    print(urlImage)
    #print(f"Dog breed name: {}")