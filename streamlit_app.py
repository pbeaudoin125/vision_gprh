import streamlit
import pandas
import snowflake.connector

streamlit.title('Banques de vacances - Client 270')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called results
# my_cur.execute("select pay_desc, count(distinct directorat_desc) as nb_directorats, sum(bank_value) as valeur_banque from fact_bank group by pay_desc order by pay_desc;")
my_cur.execute("select * from fact_bank;")
results = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(results)

streamlit.header('Sommaire par paie')

# temp write the dataframe to the page so we can see what we're working with
streamlit.write(df)
