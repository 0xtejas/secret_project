def export_hex():
    with open("reverse","rb") as infile, open("dumped","w") as outfile:
        hexdata = infile.read().hex()
        outfile.write(hexdata)
        infile.close()
        outfile.close()

def strrev(x):
  return x[::-1]

def reverse_hex():
    with open("dumped","r") as infile, open("image.png","w") as outfile:
        data = infile.read()
        for i in range(len(data)):
            temp = strrev(data[i:i+2])
            outfile.write(temp)

if __name__ == "__main__":
    export_hex()
    reverse_hex()