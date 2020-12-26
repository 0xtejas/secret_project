from PIL import Image

header, trailer = 2*"11001100",2*"0101010100000000"
res=""

def decrypt(img):

    pixels, mode = list(Image.Image.getdata(img)), img.mode
    for i in range(len(pixels)):
        newPixel = list(pixels[i])
        findLSB(newPixel[i%len(mode)])
        
def findLSB(target):

    binary = str(bin(target))[2:]
    global res
    res+=binary[-1]

img = Image.open("Secret.png")
decrypt(img)

pos = res.find(trailer)
res=res[len(header):pos]

for i in range(0,len(res),8):
    print(chr(int(res[i:i+8], 2)),end="")