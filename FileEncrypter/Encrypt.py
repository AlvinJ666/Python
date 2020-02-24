import os
import sys
import cryptography
from cryptography.fernet import Fernet

class Encrypt:
    def encrypt(self,fName):
        while(True):
            if os.path.isfile(fName)==False:
                print("Error occured, File not exists...")
                return False
            key=Fernet.generate_key()
            
            with open(fName,"rb") as infile:
                inContent=infile.read()
            f=Fernet(key)
            encrypted=f.encrypt(inContent)
            with open(str("en_"+fName),"wb") as outFile:
                outFile.write(key)
                outFile.write(encrypted)
            print("File: "+fName+" has successfully encrypted, please check File: en_"+fName)
            return True
        print("Error occured, may be due to no permission to open...")
        return False

    def decrypt(self,fName):
        while(True):
            if os.path.isfile(fName):
                if os.path.getsize(fName)<=77:
                    print("Error occured, File not exists or Not a valid file to decrypt...")
                    return False
            else:
                print("Error occured, File not exists...")
                return False

            with open(fName,"rb") as infile:
                key=infile.read(44)
                inContent=infile.read()

            f=Fernet(key)
            decrypted=f.decrypt(inContent)
            with open(str("de_"+fName),"wb") as outFile:
                outFile.write(decrypted)
            print("File: "+fName+" has successfully decrypted, please check File: de_"+fName)
            return True
        print("Error occured, may be due to no permission to open...")
        return False
