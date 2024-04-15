from PIL import Image
#str to binary
def str2bin(input):
    byte_array = input.encode()
    binary_int = int.from_bytes(byte_array, "big")
    text = bin(binary_int)
    return text
c=str2bin("hamid")
print(c)
#binary to str
def bin2str(bin_data):
    binary_int = int(bin_data, 2)
    byte_number = (binary_int.bit_length()+7)//8
    binary_array = binary_int.to_bytes(byte_number,"big")
    string = binary_array.decode()
    return string

z = bin2str(c)
print(z)
def Hide():
    i = 0
    data = str2bin("hamid")
    data = data[2:len(data)]
    with Image.open("869681.png") as img:
        width,height = img.size
        for x in range(0,width):
            for y in range(0,height):
                pixel = list(img.getpixel((x,y)))
                for n in range (0,3):
                    if (i<len(data)):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i+=1
                    img.putpixel((y,x), tuple(pixel))
                img.save("steg-LOGO","PNG")
Hide()
