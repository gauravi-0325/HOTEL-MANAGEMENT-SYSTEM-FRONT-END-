import  mysql.connector as con

conn=con.connect(host="localhost",user="root",password="nitya@567",database="management")
print(conn)