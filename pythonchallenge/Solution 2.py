Z=[]
k=[]
Q="K78m)hm=|cwsXhbH}uq5w4sJbPrw6"
def xor(inp):
    st=[]
    for i in range (len(inp)):
        st.append(chr(ord(inp[i])^1))
    return(''.join(st))
def shift(inp):
    for i in range(len(inp)):
        if(i<11):
            Z.append(chr(ord(inp[i])-i-5))
        else:
            Z.append(chr(ord(inp[i])-4))      
    return(''.join(Z))

X="K78m)hm=|cwsXhbH}uq5w4sJbPrw6"

k=xor(shift(X))

print("Flag: shaktictf{"+k+"}")


# I've renamed the function for my convenience.