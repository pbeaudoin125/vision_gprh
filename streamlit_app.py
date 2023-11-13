import streamlit
import pandas
import snowflake.connector

streamlit.title('Banques de vacances')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called results
my_cur.execute("select * from fact_bank")
results = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(results)
