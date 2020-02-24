
from User import User
class Suser(User):

    def __init__(self,UID,Utype,Uname):
        super(Suser,self).__init__(UID,Utype,Uname)

    def encrypt_File(self,encryptObj):#pass object of Encrypt class
        while(True):
            fNames=[]
            fName=read("Please enter the file names that you are going to Encrypt, Q/q to stop entering:")
            if fName!="q" and fName!="Q":
                fNames.append(fName)
            else:
                 break     
        for file in fNames:
            if encryptObj.encrypt(file)==True:
                fNameinDb=0
                fNameinDb=cursor.execute("SELECT * from En-Files WHERE Fname=%s",(file))
                if fNameinDb==0:
                    cursor.execute("INSERT INTO En_Files (Fname, Ttime, uids_e) VALUES (%s,%s,%d)",(file,self.getCurrentTime(),self.userID))
                    cursor.execute("INSERT INTO History (Fname, Ttime,uids_h) VALUES (%s,%s,%d)",(file,self.getCurrentTime(),self.userID))              
                print("File: "+file+" has successfully encrypted, please check File: en_"+file)
                     

    def decrypt_File(self,encryptObj):#pass object of Encrypt class
        while(True):
            fNames=[]
            fName=read("Please enter the file names that you are going to Encrypt, Q/q to stop entering:")
            if fName!="q" and fName!="Q":
                fNames.append(fName)
            else:
                 break     
        for file in fNames:
            if encryptObj.decrypt(file)==True:
                fNameinDb=0
                fNameinDb=cursor.execute("SELECT * from De-Files WHERE Fname=%s",(file))
                if fNameinDb==0:
                    cursor.execute("INSERT INTO De_Files (Fname, Ttime, uids_d) VALUES (%s,%s,%d)",(file,self.getCurrentTime(),self.userID))
                    cursor.execute("INSERT INTO History (Fname, Ttime,uids_h) VALUES (%s,%s,%d)",(file,self.getCurrentTime(),self.userID))              
                print("File: "+file+" has successfully decrypted, please check File: de_"+file)
    def displayHistory(self,cursor):
        pass

    def displayEnFiles(self,cursor):
        pass

    def displayDeFiles(self,cursor):
        pass

    def getCurrentTime(self,cursor):
       pass

    def resetSQA(self,cursor):
        pass
    
    def resetPwd(self,cursor):  
        pass
    def displayinfo(self):
        pass
