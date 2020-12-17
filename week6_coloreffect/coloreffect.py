from PIL import Image, ImageFilter

img = Image.open("C:\project\ce\jellyfish.jpg")
# img2 = Image.open('c:\project\ce\Tullips.jpg')

def image_color():
    img.save('c:\project\ce\A.jpg')
    img_copy = img
    r,g,b = img.split()
    img_copy=Image.merge('RGB', (r,b,g))
    img_copy.save('c:\project\ce\B.jpg')
    img_copy=Image.merge('RGB', (b,r,g))
    img_copy.save('c:\project\ce\C.jpg')
    img_copy=Image.merge('RGB', (b,g,r))
    img_copy.save('c:\project\ce\D.jpg')
    img_copy=Image.merge('RGB', (g,r,b))
    img_copy.save('c:\project\ce\E.jpg')
    img_copy=Image.merge('RGB', (g,b,r))
    img_copy.save('c:\project\ce\F.jpg')
    img_copy=Image.merge('RGB', (r,r,b))
    img_copy.save('c:\project\ce\G.jpg')
    img_copy=Image.merge('RGB', (r,r,g))
    img_copy.save('c:\project\ce\H.jpg')
    img_copy=Image.merge('RGB', (b,b,r))
    img_copy.save('c:\project\ce\I.jpg')
    img_copy=Image.merge('RGB', (b,b,g))
    img_copy.save('c:\project\ce\J.jpg')
    img_copy=Image.merge('RGB', (g,g,r))
    img_copy.save('c:\project\ce\K.jpg')
    img_copy=Image.merge('RGB', (g,g,b))
    img_copy.save('c:\project\ce\L.jpg')
    print('출력이 완료되었습니다.')

image_color()


# def self_eval(image, effect, img_save):
#     Image.eval(image, lambda x:x+int(effect)).save(img_save)

# # #img_origin = input('이미지 주소나 이름 : ')
# img_origin = Image.open("C:\project\ce\jellyfish.jpg")
# value = input('더할 값 : ')
# save = input('이미지를 저장할 파일 이름 : ')
# self_eval(img_origin, value, 'C:\\project\\ce\\' + save + ".jpg")


# img4=Image.open('c:\project/ce/new.jpg')
# img5=img.resize(500, 500)

# draw = ImageDraw.draw(img5)
# draw.line((0,0,200,200), fill='yellow').save('c:\project\ce\NEWLINE.jpg')

# imf= img.filter(ImageFilter.CONTOUR)
# imf.save('c:\project\ce\COUNTOUR.jpg')
# imf= img.filter(ImageFilter.SHARPEN)
# imf.save('c:\project\ce\SHARPEN.jpg')
# imf= img.filter(ImageFilter.EMBOSS)
# imf.save('c:\project\ce\EMBOSS.jpg')


# imf= img.filter(ImageFilter.MaxFilter(5))
# imf.save('c:\project\ce\MaxFilter.jpg')
# imf= img.filter(ImageFilter.MinFilter(5))
# imf.save('c:\project\ce\MinFilter.jpg')


# imf=img.filter(ImageFilter.MedianFilter(5))
# imf.save('c:\project\ce\MedianFilter.jpg')

# imf= img.filter(ImageFilter.BLUR)
# imf.save('c:\project\ce\inf.jpg')
# img3 = Image.open('c:\project\ce\inf.jpg')
# imf2=img3.filter(ImageFilter.BLUR)
# imf.save('c:\project\ce\inf2.jpg')
# img.convert('1').save('c:\project\ce\mow.jpg')
# img.convert('L').save('c:\project\ce\low.jpg')
# img.convert('CMYK').save('c:\project\ce\wow.jpg')

# Image.eval(img, lambda x:255-x).save('c:\project\ce\convert.jpg')

# Image.eval(img2, lambda x:x-64).save('c:\project\ce\dark.jpg')

# Image.eval(img, lambda x:x+64).save('c:\project\ce\white1.jpg')
# Image.eval(img, lambda x:x+128).save('c:\project\ce\white2.jpg')


# a = img.resize((500, 500))
# b = img2.resize((500, 500))
# c=Image.blend(a,b,0.5)
# c.save('c:\project\ce\Tullipsandjellyfish.jpg')

# img.paste('Red', (100, 150, 200, 300))
# img.save('c:\project\ce\Redbox_jellyfish.jpg')

# img_box = img.crop((100, 100, 300, 300))
# img_box.save('c:\project\ce\Box_jellyfish.jpg')


# flip_top_jellyfish = img.transpose(Image.FLIP_TOP_BOTTOM)
# flip_top_jellyfish.save('c:\project\Flip_top_jellyfish.jpg')


# 이미지 출력
# img.show()

# 이미지 속성 정보 보여주기
# print(img.mode)
# print(img.size)
# print(img)

# 이미지 크기 조정
# s=img.resize((300,225))
# print(s.size)
# s.save("c:\project\ce\jellyfish_copy.jpg")

# 이미지 크기 조정 + 회전
# img.resize((100,100)).rotate(30).save("c:\project\ce\jellyfish_resize_rotate.jpg")


