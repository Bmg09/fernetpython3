import os
from cryptography.fernet import Fernet #importing cryptography lib
#creating file list where we store the file name list inside a
#directory
files = []
for file in os.listdir():
    #checking if the current file is itself or the key file or the decryptfile else it will also encrypt those again
    #we dont want that to happen
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
#using "thekey.key" in readbinary and store in a variable for decryption 
secretkey = ""
with open("thekey.key","rb") as thekey:
    secretkey = thekey.read()

myphrase = "varun460"

secretphrase = input("Enter secretphrase:\n")

if secretphrase == myphrase:
    #opening files reading those files in a variable called as "content" and decrypting those contents using the above key 
    #and writing backed decrypted contents to the same file
    for file in files:
        with open(file,"rb") as thefiles:
            content = thefiles.read()
        contents_decrypted = Fernet(secretkey).decrypt(content)
        with open(file,"wb") as thefiles:
            thefiles.write(contents_decrypted)
    print('decrypted')
else:
    print('try harder next time')

