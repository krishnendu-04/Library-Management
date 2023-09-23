import mysql.connector
from tabulate import tabulate
from datetime import timedelta,date

def addbooks():
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="library_management")
    cur=con.cursor()
    print('\n ADD BOOK SCREEN ')
    print('-'*120)
    bid=input("Enter Book ID: ")
    bname=input("Enter Book Name: ")
    b_author=input("Enter Author: ")
    b_status=input("Enter Status: ")
    st="insert into books(book_id,title,author,status)values('{}','{}','{}','{}')".format(bid,bname,b_author,b_status)
    cur.execute(st)
    con.commit()
    print('\nNew Book Added Successfully!!')

def addmembers():
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="library_management")
    cur=con.cursor()
    print('\n ADD MEMBER SCREEN ')
    print('-'*120)
    mid=input("Enter Member ID: ")
    mname=input("Enter Member Name: ")
    ph_no=int(input("Enter Phone Number: "))
    st="insert into members(member_id,name,phone_no)values('{}','{}','{}')".format(mid,mname,ph_no)
    cur.execute(st)
    con.commit()
    print('\nNew Member Added Successfully!!')

def search_book(field):
    conn = mysql.connector.connect(
    host='localhost', database='library_management', 
    user='root', password='root')
    cursor = conn.cursor()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' of the Book:'
    title = input(msg)
    sql ='select * from books where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Search Result for ',field,' :' ,title)
    a=list(records)
    print(tabulate(a,headers=['Book ID','Title','Author','Status'],tablefmt='fancy_grid'))
    print('\n')

def booksearch_menu():
    while True:
        print(' B O O K S E A R C H M E N U ')
        print("\n1. Book Title")
        print('\n2. Book Author')
        print('\n3. Exit to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        field =''
        if choice == 1:
            field='title'
        if choice == 2:
            field = 'author'
        if choice == 3:
            break
        search_book(field)

def search_member(field):
    conn = mysql.connector.connect(
    host='localhost', database='library_management', 
    user='root', password='root')
    cursor = conn.cursor()
    print('\n MEMBER SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' of the Member:'
    title = input(msg)
    sql ='select * from members where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Search Result for ',field,' :' ,title)
    a=list(records)
    print(tabulate(a,headers=['Member ID','Name','Phone Number'],tablefmt='fancy_grid'))
    print('\n')

def membersearch_menu():
    while True:
        print(' M E M B E R S E A R C H M E N U ')
        print("\n1. Member ID")
        print('\n2. Member Name')
        print('\n3. Exit to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        field =''
        if choice == 1:
            field='member_id'
        if choice == 2:
            field = 'name'
        if choice == 3:
            break
    search_member(field)

def update_book():
    conn = mysql.connector.connect(host='localhost',database='library_management', user='root', password='root')
    cursor = conn.cursor()
    print('\n UPDATE BOOK DETAILS SCREEN ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title'
    elif choice == 2:
        field = 'author'
    try:
        book_id = input('Enter Book ID :')
        value = input('Enter new value:')
        sql='update books set ' + field + ' = "'+value+'" where book_id="'+book_id+'";'
        cursor.execute(sql)
        conn.commit()
        print('\nBook details updated Successfully!!')
    except:
        print("Book with given ID does not exist!")
 
def update_member():
    conn = mysql.connector.connect(host='localhost', database='library_management',user='root', password='root')
    cursor = conn.cursor()
    print('\n UPDATE MEMBER INFORMATION SCREEN ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Phone')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'phone_no'
    try:
        mem_id =input('Enter member ID :')
        value = input('Enter new value :')
        sql = 'update members set '+ field +' = "'+value+'" where member_id ="'+mem_id+'";'
        cursor.execute(sql)
        conn.commit()
        print('\nMember details updated Successfully!!')
        conn.close()
    except:
        print("Member with given ID does not exist!")
 
def report():
    def report_book_list():
        conn = mysql.connector.connect(host='localhost', database='library_management', user='root', password='root')
        cursor = conn.cursor()
        print('\n REPORT - BOOK TITLES ')
        print('-'*120)
        sql ='select * from books'
        cursor.execute(sql)
        records = cursor.fetchall()
        a=list(records)
        print(tabulate(a,headers=['Book ID','Title','Author','Status'],tablefmt='fancy_grid'))
        print('\n')
 
def report_issued_books():
    conn = mysql.connector.connect(host='localhost', database='library_management',user='root', password='root')
    cursor = conn.cursor()
    print('\n REPORT - BOOK TITLES - Issued')
    print('-'*120)
    sql = 'select * from books where status = "Issued";'
    cursor.execute(sql)
    records = cursor.fetchall()
    a=list(records)
    print(tabulate(a,headers=['Book ID','Title','Author','Status'],tablefmt='fancy_grid'))
    print('\n')
    
def report_available_books():
    conn = mysql.connector.connect(
    host='localhost', database='library_management',user='root', password='root')
    cursor = conn.cursor()
    print('\n REPORT - BOOK TITLES - Available')
    print('-'*120)
    sql = 'select * from books where status = "Available";'
    cursor.execute(sql)
    records = cursor.fetchall()
    a=list(records)
    print(tabulate(a,headers=['Book ID','Title','Author','Status'],tablefmt='fancy_grid'))
    print('\n')
 
def report_lost_books():
    conn = mysql.connector.connect(host='localhost',database='library_management', user='root', password='root')
    cursor = conn.cursor()
    print('\n REPORT - BOOK TITLES - Lost')
    print('-'*120)
    sql = 'select * from books where status = "Lost";'
    cursor.execute(sql)
    records = cursor.fetchall()
    a=list(records)
    print(tabulate(a,headers=['Book ID','Title','Author','Status'],tablefmt='fancy_grid'))
    print('\n')

def report_member_list():
    conn=mysql.connector.connect(host='localhost',database='library_management',user='root',password='root')
    cursor=conn.cursor()
    print("\n REPORT - Member List")
    print('-'*120)
    sql='select * from members'
    cursor.execute(sql)
    records=cursor.fetchall()
    a=list(records)
    print(tabulate(a,headers=['Member ID','Name','Phone Number'],tablefmt='fancy_grid'))
    print('\n')
     
def report_menu():
    while True:
        print(' R E P O R T M E N U ')
        print("\n1. Book List")
        print('\n2. Issued Books')
        print('\n3. Available Books')
        print('\n4. Lost Book')
        print('\n5. Member List')
        print('\n6. Exit to main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            report_book_list()
        elif choice == 2:
            report_issued_books()
        elif choice == 3:
            report_available_books()
        elif choice ==4:
            report_lost_books()
        elif choice==5:
            report_member_list()
        elif choice == 6:
            break
        else:
            print("ENTER VALID CHOICE")
            print('\n')
    report_menu()

def delete_book():
    con= mysql.connector.connect(host ="localhost",user = "root",password = 'root',database='library_management')
    cursor = con.cursor()
    print('\n DELETE BOOK SCREEN ')
    print('-'*120)
    bid=input("Enter Book ID: ")
    try:
        sql= "delete from books where book_id='"+bid+"';"
        cursor.execute(sql)
        con.commit()
        print("\nBook deleted Successfully!!")
    except:
        print("Book with given ID does not exist!")
 
def delete_member():
    con= mysql.connector.connect(host ="localhost",user = "root",password = 'root',database='library_management')
    cursor = con.cursor()
    print('\n DELETE MEMBER SCREEN ')
    print('-'*120)
    mid=input("Enter Member ID: ")
    try:
        sql= "delete from members where member_id='"+mid+"';"
        cursor.execute(sql)
        con.commit()
        print("\nMember deleted Successfully!!")
    except:
        print("Member with given ID does not exist!")

def issue_book():
    con= mysql.connector.connect(host='localhost', database='library_management', user='root', password='root')
    cur = con.cursor()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    a='select * from books where status="Available"'
    cur.execute(a)
    flag=0
    book_id=input("Enter Book id: ")
    for i in cur:
        if i[0]==book_id:
            flag=1
    if flag==1:
        member_id=input("Enter member id: ")
        today = date.today()
        due_date=today+timedelta(days=14)
        sql='insert into issue values("'+book_id+'","'+member_id+'","'+str(today)+'","'+str(due_date)+'");'
        sql1= 'update books set status="Issued" where book_id ="'+book_id+'";'
        cur.execute(sql)
        cur.execute(sql1)
        con.commit()
        print("\nBook issued Successfully!!")
        print("\nTo be returned on or before: ",due_date)
    else:
        print("The Required book is not available")

def return_book():
    con= mysql.connector.connect(host='localhost', database='library_management', user='root', password='root')
    cur = con.cursor()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    a='select * from books where status="Issued"'
    cur.execute(a)
    flag=0
    book_id=input("Enter Book id: ")
    for i in cur:
        if i[0]==book_id:
            flag=1
    if flag==1:
        sql='delete from issue where book_id="'+book_id+'";'
        sql1= 'update books set status="Available" where book_id ="'+book_id+'";'
        cur.execute(sql)
        cur.execute(sql1)
        con.commit()
        print("\nBook returned Successfully!!")
    else:
        print("The Required book is not available")
 
 
def main_menu():
    while True:
        print('\n')
        print('-'*120)
        print(" R E A D E R ' S H U B L I B R A R Y ")
        print('-'*120)
        print('\n')
        print('\n1. ADD BOOKS')
        print('\n2. ADD MEMBERS')
        print('\n3. SEARCH BOOKS')
        print('\n4. SEARCH MEMBERS')
        print('\n5. UPDATE BOOKS')
        print('\n6. UPDATE MEMBERS')
        print('\n7. GENERATE REPORT')
        print('\n8. DELETE BOOKS')
        print('\n9. DELETE MEMBERS')
        print('\n10. ISSUE BOOK')
        print('\n11. RETURN BOOK')
        print('\n12. EXIT')
        print('\n\n')
        choice=int(input("Enter your choice....:"))
        print('\n')
        if choice==1:
            addbooks()
        elif choice==2:
            addmembers()
        elif choice==3:
            booksearch_menu()
        elif choice==4:
            membersearch_menu()
        elif choice==5:
            update_book()
        elif choice==6:
            update_member()
        elif choice==7:
            report()
        elif choice==8:
            delete_book()
        elif choice==9:
            delete_member()
        elif choice==10:
            issue_book()
        elif choice==11:
            return_book()
        elif choice==12:
            print("\n Thank You For choosing us...See you again!!")
            break
        else:
            print("\n INVALID CHOICE!! Try Again")
        main_menu()







    





