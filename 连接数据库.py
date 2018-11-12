import psycopg2

try:
    conn = psycopg2.connect(host="localhost", port=5432, dbname="postgres", user="postgres", password="123456")
    print(conn)
except Exception as ex:
    print(ex)

cur = conn.cursor()
cur.execute("select * from postgres.public.lab;")

rows = cur.fetchall()
for row in rows:
    print(row)

print(rows)
conn.commit()
cur.close()
conn.close()
