import sqlite3

conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
cursor = conn.cursor()

id = input("請輸入門市編號: ")
code = input("請輸入統一編號: ")
name = input("請輸入門市名稱: ")
add = input("請輸入您的地址: ")

data=(id,code,name,add)
cursor.execute("INSERT INTO store (sid,scode,sname,sadd) VALUES(?,?,?,?)",data)

conn.commit()
print("寫入成功")
cursor.close()
conn.close()