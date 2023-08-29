import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
mycursor=mydb.cursor()

def Movies():
    print("Welcome to Search Menu for Movies! : Select the category to Search the data")
    print("1. Reference COde")
    print("2. Title")
    print("3. Ratings")
    print("4. Genre")
    print("5. Director")
    x=0
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        var='Reference_Code'
        val=input("Enter the Reference Code : ")
    elif ch==2:
        var='Title'
        val=input("Enter the Title of the Movie : ")
    elif ch==3:
        var='Ratings'
        val=input("Enter Ratings : ")
    elif ch==4:
        var='Genre'
        val=input("Enter Genre : ")
    elif ch==5:
        var='Director'
        val=input("Enter the Name of the Director : ")
    if x==0:
        sql="select * from Movies where " + var + " = %s" 
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))


def Tv_Shows():
    print("Welcome to Search Menu for Tv Shows! : Select the category to Search the data")
    print("1. Reference Code")
    print("2. Title")
    print("3. Ratings")
    print("4. Year of Release")
    print("5. Number of Seasons")
    print("6. Number of Episodes")
    print("7. Genre")
    print("8. Ongoing")
    x=0
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        var='Reference_Code'
        val=input("Enter the Reference Code : ")
    elif ch==2:
        var='Title'
        val=input("Enter the Title of the Tv Show : ")
    elif ch==3:
        var='Rating'
        val=float(input("Enter Ratings : "))
    elif ch==4:
        var='Year_of_Release'
        val=input("Enter Year of Release : ")
    elif ch==5:
        var='No_of_Seasons'
        val=input("Enter Number of Seasons : ")
    elif ch==6:
        var='Total_No_of_Episodes'
        val=input("Enter Total Number of Episodes : ")
    elif ch==7:
        var='Genre'
        val=input("Enter Genre : ")
    if ch==8:
        var='Ongoing'
        val=input("Is it an Ongoing Tv Show? (Enter True/False) ")
        sql="select * from Tv_Shows where "+var+"="+val+";"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
            x=1
    if x==0:
        sql="select * from Tv_Shows where " + var + " = %s"
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))


def Video_Games():
    print("Display Menu: Select the category to display the data")
    print("1. Reference Code")
    print("2. Title")
    print("3. Ratings")
    print("4. Date of Release")
    print("5. Genre")
    print("6. Developing Company")
    print("7. Platforms")
    x=0
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        var='Reference_Code'
        val=input("Enter the Reference Code : ")
    elif ch==2:
        var='Title'
        val=input("Enter the Title of the Video Game : ")
    elif ch==3:
        var='Ratings'
        val=input("Enter Ratings of the Video Game: ")
    elif ch==4:
        var='Date_of_Release'
        val=input("Enter Date of Release : ")
    elif ch==5:
        var='Genre'
        val=input("Enter Genre of the Video Game: ")
    elif ch==6:
        var='Developing_Company'
        val=input("Enter Name of the Developing Company : ")
    elif ch==7:
        var='Platform'
        val=input("Enter Platform Combination on which it can be played : ")
    if x==0:
        sql="select * from video_games where " + var + " = %s" 
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))


def Anime():
    print("Display Menu: Select the category to display the data")
    print("1. Reference Code")
    print("2. Title")
    print("3. Ratings")
    print("4. Year of Release")
    print("5. Number of Seasons")
    print("6. Number of Episodes")
    print("7. Genre")
    print("8. Ongoing")
    print("9. Creators")
    x=0
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        var='Reference_Code'
        val=input("Enter the Reference Code : ")
    elif ch==2:
        var='Title'
        val=input("Enter the Title of the Anime : ")
    elif ch==3:
        var='Rating'
        val=input("Enter Ratings : ")
    elif ch==4:
        var='Year_of_Release'
        val=input("Enter Year of Release : ")
    elif ch==5:
        var='No_of_Seasons'
        val=input("Enter Number of Seasons : ")
    elif ch==6:
        var='Total_No_of_Episodes'
        val=input("Enter Total Number of Episodes : ")
    elif ch==7:
        var='Genre'
        val=input("Enter Genre : ")
    if ch==8:
        var='Ongoing'
        val=input("Is it an Ongoing Anime? (Enter True/False) ")
        sql="select * from Anime where "+var+"="+val+";"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            x=1
    elif ch==9:
        var='Creators'
        val=input("Enter Name of the Creator : ")
    if x==0:
        sql="select * from Anime where " + var + " = %s" 
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        for x in res:
            print("{}\t\t\t{}\t\t\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))

print("Welcome to Search Menu!")
print("Select one of the below tables")
print("1. Movies")
print("2. Tv Shows")
print("3. Video Games")
print("4. Anime")
a=0
while a==0:
    try:
        userInput=int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") #Print New Line
    if(userInput == 1):
        Movies()
    elif(userInput == 2):
        Tv_Shows()
    elif(userInput == 3):
        Video_Games()
    elif(userInput == 4):
        Anime()
    trmn=input("Do you want to continue? (To exit the program type 'No') : ")
    if trmn=='No':
        print("Thank you for using Search Menu!")
        a=a+1
    else:
        continue
