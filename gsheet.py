import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from st_aggrid import AgGrid
from datetime import date
import pandas as pd
import numpy as np

# Masukkan nama file JSON yang sudah Anda download
json_file = 'booming-triode-305701-7b37e82be7a3.json'

# Masukkan nama worksheet pada Google Sheets
worksheet_name = 'Sheet1'

# Membuat credentials object
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file)

# Membuat client object
client = gspread.authorize(creds)

# Membuka spreadsheet
spreadsheet = client.open('OVEN')

# Memilih worksheet
worksheet = spreadsheet.worksheet(worksheet_name)

# Mengambil semua data pada worksheet
data = worksheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
df.index = np.arange(1, len(df)+1)

# Header
with st.container():
    st.header("Oven 45\xb0C")
    st.subheader("Realtime Sample Tracking")

# Menampilkan data sebagai tabel menggunakan Streamlit
st.table(df)

# Menambahkan data pada worksheet
nama_sampel = st.text_input('Nama Sampel')
pic = st.text_input('PIC')
input_date = st.date_input(
    "Tanggal Masuk",
    date.today())
output_date = st.date_input(
    "Tanggal Keluar",
    date.today())

if st.button('Tambah Data'):
    # Menambahkan data pada worksheet
    worksheet.append_row([nama_sampel, pic, input_date.isoformat(), output_date.isoformat()])

    # Menampilkan pesan sukses pada web app
    st.success('Data berhasil ditambahkan ke Google Sheet')
    st.experimental_rerun()