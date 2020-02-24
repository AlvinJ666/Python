import pyodbc
from Admin import Admin
from User import User
from S_user import Suser
from Encrypt import Encrypt

def createUser(cursor):
    while True:
        username=input("Give a username to your account: ")
        unmdb=cursor.execute("Select Uname from Users where Uname=%s",usernamee)
        if username==unmdb:
            print("Sorry, this username has been taken, please pick another one...")
        else:
            break
    upwd=0
    while True:
        upwd=input("Give a password to your account: ")
        if len(upwd)<=8:
            print("Password is too short, should be no less than 8 characters...")
        else:
            break
    usq=input("Please give a security question to your account: ")
    usa=input("Please give an answer for your security question: ")
    cursor.execute("insert into Users (Uname,Upwd,SQ,SA,Utype) values(%s,%s,%s,%s,%s)",(username,upwd,usq,usa,"u"))
    return True
def login(cursor):
    uname=input("Enter your username: ")
    uinfo=cursor.execute("Select * from Users where Uname=%s",uname)
    if uname!=str(uinfo[2]):
        create=input("User not exists, do you want to create one?\nEnter Y/y to continue or any other key to return to the menu:")
        if create=='Y' or create=='y':
            createUser(cursor)
    else:
        upwd=input("Enter the password: ")
        if upwd==str(uinfo[1]):
            if str(uinfo[3])=='u':
                newone=User(str(uinfo[0]),str(uinfo[3]),str(uinfo[2]))
            elif str(uinfo[3])=='s':
                newone=Suser(str(uinfo[0]),str(uinfo[3]),str(uinfo[2]))
            elif str(uinfo[3])=='a':
                newone=Admin(str(uinfo[0]),str(uinfo[3]),str(uinfo[2]))
            return newone
    return False

def pmenu():   
     print('1: log in;\n'
          +'2: create a user;\n'
          +'3: reset password;\n'
          +'4: reset security question and answer;\n'
          +'5: log in as admin;\n'
          +'6: type 6/“bye”/Q/q to quit the program\n');
     opt=input("Enter your option: ");
     return opt

def pUsubmenu():   
     print('1: Encrypt file/files;\n'
          +'2: Decrypt file/files;\n'
          +'3: check profile;\n'
          +'4: check history;\n'
          +'5: check encrypted files;\n'
          +'6: check decrypted files;\n'
          +'7: type 7/logout/Q/q to return to the main menu\n');   
     opt=input("Enter your option: ");
     return opt

def pAsubmenu():   
     print('1: Encrypt files;\n'
          +'2: Decrypt files;\n'
          +'3: promote/demote a user;\n'
          +'4: check one user history;\n'
          +'5: check one user encrypted files;\n'
          +'6: check one user decrypted files;\n'
          +'7: check own encrypted files;\n'
          +'8: check own decrypted files;\n'
          +'9: check own history;\n'
          +'10: check users list\n'
          +'11: make other updates\n'
          +'0: quit\n');   
     opt=input("Enter option: ");
     return opt

if __name__ == "__main__":

    cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:cs-server666.database.windows.net,1433;Database=FileEncryption;Uid=alvin;Pwd={pwd};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = cnxn.cursor()
    encrypt=Encrypt()
    user=0
    ulogin=False
    while True:       
        opt=pmenu()        
        #adm.loadUserInfo()
        if opt=='1':
            user=login(cursor)
            if user!=False and (isinstance(user,User) or isinstance(user,Suser))  :
                ulogin=True
                while True:
                    optu=pumenu()
                    if optu=='1':
                        torf=user.encrypt_File(encrypt)
                        if torf==True:
                            cnxn.commit()
                    elif optu=='2':
                        torf=user.decrypt_File(encrypt)
                        if torf==True:
                            cnxn.commit()
                    elif optu=='3':
                        user.displayinfo()
                    elif optu=='4':
                        user.displayHistory(cursor)
                    elif optu=='5':
                        user.displayEnFiles(cursor)
                    elif optu=='6':
                        user.displayDeFiles(cursor)
                    elif optu=='7' or optu=='logout' or optu=='Q' or optu=='q':
                        user=0
                        ulogin=False
                        break
        elif opt=='2':
            created=createcreateUser(cursor)
            if created==True:
                cnxn.commit()
        elif opt=='3':
            if ulogin==True:
                reset=user.resetPwd(cursor)
                if reset==True:
                    cnxn.commit()
            else:
                user=login(cursor)
                if user!=False:
                    reset=user.resetPwd(cursor)
                if reset==True:
                    cnxn.commit()
        elif opt=='4':
            if ulogin==True:
                reset=user.resetSQA(cursor)
                if reset==True:
                    cnxn.commit()
            else:
                user=login(cursor)
                if user!=False:
                    reset=user.resetSQA(cursor)
                if reset==True:
                    cnxn.commit()
        elif opt=='5':
            adm=login(cursor)
            if isinstance(adm,Admin):
                while True:
                    if optu=='1':
                        adm.encrypt_File(encrypt)
                    elif optu=='2':
                        adm.decrypt_File(encrypt)                        
                    elif optu=='3':
                        done=adm.proDemoteUser(cursor)
                        if done==True:
                            cnxn.commit()
                    elif optu=='4':
                        adm.displayOneUserHistory(cursor)
                    elif optu=='5':
                        adm.displayOneUserEnFiles(cursor)
                    elif optu=='6':
                        adm.displayOneUserDeFiles(cursor)
                    elif optu=='7':
                        adm.displayEnFiles(cursor)
                    elif optu=='8':
                        adm.displayDeFiles(cursor)
                    elif optu=='9':
                        adm.displayHistory(cursor)
                    elif optu=='10':
                        adm.displayUsers(cursor)
                    elif optu=='11':
                        done=adm.makeUpdates(cursor)
                        if done==True:
                            cnxn.commit()
                    elif optu=='0' or optu=='logout' or optu=='Q' or optu=='q':
                        break  
            else:
                adm=0
        elif opt=='7' or opt=='bye'or opt=='Q'or opt=='q':
            break
