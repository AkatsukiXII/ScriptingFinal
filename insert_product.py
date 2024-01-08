import sqlite3

conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
cursor = conn.cursor()

id = input("請輸入您的商品編號: ")
name = input("請輸入商品名稱: ")
price = input("請輸入價格: ")
stock = input("請輸入庫存量: ")

data=(id,name,price,stock)
cursor.execute("INSERT INTO product (pid,pname,price,pstock) VALUES(?,?,?,?)",data)

conn.commit()
print("寫入成功")
cursor.close()
conn.close()