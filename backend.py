import sqlite3 as sq

#creating table
con = sq.connect('bookinfo.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS book_dir(book_id integer PRIMARY KEY, "
            "title text, author_name text, year integer, isbn integer)")
con.commit()
con.close()

#view table contents
def view_books():
    try:     
         con = sq.connect('bookinfo.db')
         cur = con.cursor()
         query="select * from book_dir"
         cur.execute(query)
         data = cur.fetchall()
         return data

    except Exception as e:
       print("Error occured!!")
       print("Problem: ",e)
         
    finally:
         con.close()
    
#add values in table
def add_book(t,a,y,i):
    try:   
         con = sq.connect('bookinfo.db')
         cur = con.cursor()
         
         q=("insert into book_dir" 
            " values(NULL,?, ?, ?, ?)")
        
         cur.execute(q,(t,a,y,i))
         con.commit()

    except Exception as e:
       print("Error occured!!")
       print("Problem: ",e)
         
    finally:
         con.close()

#delete operation
def delete_book(book_id):
    try:   
         con = sq.connect('bookinfo.db')
         cur = con.cursor()
         
         q=("delete from book_dir" 
            " where book_id = ?")
        
         cur.execute(q,(book_id,))
         con.commit()

    except Exception as e:
       print("Error occured!!")
       print("Problem: ",e)
         
    finally:
         con.close()   


#search book
def search_books(t,a,y,i):
    try:   
         con = sq.connect('bookinfo.db')
         cur = con.cursor()
         
         q=("select * from book_dir" 
            " where title = ? OR author_name = ? OR year = ? OR isbn = ?")
         cur.execute(q,(t,a,y,i))
         data=cur.fetchall()

         con.commit()
         return data

    except Exception as e:
       print("Error occured!!")
       print("Problem: ",e)
         
    finally:
         con.close()


#update entry
def update_book(book_id,t,a,y,i):
    try:   
         con = sq.connect('bookinfo.db')
         cur = con.cursor()
         
         q=("update book_dir" 
            " set title= ?,"
            " author_name= ?,"
            " year= ?, "
            " isbn = ?"
            "where book_id = ?")
        
         cur.execute(q,(t,a,y,i,book_id))
         con.commit()

    except Exception as e:
       print("Error occured!!")
       print("Problem: ",e)
         
    finally:
         con.close()
      

