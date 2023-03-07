import streamlit as st
# from streamlit_modal import Modal
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# from st_aggrid import AgGrid
from datetime import date
import pandas as pd
import numpy as np
import time

# define variable for json and sheet name
json_file = 'credentials.json'
worksheet_name = 'Sheet1'

# Credentials making
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file)
client = gspread.authorize(creds) # login as client
spreadsheet = client.open('OVEN') # open spreadsheet
worksheet = spreadsheet.worksheet(worksheet_name) # choose worksheet

# Mengambil semua data pada worksheet dan buat menjadi dataframe
data = worksheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
df.index = np.arange(1, len(df)+1)

# web panel
st.set_page_config(page_title="Faris' Webpage", page_icon=":tada:", layout="wide")

# Header
with st.container():
    st.header("Oven 45\xb0C")
    st.subheader("Realtime Sample Tracking")

# Menampilkan data sebagai tabel menggunakan Streamlit
st.dataframe(df, use_container_width=True)
# AgGrid(df, editable=True)


# Fitur tambah dan hapus baris
col1, col2 = st.columns(2)

with col1:
    # fitur forms
    with st.expander("Tambah sampel baru"):
        with st.form("my_form", clear_on_submit=True):
            nama_sampel = st.text_input('Nama Sampel')
            pic = st.text_input('PIC')
            input_date = st.date_input("Tanggal Masuk")
            output_date = st.date_input("Tanggal Keluar")

            submitted = st.form_submit_button("Submit")
        if submitted:
            worksheet.append_row([nama_sampel, pic.title(), input_date.isoformat(), output_date.isoformat()])
            st.success('Data berhasil ditambahkan')
            time.sleep(2)
            st.experimental_rerun()

with col2:
    # Hapus data
    with st.expander("Keluarkan sampel"):
        with st.form('deletion_form', clear_on_submit=True):
            pic = st.selectbox('PIC sampel', 
                               df['PIC'].unique(),
                               key='pic')
            st.write('mengeluarkan sampel milik ', st.session_state.pic)
            index = st.selectbox('sampel number',
                                 df[df['PIC']==st.session_state.pic].index.to_list())
            submitted = st.form_submit_button("Submit")
        if submitted:
            worksheet.delete_row(6)
            st.success('Data berhasil dihapus')
            time.sleep(2)
            st.experimental_rerun()
