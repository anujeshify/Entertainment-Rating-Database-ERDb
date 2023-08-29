from tabulate import tabulate
print("Welcome to ERDB database")
def main_menu():
    print("The  following operations can be done on this database.")
    print("1.Display table data")
    print("2.Update any table")
    print("3.Search any table")
    print("4.Insert new record")
    print("5.Delete any record")
    print("6.Exit")
    r=int(input("Enter number corresponding to your choice"))
    if r==1:
        Display()
    elif r==2:
        Update()
    elif r==3:
        Search()
    elif r==4:
        Insert()
    elif r==5:
        Delete()
    elif r==6:
        exit()
    else:
        print("Enter appropriate number!!!")
        main_menu()

def Display():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mydb.cursor()
    print("Welcome to Display Menu!")
    print("Select one of the below tables")
    print("1. Movies")
    print("2. Tv Shows")
    print("3. Video Games")
    print("4. Anime")
    print("5.Go back to main menu")
    try:
        userInput=int(input("Please Select An Above Option: ")) 
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")
    if(userInput == 1):
        sql="select * from Movies;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Runtime','Genre','Director','Cast'])
        print(t)
        b=int(input("Enter 1 if you want to go back to the display menu,2 if you want to go back to the main menu or any other number to exit the program"))
        if b==1:
            Display()
        elif b==2:
            main_menu()
        else:
            exit()
    elif(userInput == 2):
        sql="select * from Tv_Shows;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
        print(t)
        b=int(input("Enter 1 if you want to go back to the display menu,2 if you want to go back to the main menu or any other number to exit the program"))
        if b==1:
            Display()
        elif b==2:
            main_menu()
        else:
            exit()
    elif(userInput == 3):
        sql="select * from video_games;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Genre','Developing_Company','Platforms'])
        print(t)
        b=int(input("Enter 1 if you want to go back to the display menu,2 if you want to go back to the main menu or any other number to exit the program"))
        if b==1:
            Display()
        elif b==2:
            main_menu()
        else:
            exit()
    elif(userInput == 4):
        sql="select * from Anime;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
        print(t)
        b=int(input("Enter 1 if you want to go back to the display menu,2 if you want to go back to the main menu or any other number to exit the program"))
        if b==1:
            Display()
        elif b==2:
            main_menu()
        else:
            exit()
    elif(userInput==5):
        main_menu()
        

def Update():
    print("Welcome to Update Menu!")
    print("1. Update Movies")
    print("2. Update Tv Shows")
    print("3. Update Video Games")
    print("4. Update Anime")
    print("5. Go back to Main menu")
    n1=int(input("Enter any one of the above choices : "))
    if n1==1:
        UpdateMovie()
    elif n1==2:
        UpdateTvshow()
    elif n1==3:
        UpdateVideoGames()
    elif n1==4:
        UpdateAnime()
    elif n1==5:
        main_menu()
    
def UpdateMovie():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    Ref_code=str(input("Enter a 4 digit reference code (Include it in quoutes \" \"):"))
    fld=input("Enter the field which you want to edit : ")
    print("Select one of the options")
    print("1. Update an existing value to new value")
    print("2. Update an existing vlaue to a NULL value")
    n2=int(input("Enter a choice : "))
    if n2==1:
       newval=input("Enter the value you want to set(Include it in quoutes \" \") :")
       sql="Update Movies set " + fld +"=" + newval + " where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Movies where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Runtime','Genre','Director','Cast'])
       print(t)
       mycon.commit()
    elif n2==2:
       sql="Update Movies set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Movies where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Runtime','Genre','Director','Cast'])
       print(t)
       mycon.commit()
    h=int(input("Enter 1 if you want to update more records in the same table, 2 if you want to go to the update menu to select some other table,3 if you want to go back to the main menu and any other number to exit the program."))
    if h==1:
        UpdateMovie()
    elif h==2:
        Update()
    elif h==3:
        main_menu()
    else:
        exit()

def UpdateTvshow():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
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
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
       print(t)
       mycon.commit()
    elif n2==2:
       sql="Update Tv_Shows set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Tv_Shows where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
       print(t)
       mycon.commit()
    h=int(input("Enter 1 if you want to update more records in the same table, 2 if you want to go to the update menu to select some other table,3 if you want to go back to the main menu and any other number to exit the program."))
    if h==1:
        UpdateTvshow()
    elif h==2:
        Update()
    elif h==3:
        main_menu()
    else:
        exit()

def UpdateVideoGames():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
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
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Genre','Developing_Company','Platforms'])
       print(t)
       mycon.commit()
    elif n2==2:
       sql="Update Video_Games set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Video_Games where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Genre','Developing_Company','Platforms'])
       print(t)
       mycon.commit()
    h=int(input("Enter 1 if you want to update more records in the same table, 2 if you want to go to the update menu to select some other table,3 if you want to go back to the main menu and any other number to exit the program."))
    if h==1:
        UpdateVideoGames()
    elif h==2:
        Update()
    elif h==3:
        main_menu()
    else:
        exit()

def UpdateAnime():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
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
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
       print(t)
       mycon.commit()
    elif n2==2:
       sql="Update Anime set " + fld +"= NULL where Reference_Code=" + Ref_code + ";"
       mycursor.execute(sql)
       print("Editing Done: ")
       print("After correction the record is : ")
       sql="select * from Anime where Reference_Code=" + Ref_code + ";"    
       mycursor.execute(sql)
       res=mycursor.fetchall()
       t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
       print(t)
       mycon.commit()
    h=int(input("Enter 1 if you want to update more records in the same table, 2 if you want to go to the update menu to select some other table,3 if you want to go back to the main menu and any other number to exit the program."))
    if h==1:
        UpdateAnime()
    elif h==2:
        Update()
    elif h==3:
        main_menu()
    else:
        exit()

def Search():
    print("Welcome to Search Menu!")
    print("Select one of the below tables")
    print("1. Movies")
    print("2. Tv Shows")
    print("3. Video Games")
    print("4. Anime")
    print("5. Go back to Main menu")
    try:
        userInput=int(input("Please Select An Above Option: "))
    except ValueError:
            exit("\nHy! That's Not A Number") 
    else:
        print("\n")
    if(userInput == 1):
        SMovies()
    elif(userInput == 2):
        STv_Shows()
    elif(userInput == 3):
        SVideo_Games()
    elif(userInput == 4):
        SAnime()
    elif(userInput==5):
        main_menu()

def SMovies():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mydb.cursor()
    print("Welcome to Search Menu for Movies! : Select the category to Search the data")
    print("1. Reference Code")
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
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Runtime','Genre','Director','Cast'])
        print(t)
    z=int(input("Enter 1 if you want to search more records in this table,2 if you want to go back to search menu, 3 if you want to go all the way back to main menu and any other number to exit the program."))
    if z==1:
        SMovies()
    elif z==2:
        Search()
    elif z==3:
        main_menu()
    else:
        exit()
                
                
def STv_Shows():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mydb.cursor()
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
        var='Ratings'
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
        val=input("Is it an Ongoing Tv Show? (Enter True/False) ")
        sql="select * from Tv_Shows where "+var+"="+val+";"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
        print(t)
    if x==0:
        sql="select * from Tv_Shows where " + var + " = %s"
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_Of_Release','No_of_Seasons','Total_No_of_Episodes','Genre','Ongoing'])
        print(t)
    z=int(input("Enter 1 if you want to search more records in this table,2 if you want to go back to search menu, 3 if you want to go all the way back to main menu and any other number to exit the program."))
    if z==1:
        STv_Shows()
    elif z==2:
        Search()
    elif z==3:
        main_menu()
    else:
        exit()

def SVideo_Games():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mydb.cursor()
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
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Date_Of_Release','Genre','Developing_Company','Platforms'])
        print(t)
    z=int(input("Enter 1 if you want to search more records in this table,2 if you want to go back to search menu, 3 if you want to go all the way back to main menu and any other number to exit the program."))
    if z==1:
        SVideo_Games()
    elif z==2:
        Search()
    elif z==3:
        main_menu()
    else:
        exit()
def SAnime():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mydb.cursor()
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
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
        print(t)
    elif ch==9:
        var='Creators'
        val=input("Enter Name of the Creator : ")
    if x==0:
        sql="select * from Anime where " + var + " = %s" 
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        t=tabulate(res, headers=['Reference_Code','Title','Ratings','Year_of_Release','No_of_Seasons','Total_No_of_Seasons','Genre','Creators','Ongoing'])
        print(t)
    z=int(input("Enter 1 if you want to search more records in this table,2 if you want to go back to search menu, 3 if you want to go all the way back to main menu and any other number to exit the program."))
    if z==1:
        SAnime()
    elif z==2:
        Search()
    elif z==3:
        main_menu()
    else:
        exit()

def Insert():    
       print("welcome to Insert Menu:")
       print("Enter number corresponding to the table to which record has to be inserted:")
       print("Tables:")
       print("1.Movies")
       print("2.Tv Shows")
       print("3.Video Games")
       print("4.Anime")
       print("5.Go back to Main menu")
       s=int(input())
       if s==1:
           insrtmovie()
       elif s==2:
           insrtshow()
       elif s==3:
            insrtgame()
       elif s==4:
            insrtanime()
       elif s==5:
            main_menu()

def insrtmovie():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    Ref_code=str(input("Enter a 4 digit reference code with a hash at the beginning:"))
    Title=str(input("Enter Title of the movie:"))
    Ratings=float(input("Enter rating out of 10:"))
    date_of_release=str(input("Enter date of release in yyyy-mm-dd format:"))
    Runtime=str(input("Enter runtime:"))
    Genre=str(input("Enter Genre:"))
    Director=str(input("Enter the name of the Director:"))
    Cast=str(input("Enter Cast:"))
    val=(Ref_code,Title,Ratings,date_of_release,Runtime,Genre,Director,Cast)
    sql="insert into movies(Reference_Code,Title,Ratings,Date_Of_Release,Runtime,Genre,Director,Cast) values(%s,%s,%s,%s,%s,%s,%s,%s);"
    try:
        mycursor.execute(sql,val)
        mycon.commit()
        print(mycursor.rowcount,"Record Added!!")
    except:
        print("Error encountered!!Try using a different reference code.")
    e=int(input("Enter 1 if you want to insert more records into this table, 2 if you want to go back to insert menu,3 if you want to go all the way back to main menu and any other number to exit the program."))
    if e==1:
        insrtmovie()
    elif e==2:
        Insert()
    elif e==3:
        main_menu()
    else:
        exit()
def insrtshow():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    Ref_code=str(input("Enter a 4 digit reference code with a hash at the beginning:"))
    Title=str(input("Enter Title of the Tv Show:"))
    Ratings=float(input("Enter rating out of 10:"))
    year_of_release=int(input("Enter Year of Release:"))
    nos=int(input("Enter Number of Seasons:"))
    noe=int(input("Enter Total Number of Episodes:"))
    Genre=str(input("Enter Genre:"))
    ongoing=int(input("If the show is ongoing, enter 1 otherwise enter 0"))
    val=(Ref_code,Title,Ratings,year_of_release,nos,noe,Genre,ongoing)
    sql="insert into tv_shows(Reference_Code,Title,Rating,Year_of_Release,No_of_seasons,Total_No_of_episodes,Genre,Ongoing) values(%s,%s,%s,%s,%s,%s,%s,%s);"
    try:
        mycursor.execute(sql,val)
        mycon.commit()
        print(mycursor.rowcount,"Record Added!!")
    except:
        print("Error encountered!!Try using a different reference code.")
    e=int(input("Enter 1 if you want to insert more records into this table, 2 if you want to go back to insert menu,3 if you want to go all the way back to main menu and any other number to exit the program."))
    if e==1:
        insrtshow()
    elif e==2:
        Insert()
    elif e==3:
        main_menu()
    else:
        exit()
def insrtgame():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    Ref_code=str(input("Enter a 4 digit reference code with a hash at the beginning:"))
    Title=str(input("Enter Title of the Game:"))
    Ratings=float(input("Enter rating out of 10:"))
    Dor=str(input("Enter Date of Release in yyyy-mm-dd format:"))
    Genre=str(input("Enter Genre:"))
    DevCo=str(input("Enter Developing Company Name:"))
    pfm=str(input("Enter various platforms:"))
    val=(Ref_code,Title,Ratings,Dor,Genre,DevCo,pfm)
    sql="insert into video_games(Reference_Code,Title,Ratings,Date_Of_Release,Genre,Developing_Company,Platform) values(%s,%s,%s,%s,%s,%s,%s);"
    try:
        mycursor.execute(sql,val)
        mycon.commit()
        print(mycursor.rowcount,"Record Added!!")
    except:
        print("Error encountered!!Try using a different reference code.")
    e=int(input("Enter 1 if you want to insert more records into this table, 2 if you want to go back to insert menu,3 if you want to go all the way back to main menu and any other number to exit the program."))
    if e==1:
        insrtgame()
    elif e==2:
        Insert()
    elif e==3:
        main_menu()
    else:
        exit()
def insrtanime():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    Ref_code=str(input("Enter a 4 digit reference code with a hash at the beginning:"))
    Title=str(input("Enter Title of the Anime:"))
    Ratings=float(input("Enter rating out of 10:"))
    year_of_release=int(input("Enter Year of Release:"))
    nos=int(input("Enter Number of Seasons:"))
    noe=int(input("Enter Total Number of Episodes:"))
    Genre=str(input("Enter Genre:"))
    cr=str(input("Enter Names of Creators:"))
    ongoing=int(input("If the show is ongoing, enter 1 otherwise enter 0"))
    val=(Ref_code,Title,Ratings,year_of_release,nos,noe,Genre,cr,ongoing)
    sql="insert into anime(Reference_Code,Title,Rating,Year_of_Release,No_of_seasons,Total_No_of_episodes,Genre,Creators,Ongoing) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    try:
        mycursor.execute(sql,val)
        mycon.commit()
        print(mycursor.rowcount,"Record Added!!")
    except:
        print("Error encountered!!Try using a different reference code.")
    e=int(input("Enter 1 if you want to insert more records into this table, 2 if you want to go back to insert menu,3 if you want to go all the way back to main menu and any other number to exit the program."))
    if e==1:
        insrtanime()
    elif e==2:
        Insert()
    elif e==3:
        main_menu()
    else:
        exit()

def Delete():
    print("Welcome to Delete Menu.This menu deletes any record from the tables in the database using the reference code.")
    print("Tables:")
    print("1.Movies")
    print("2.Tv Shows")
    print("3.Games")
    print("4.Anime")
    print("5.Go back to Main menu")
    s=int(input("Enter Table no."))
    
    if s==1:
        deletemoviebycode()
    elif s==2:
        deleteshowbycode()
    elif s==3:
        deletegamebycode()
    elif s==4:
        deleteanimebycode()
    elif s==5:
        main_menu()

def deletemoviebycode():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    try:
        n=str(input("Enter reference code including hash and within quotes:"))
        sql="DELETE from movies where Reference_Code ="
        mycursor.execute(sql+ n)
        res=mycursor.rowcount
        if (res!=0):
            print("Record deleted")
            mycon.commit()
        else:
            print("Record not found")
        
    except:
        print("Error encountered.Try checking the Reference Code once")
    rt=int(input("Enter 1 if you want to delete more records from this table,2 to choose another table from the Delete menu,3 to go back to main menu and any other number to exit."))
    if rt==1:
        deletemoviebycode()
    elif rt==2:
        Delete()
    elif rt==3:
        main_menu()
    else:
        exit()
def deleteshowbycode():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    try:
        n=str(input("Enter reference code including hash and within quotes:"))
        sql="delete from tv_shows where reference_code="
        mycursor.execute(sql+n)
        res=mycursor.rowcount
        if (res!=0):
            print("Record deleted")
            mycon.commit()
        else:
            print("Record not found")
    except:
        print("Error encountered.Try checking the Reference code once")
    rt=int(input("Enter 1 if you want to delete more records from this table,2 to choose another table from the Delete menu,3 to go back to main menu and any other number to exit."))
    if rt==1:
        deleteshowbycode()
    elif rt==2:
        Delete()
    elif rt==3:
        main_menu()
    else:
        exit()

def deletegamebycode():    
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    try:
        n=str(input("Enter reference code including hash and within quotes:"))
        sql="delete from video_games where reference_code="
        mycursor.execute(sql+n)
        res=mycursor.rowcount
        if (res!=0):
            print("Record deleted")
            mycon.commit()
        else:
            print("Record not found")
    except:
        print("Error encountered.Try checking the Reference code once")
    rt=int(input("Enter 1 if you want to delete more records from this table,2 to choose another table from the Delete menu,3 to go back to main menu and any other number to exit."))
    if rt==1:
        deletegamebycode()
    elif rt==2:
        Delete()
    elif rt==3:
        main_menu()
    else:
        exit()

def deleteanimebycode():    
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="agnel",database="cs2")
    mycursor=mycon.cursor()
    try:
        n=str(input("Enter reference code including hash and within quotes:"))
        sql="delete from anime where reference_code="
        mycursor.execute(sql+n)
        res=mycursor.rowcount
        if (res!=0):
            print("Record deleted")
            mycon.commit()
        else:
            print("Record not found")
    except:
        print("Error encountered.Try checking the Reference code once")
    rt=int(input("Enter 1 if you want to delete more records from this table,2 to choose another table from the Delete menu,3 to go back to main menu and any other number to exit."))
    if rt==1:
        deleteanimebycode()
    elif rt==2:
        Delete()
    elif rt==3:
        main_menu()
    else:
        exit()
main_menu()
