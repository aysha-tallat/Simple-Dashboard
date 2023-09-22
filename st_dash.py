import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Sales Dashboard American SuperStore",
                    page_icon='📊',
                    layout='wide')

sstore = pd.read_excel('superstore.xlsx')
#----------Side bar---------------
st.sidebar.header("Filter")

Region = st.sidebar.multiselect(
    "Region",
    options=sstore['Region'].unique(),
    default=sstore['Region'].unique()
)

Category = st.sidebar.multiselect(
    "Category",
    options=sstore['Category'].unique(),
    default=sstore['Category'].unique()
)

sstore_selection =sstore.query(
    "Region == @Region & Category == @Category"
)
#st.dataframe(sstore_selection)

#----------Main Page---------------
st.title(":bar_chart: Super Store Sales Dashboard")
st.markdown("##")
total_profit = int(sstore_selection['Profit'].sum())
pure_profit = round(sstore_selection[sstore_selection['Profit']>0]['Profit'].sum(),2)
loss = round(sstore_selection[sstore_selection['Profit']<=0]['Profit'].sum(),2)
total_sales =int(sstore_selection['Sales'].sum())
average_discount = round(sstore_selection[sstore_selection['Discount']!=0]['Discount'].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Profit')
    st.subheader(f"US $ {total_profit :,}")
    st.markdown("###")
    lt_col, rt_col = st.columns(2)
    with lt_col:
       st.subheader('Pure Profit')
       st.subheader(f"US $ {pure_profit :,}")
    with rt_col:
        st.subheader('Loss')
        st.subheader(f"US $ {loss :,}")

with middle_column:
    st.subheader('Total Sales')
    st.subheader(total_sales)

with right_column:
    st.subheader("Average Discount")
    st.subheader(f"US $ {average_discount :,}")

st.markdown("___")

columns=["Customer ID","Customer Name","Country","Postal Code","Product ID","Product Name",'Ship Mode',"Row ID","Order ID","Order Date","Ship Date"]
for i in columns:
    if i in columns:
        sstore_selection=sstore_selection.drop(i,axis=1)

st.dataframe(sstore_selection)



