import pandas as pd
import streamlit as st

# # Define the dataframe
# df = pd.DataFrame({
#     'filename': ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.csv'],
#     'local address': ['C:\\Documents\\file1.txt', 'C:\\Documents\\file2.txt', 'C:\\Documents\\file3.pdf', 'C:\\Documents\\file4.csv']
# })

# # Get user input
# search_term = st.text_input('Enter search term')

# # Filter the dataframe based on the user input
# filtered_df = df[df['filename'].str.contains(search_term, case=False)]

# # Display the filtered dataframe using st.columns()
# num_columns = len(filtered_df.columns)
# num_rows = len(filtered_df)

# columns = st.columns(num_columns)

# for col_index, column in enumerate(filtered_df.columns):
#     with columns[col_index]:
#         st.write(column)
#         st.write(filtered_df[column].tolist())



# -------------------------------------------------------

# Define the dataframe
df = pd.DataFrame({
    'filename': ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.csv'],
    'local address': ['C:\\Documents\\file1.txt', 'C:\\Documents\\file2.txt', 'C:\\Documents\\file3.pdf', 'C:\\Documents\\file4.csv']
})

# Create a list of unique filenames to use as options in the autocomplete dropdown
options = df['filename'].unique().tolist()

# Get user input with autocomplete
search_term = st.sidebar.text_input('Enter search term', type='default', key='search_term', value='')

# Create a datalist HTML tag with the autocomplete options
options_html = "".join([f"<option value='{option}'></option>" for option in options])
datalist_html = f"<datalist id='options'>{options_html}</datalist>"
st.sidebar.markdown(datalist_html, unsafe_allow_html=True)

# Filter the dataframe based on the user input
filtered_df = df[df['filename'].str.contains(search_term, case=False)]

# Display the filtered dataframe using st.columns()
num_columns = len(filtered_df.columns)
num_rows = len(filtered_df)

columns = st.columns(num_columns)

for col_index, column in enumerate(filtered_df.columns):
    with columns[col_index]:
        st.write(column)
        st.write(filtered_df[column].tolist())