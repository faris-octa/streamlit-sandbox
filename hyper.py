import streamlit as st
import os

file_path = r'C:\Users\INKALI-PC\Desktop\Manajemen Dokumen PE (Faris).docx'
if os.path.exists(file_path):
    st.markdown(f'[Download file]({file_path})', unsafe_allow_html=True)
else:
    st.write("File tidak ditemukan")


with open(file_path, 'rb') as f:
    st.download_button(label='Download',
                        data=f,
                        file_name=file_path.split('\\')[-1])

if st.button(f'Buka file {file_path}'):
    os.startfile(file_path)