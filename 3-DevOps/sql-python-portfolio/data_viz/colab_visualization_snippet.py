# Run this in Google Colab (or locally) after starting an ngrok TCP tunnel
# pip install psycopg2-binary pandas numpy matplotlib

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace with your ngrok forwarding host/port
NGROK_HOST = "4.tcp.ngrok.io"   # example
NGROK_PORT = 16960              # example
DBNAME = "portfolio_db"
USER = "postgres"
PASSWORD = "postgres"  # set your password if required

con = psycopg2.connect(
    dbname=DBNAME,
    user=USER,
    host=NGROK_HOST,
    port=NGROK_PORT,
    password=PASSWORD
)

def sql_to_df(sql_query: str):
    return pd.read_sql(sql_query, con)

title = "Posts by Topic"
query = '''
    SELECT topic, COUNT(*) AS count
    FROM posts
    GROUP BY topic
    ORDER BY count DESC;
'''

df = sql_to_df(query)

plt.figure(figsize=(10, 5))
xpos = np.arange(len(df))
plt.bar(xpos, df["count"])
plt.xticks(xpos, df["topic"], rotation=30, ha="right")
plt.ylabel("Count")
plt.title(title)
plt.tight_layout()
plt.show()
