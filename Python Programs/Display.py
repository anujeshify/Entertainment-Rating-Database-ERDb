import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
mycursor=mydb.cursor()

print("Welcome to Display Menu!")
print("Select one of the below tables")
print("1. Movies")
print("2. Tv Shows")
print("3. Video Games")
print("4. Anime")
a=0
while a==0:
    from tabulate import tabulate
    userInput=int(input("Please Select An Above Option: "))
    if(userInput == 1):
        sql="select * from Movies;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Runtime','Genre','Director','Cast'])
        print(t)
    elif(userInput == 2):
        sql="select * from Tv_Shows;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
        print(t)
    elif(userInput == 3):
        sql="select * from video_games;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Genre','Developing_Company','Platforms'])
        print(t)
    elif(userInput == 4):
        sql="select * from Anime;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
        print(t)
    trmn=input("Do you want to continue? (To exit the program type 'No') : ")
    if trmn=='No':
        print("Thank you for using Display Menu!")
        a=a+1
    else:
        continue
