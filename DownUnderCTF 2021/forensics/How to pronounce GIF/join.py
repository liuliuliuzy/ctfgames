# from PIL import Image

# image_row = 12

# for j in range(1,11):
#     to_image = Image.new('RGB', (300, 300))
#     for i in range(12):
#         from_image = Image.open('./challenge/第{}帧.png'.format(i*10+j))
#         to_image.paste(from_image, (0, 22*i))
#     print('code{}.png'.format(j))
#     to_image.save('code{}.png'.format(j))

from base64 import b16decode, b64decode

p = 'fMV9oYVhYMHJfbjB3P30='
print(b64decode(p))