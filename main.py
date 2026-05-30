import cv2
import math

ASCII_CHARS_BLOCK = " ░▒▓█"
ASCII_CHARS_NORMAL = ".:-=+*#%@"
ASCII_CHARS_IMPACT = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


print("-------ASCII ARK GENERATOR---------")
print("If you want to use sample, type s and press enter")
path = input("Enter the path: ")
if path == "s":
    print("You selected sample.jpg")
    path = "./sample.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = gray.shape
print("This photos ratio is (width:height)" + str(width) + ":" + str(height))
question = input("Would you like to change a size? [y/n]: ")
if question == "y" or question == "Y":
    try:
        new_width = math.ceil(int(input("Type a new width: ")))
    except ValueError:
        print("Error was occurred")
        new_width = width
    ratio = math.ceil(width / height)
    factor = float(input("Input a correction factor (normal=0.55): "))
    new_height = math.ceil(height * (new_width / width) * factor)
else:
    new_width = width
    new_height = height



def image_to_ascii(gray, width, height):
    resized_image = cv2.resize(gray, (width, new_height))

    pixels = resized_image.flatten().astype(int)

    print("1: " + ASCII_CHARS_NORMAL)
    print("2: " + ASCII_CHARS_BLOCK)
    print("3: " + ASCII_CHARS_IMPACT)
    choose = input("Choose characters: ")
    if choose == "1":
        num_chars = len(ASCII_CHARS_NORMAL)
        ascii_str = "".join([ASCII_CHARS_NORMAL[pixel * num_chars // 256] for pixel in pixels])
        ascii_image = "\n".join(ascii_str[i:(i + width)] for i in range(0, len(ascii_str), width))
        print(ascii_image)
    elif choose == "2":
        num_chars = len(ASCII_CHARS_BLOCK)
        ascii_str = "".join([ASCII_CHARS_BLOCK[pixel * num_chars // 256] for pixel in pixels])
        ascii_image = "\n".join(ascii_str[i:(i + width)] for i in range(0, len(ascii_str), width))
        print(ascii_image)
    elif choose == "3":
        num_chars = len(ASCII_CHARS_IMPACT)
        ascii_str = "".join([ASCII_CHARS_IMPACT[pixel * num_chars // 256] for pixel in pixels])
        ascii_image = "\n".join(ascii_str[i:(i + width)] for i in range(0, len(ascii_str), width))
        print(ascii_image)


image_to_ascii(gray, new_width, new_height)


