import os

def export_hex():
    with open("reverse","rb") as infile, open("dumped","w") as outfile:
        hexdata = infile.read().hex()
        outfile.write(hexdata[::-1])
        infile.close()
        outfile.close()

if __name__ == "__main__":
    export_hex()
    os.popen("python -m hexdump --restore dumped > image.png")
    