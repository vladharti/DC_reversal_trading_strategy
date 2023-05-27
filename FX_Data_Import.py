import pandas as pd
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="username",
password="password",
database="database")
cursor = mydb.cursor()
cursor.execute("select * from vw_DAT_ASCII__EURUSD_T_2")
#second dataset vw_DAT_ASCII_EURGBP_T_2
result=cursor.fetchall()
df=pd.DataFrame(result,columns=cursor.column_names)
#print(df)
