
import os
import json
from S_user import Suser
class Admin(Suser):
    
    def __init__(self,UID,Utype,Uname):
        super(Suser,self).__init__(UID,Utype,Uname)

    def displayUsersInfo(self,cursor):
        users=cursor.execute("SELECT * from Users WHERE User_id=%d",(self.userID))
        for row in users:
            print("ID "+str(str(row[0])
                   +"User Type: "+str(row[1])
                   +"User Name: "+str(row[2])
                   +"User password: "+str(row[3])
                   +"Security Question: "+str(row[4])
                   +"Answer to SQ: "+str(row[5])))
        print("\n")

    def proDemoteUser(self,user,cursor):
        uname=input("Please enter the user name to promote/demote")
        utype=cursor.execute("SELECT Utype from Users WHERE Uname=%s",(uname))
        toUpdate=0
        if str(utype)=='s':
            toUpdate='u'
        elif str(utype)=='u':
            toUpdate='s'
        else:
            print("Error occured...")
            return False
        cursor.execute("INSERT INTO Users (Uname) VALUES(%s) ON DUPLICATE KEY UPDATE Utype=%s",(self.userID,toUpdate))
        if str(utype)=='s':
            print("User: "+uname+" has been demoted.")
        elif str(utype)=='u':
            print("User: "+uname+" has been promoted.")
        print("\n")
        return True

    def displayOneUserHistory(self,cursor):      
        uname=input("Please enter the user name to display history")
        history=cursor.execute("SELECT Fname,Ttime from History WHERE uids_h IN (SELECT User_id FROM User Where Uname=%s)",(uname))
        for row in history:
            print("File Name: "+str(row[0])
                   +"Process Time: "+str(row[1]))
        print("\n")

    def displayOneUserEnFiles(self):
        uname=input("Please enter the user name to display his encrypted files")
        efiles=cursor.execute("SELECT Fname from En_Files WHERE uids_e IN (SELECT User_id FROM User Where Uname=%s)",(uname))
        for row in efiles:
            print("File Name: "+str(row))
        print("\n")

    def displayOneUserDeFiles(self):
        uname=input("Please enter the user name to display his encrypted files")
        dfiles=cursor.execute("SELECT Fname from De_Files WHERE uids_d IN (SELECT User_id FROM User Where Uname=%s)",(uname))
        for row in dfiles:
            print("File Name: "+str(row))
        print("\n")

    def displayUsers(self):
        if self.loaded==True:
            option=input('Do you want to show user passwords and security Q&A as well? y/n')    
            for userd in self.jsonf:
                if option=='y' or option=='Y':
                    print('id: '+userd['id']
                          +"   utype: "+userd['utype']
                          +"   uname: "+userd['uname']
                          +"   upassword: "+userd['upassword']
                          +"   usq: "+userd['sq']
                          +"   usa: "+userd['sa'])
            print("\n")
        else:
            print("Please load user info at first...\n")

    def makeUpdates(self,cursor):    
        while(True):
            uname=input("Please enter the user name to make updates or Q/q to quit:")
            if uname==str(cursor.execute("SELECT Uname from Users WHERE Uname=%s",(uname))):
                field=input("Enter to make update for specific field:\n"
                    +"1:Username\n"
                    +"2:User Password"
                    +"3:User Security Question"
                    +"4:User Security Answer"
                    +"5:Delete user"
                    +"Q/q: quit")
                if field=="1" or field=="Username":
                    newuname=input("Enter new user name:")
                    cursor.execute("UPDATE Users SET Uname=%s WHERE Uname=%s",(newuname,uname))
                    print("Done...")
                    break
                if field=="2" or field=="User Password":
                    upwd=input("Enter new user password:")
                    cursor.execute("UPDATE Users SET pwd=%s WHERE Uname=%s",(upwd,uname))
                    print("Done...")
                    break
                if field=="3" or field=="User Security Question":
                    nsq=input("Enter new user security question:")
                    cursor.execute("UPDATE Users SET SQ=%s WHERE Uname=%s",(nsq,uname))
                    print("Done...")
                    break
                if field=="4" or field=="User Security Answer":
                    nsa=input("Enter new user security answer:")
                    cursor.execute("UPDATE Users SET SA=%s WHERE Uname=%s",(nsa,uname))
                    print("Done...")
                    break
                if field=="5" or field=="Delete user":
                    cursor.execute("DELETE FROM Users WHERE Uname=%s",(uname))
                    print("Done...")
                    break
                elif field=="q" or field=="Q":
                    break
            elif uname=="q" or uname=="Q":
                break
            return True
        
        
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
