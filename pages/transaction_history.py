import streamlit as st
import pandas as pd
from bank import transaction_history

st.set_page_config(layout="wide")

# Transaction History Page
st.header("Transaction History")

with st.container():
    st.dataframe(transaction_history, width=700)

# # Save the transaction history to a CSV file (optional)
# transaction_history.to_csv("piggy_bank_transactions.csv", index=False)
