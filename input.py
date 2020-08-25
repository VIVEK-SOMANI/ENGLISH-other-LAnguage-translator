text=""
while(True):
    z=input()
    if(z==":q" or z=="exit()"):
        break
    text= text+z+'\n'
print(text)
