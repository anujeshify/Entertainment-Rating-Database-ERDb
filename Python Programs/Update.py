import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
mycursor=mycon.cursor()

def UpdateMovie():
    Ref_code=str(input("Enter a 4 digit reference code (Include it in quoutes \" \"):"))
    fld=input("Enter the field which you want to edit : ")
    print("Select one of the options")
    print("1. Update an existing value to new value")
    print("2. Update an existing vlaue to a NULL value")
    n2=int(input("Enter a choice : "))
    if n2==1:
       newval=input("Enter the value you want to set (Include it in quoutes \" \"):")
       sql="Update Movies set " + fld +"=" + newval + " where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Movies where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t\t{}\t{}\t{}\t{}\t\t{}\t\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7]))
           mycon.commit()
    elif n2==2:
       sql="Update Movies set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Movies where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t\t{}\t{}\t{}\t{}\t\t{}\t\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7]))
           mycon.commit()

def UpdateTvshow():
    Ref_code=str(input("Enter a 4 digit reference code (Include it in quoutes \" \"):"))
    fld=input("Enter the field which you want to edit : ")
    print("Select one of the options")
    print("1. Update an existing value to new value")
    print("2. Update an existing vlaue to a NULL value")
    n2=int(input("Enter a choice : "))
    if n2==1:
       newval=input("Enter the value you want to set (Include it in quoutes \" \"):")
       sql="Update Tv_Shows set " + fld +"=" + newval + " where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Tv_Shows where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
           mycon.commit()
    elif n2==2:
       sql="Update Tv_Shows set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Tv_Shows where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
           mycon.commit()

def UpdateVideoGames():
    Ref_code=str(input("Enter a 4 digit reference code (Include it in quoutes \" \"):"))
    fld=input("Enter the field which you want to edit : ")
    print("Select one of the options")
    print("1. Update an existing value to new value")
    print("2. Update an existing vlaue to a NULL value")
    n2=int(input("Enter a choice : "))
    if n2==1:
       newval=input("Enter the value you want to set (Include it in quoutes \" \"):")
       sql="Update Video_Games set " + fld +"=" + newval + " where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Video_Games where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
           mycon.commit()
    elif n2==2:
       sql="Update Video_Games set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Video_Games where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
           mycon.commit()

def UpdateAnime():
    Ref_code=str(input("Enter a 4 digit reference code (Include it in quoutes \" \"):"))
    fld=input("Enter the field which you want to edit : ")
    print("Select one of the options")
    print("1. Update an existing value to new value")
    print("2. Update an existing vlaue to a NULL value")
    n2=int(input("Enter a choice : "))
    if n2==1:
       newval=input("Enter the value you want to set (Include it in quoutes \" \"):")
       sql="Update Anime set " + fld +"=" + newval + " where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Anime where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8]))
           mycon.commit()
    elif n2==2:
       sql="Update Anime set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Anime where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       for j in res:
           print("{}\t\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}\t\t{}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8]))
           mycon.commit()

print("Welcome to Update Menu!")
print("1. Update Movies")
print("2. Update Tv Shows")
print("3. Update Video Games")
print("4. Update Anime")
n1=int(input("Enter any one of the above choices : "))
if n1==1:
       UpdateMovie()
elif n1==2:
   UpdateTvshow()
elif n1==3:
   UpdateVideoGames()
elif n1==4:
   UpdateAnime()
   
