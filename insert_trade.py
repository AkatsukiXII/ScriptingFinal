import sqlite3

conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
cursor = conn.cursor()

tid = input("請輸入交易編號: ")
pid = input("請輸入商品編號: ")
count = input("請輸入商品數量: ")
price = input("請輸入商品單價: ")

data=(tid,pid,count,price)
cursor.execute("INSERT INTO trade (tid,pid,tcount,price) VALUES(?,?,?,?)",data)

conn.commit()
print("寫入成功")
cursor.close()
conn.close()