import sqlite3

conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM customer')
result = cursor.fetchall()
print("客戶資料: ")
for row in result:
    print(f'cid:{row[0]} ,cname:{row[1]}, cphone:{row[2]}, cadd:{row[3]}')

print("-"*40)

cursor.execute('SELECT * FROM product')
result = cursor.fetchall()
print("商品資料: ")
for row in result:
    print(f'pid:{row[0]} ,pname:{row[1]}, price:{row[2]}, pstock:{row[3]}')
    
print("-"*40)

cursor.execute('SELECT * FROM store')
result = cursor.fetchall()
print("門市資料: ")
for row in result:
    print(f'sid:{row[0]} ,scode:{row[1]}, sname:{row[2]}, sadd:{row[3]}')
    
print("-"*40)

cursor.execute('SELECT * FROM trade')
result = cursor.fetchall()
print("交易資料: ")
for row in result:
    print(f'tid:{row[0]} ,pid:{row[1]}, tcount:{row[2]}, price:{row[3]}')



cursor.close()
conn.close()