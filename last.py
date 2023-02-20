import streamlit as st
import pandas as pd
import os

file_path = r"C:\Users\INKALI-PC\Desktop\Perbaikan Produk OQC FL-27 (Faris).docx"

# # Show user table 
colms = st.columns((1, 2, 2, 1, 1))
fields = ["№", 'email', 'uid', 'verified', "action"]
for col, field_name in zip(colms, fields):
    # header
    col.write(field_name)

col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
col1.write("kolom 1")
button_phold = col5.empty()
if button_phold.button("click"):
    os.startfile(file_path)


# for x, email in enumerate(user_table['email']):
#     col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
#     col1.write(x)  # index
#     col2.write(user_table['email'][x])  # email
#     col3.write(user_table['uid'][x])  # unique ID
#     col4.write(user_table['verified'][x])   # email status
#     disable_status = user_table['disabled'][x]  # flexible type of button
#     button_type = "Unblock" if disable_status else "Block"
#     button_phold = col5.empty()  # create a placeholder
#     do_action = button_phold.button(button_type, key=x)
#     if do_action:
#             pass # do some action with a row's data
#             button_phold.empty()  #  remove button