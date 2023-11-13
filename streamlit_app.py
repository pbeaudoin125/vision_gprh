import streamlit
import pandas
import snowflake.connector

streamlit.title('Banques de vacances - Client 270')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called results
# my_cur.execute("select pay_desc, count(distinct directorat_desc) as nb_directorats, sum(bank_value) as valeur_banque from fact_bank group by pay_desc order by pay_desc;")
my_cur.execute("select pay_desc, bank_value from fact_bank;")
results = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(results, columns=["Paie", "Valeur"])

streamlit.header('Sommaire par paie')

# temp write the dataframe to the page so we can see what we're working with
# streamlit.write(df)

chart_data_agg = df.groupby("Paie")["Valeur"].sum()
streamlit.write(chart_data_agg)

print(chart_data_agg.columns)

# col = streamlit.multiselect("Select any column", chart_data_agg.columns)
# streamlit.dataframe(data[col])

streamlit.bar_chart(df, x="Paie", y="Valeur")
# streamlit.bar_chart(chart_data_agg, x="Paie", y="Valeur")
