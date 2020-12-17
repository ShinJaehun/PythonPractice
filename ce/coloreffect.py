from PIL import Image

img = Image.open("C:\project\coloreffect\jellyfish.jpg")
# img.show()

# print(img.mode)
# print(img.size)
# print(img)

s=img.resize((300,225))

