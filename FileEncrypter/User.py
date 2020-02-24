from datetime import datetime
from Encrypt import Encrypt
class User:
    userID=-1
    userType=0
    uName=0
    def __init__(self,UID,Utype,Uname):
       self.userID=UID
       self.userType=Utype
       self.uName=Uname

    def encrypt_File(self,encryptObj,cursor):#pass object of Encrypt class
        fName=input("Please enter the file name that you are going to Encrypt:")
        if encryptObj.encrypt(fName)==True:
            fNameinDb=0
            fNameinDb=cursor.execute("SELECT * from En-Files WHERE Fname=%s",(fName))
            if fNameinDb==0:
                cursor.execute("INSERT INTO En_Files (Fname, uids_e) VALUES (%s,%s,%d)",(fName,self.userID))
                cursor.execute("INSERT INTO History (Fname, Ttime,uids_h) VALUES (%s,%s,%d)",(fName,self.getCurrentTime(),self.userID))
            print("File: "+file+" has successfully encrypted, please check File: en_"+file)
            return True
        else:
            return False           
    def decrypt_File(self,encryptObj):#pass object of Encrypt class
        fName=input("Please enter the file name that you are going to Encrypt:")
        if encryptObj.decrypt(fName)==True:
            fNameinDb=0
            fNameinDb=cursor.execute("SELECT * from En-Files WHERE Fname=%s",(fName))
            if fNameinDb==0:
                cursor.execute("INSERT INTO De_Files (Fname, uids_d) VALUES (%s,%s,%d)",(fName,self.userID))
                cursor.execute("INSERT INTO History (Fname, Ttime,uids_h) VALUES (%s,%s,%d)",(fName,self.getCurrentTime(),self.userID))
            print("File: "+file+" has successfully decrypted, please check File: de_"+file)
            return True
        else:
            return False
 #   def doEncrypt(self):append history,check enfiles, if not exists, append
 #   def doDecode(self):append history,check defiles, if not exists, append


    def resetPwd(self,cursor):        
        oldpwdOrSQA=cursor.execute("SELECT Upwd,SQ,SA from Users WHERE User_id=%d",(self.userID))
        while True:
            old=input()
            print("Please enter your current password or security question answer\n"+"Your security question: "+str(oldpwdOrSA[1]))
            if old=="q" or old=="Q":
                return False
            if old==str(oldpwdOrSQA[0]) or old==str(oldpwdOrSQA[2]):
                newpwd=input("Please enter your new password:")
                cursor.execute("UPDATE Users SET Upwd=%s WHERE User_id = %d",(newpwd,self.userID))
                return True
            else: 
                print("Input not correct...Please retry or type Q/q to quit")
            
    def resetSQA(self,cursor):        
        oldpwdOrSQA=cursor.execute("SELECT Upwd,SQ,SA from Users WHERE User_id=%d",(self.userID))
        while True:
            old=input()
            print("Please enter your current password or security question answer\n"+"Your security question: "+str(oldpwdOrSA[1]))
            if old=="q" or old=="Q":
                return False
            if old==str(oldpwdOrSQA[0]) or old==str(oldpwdOrSQA[2]):
                newSQ=input("Please enter your new Secutiry Question:")
                newSA=input("Please enter your answer to this uestion:")
                cursor.execute("UPDATE Users SET SQ=%s,SA=%s WHERE User_id = %d",(newSQ,newSA,self.userID))
                return True
            else: 
                print("Input not correct...Please retry or type Q/q to quit")

    def displayHistory(self,cursor):
        history=cursor.execute("SELECT * from History WHERE uids_h=%d",(self.userID))
        for row in history:
            print("HID "+str(row[0])
                   +"File Name: "+row[1]
                   +"Time: "+row[2])      
    def displayEnFiles(self,cursor):
        eFiles=cursor.execute("SELECT * from En_Files WHERE uids_e=%d",(self.userID))
        for row in eFiles:
            print("Encrypted File Id: "+str(row[0])
                   +"File Name: "+row[1]
                   +"Last Modified Time: "+row[2])  

    def displayDeFiles(self,cursor):
        dFiles=cursor.execute("SELECT * from De_Files WHERE uids_d=%d",(self.userID))
        for row in eFiles:
            print("Decrypted File Id: "+str(row[0])
                   +"File Name: "+row[1]
                   +"Last Modified Time: "+row[2])  

    def getCurrentTime(self,cursor):
       timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       return timestamp
    def displayinfo(self):
        print("UID: "+self.userID)
        print("Username: "+self.uName)
        print("User type: "+self.userType)
