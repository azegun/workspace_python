import pymysql as pm
import pymysql.cursors

conn = pm.connect(host='localhost',
                  user='root',
                  password='rootroot')

# create_database = 'create database test1'
# conn.cursor().execute(create_database)

# sql = 'show databases;'
# sql_test = conn.cursor().execute(sql)
# print(sql_test)
cursor = conn.cursor(pymysql.cursors.DictCursor)
# database 사용
cursor.execute('use test1;')

# insert
# insert_sql = 'insert into test_table(name) values("python")'
# cursor.execute(insert_sql)

# select all
select_sql = 'select * from test_table;'
cursor.execute(select_sql)
result = cursor.fetchall()
print(result)

# update
# update_sql = 'update test_table set name = "HTML" where id = 1'
# cursor.execute(update_sql)

# delete
# delete_sql = 'delete from test_table where id = 3'
# cursor.execute(delete_sql)

conn.commit()
conn.close()
