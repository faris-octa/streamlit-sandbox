import streamlit as st
import pandas as pd
from pathlib import Path

# data dummy dengan nama file dan link file
data = {'Nama file': ['File 1', 'File 2', 'File 3'],
        'Link file': ['C:\\Users\\INKALI-PC\\Desktop\\Manajemen Dokumen PE (Faris).docx',
                      'C:\\Users\\INKALI-PC\\Desktop\\File2.docx',
                      'C:\\Users\\INKALI-PC\\Desktop\\File3.docx']}

# konversi data ke pandas DataFrame
df = pd.DataFrame(data)

# tambahkan kolom "Link" berisi tautan hyperlink ke file
df['Link'] = df['Link file'].apply(lambda x: f'<a href="file://{Path(x).resolve()}">Open file</a>')
st.write(df, unsafe_allow_html=True)