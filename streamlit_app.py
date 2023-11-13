import streamlit
import pandas
import snowflake.connector

streamlit.title('Banques de vacances - Client 270')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called results
my_cur.execute("select pay_desc, pay_end_date, bank_value from fact_bank;")
results = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(results, columns=["Paie", "Date de fin", "Valeur"])

# temp write the dataframe to the page so we can see what we're working with
# streamlit.write(df)

table_data = df.groupby(["Paie", "Date de fin"])["Valeur"].agg(['sum','count'])
table_data.columns = ["Total", "Nombre"]

streamlit.header('Sommaire par paie')
streamlit.write(table_data)

my_cur.execute("select directorat_desc, bank_value from fact_bank;")
results = my_cur.fetchall()
df = pandas.DataFrame(results, columns=["Directorat", "Valeur"])
chart_data = df.groupby("Paie")["Valeur"].sum()

streamlit.header('Sommaire par directorat')
streamlit.bar_chart(chart_data)
