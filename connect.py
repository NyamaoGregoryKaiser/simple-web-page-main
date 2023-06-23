import mysql.connector
conn = mysql.connector.connect(host="localhost", user = "root", passwd = "")

mycur = conn.cursor()
mycur.execute("use footballdb")


mycur.execute('insert into players values("103","Nyamao","terry","Mukonga","12-20-2023","male","Kenya")')
mycur.execute("select * from players")
for x in mycur:
    print(x)

conn.close()