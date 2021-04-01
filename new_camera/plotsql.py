import pandas as pd 
import matplotlib.pyplot as plt 
import database2

database = r"flocs.db"

conn = database2.create_connection(database)
curs = conn.cursor()

sql = "SELECT datetime, SUM(size) AS Total_Size FROM flocs GROUP BY datetime"
sqlsmall = "SELECT datetime, SUM(size) AS Small_Total_Size FROM flocs WHERE size < 1500 GROUP BY datetime"

df = pd.read_sql(sql, conn)
dfsmall = pd.read_sql(sqlsmall, conn)
df = pd.merge(df, dfsmall, on='datetime')
print(df['datetime'].str[11:])
plt.plot(df['datetime'].str[11:], df['Total_Size'], df['Small_Total_Size'])
plt.xlabel("Time")
plt.ylabel("Total Area of Flocs")
plt.title("Total Area of Flocs (Blue) vs Area of Small Flocs (Orange)")
plt.show()