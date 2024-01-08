import sqlite3

conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
cursor = conn.cursor()

id = input("請輸入您的客戶編號: ")
name = input("請輸入您的名字: ")
phone = input("請輸入您的手機號碼: ")
add = input("請輸入您的地址: ")

data=(id,name,phone,add)
cursor.execute("INSERT INTO customer (cid,cname,cphone,cadd) VALUES(?,?,?,?)",data)

conn.commit()
print("寫入成功")
cursor.close()
conn.close()