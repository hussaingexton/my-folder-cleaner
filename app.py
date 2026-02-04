import streamlit as st
import os
from zipfile import ZipFile
import io

st.set_page_config(page_title="Auto Folder Cleaner", page_icon="📁")

st.title("📁 AI Folder Cleaner")
st.write("Apni messy files upload karein, main unhein folders mein organize kar ke ZIP bana doonga!")

uploaded_files = st.file_uploader("Files select karein", accept_multiple_files=True)

if uploaded_files:
    if st.button("Organize & Download ZIP"):
        memory_file = io.BytesIO()
        with ZipFile(memory_file, 'w') as zf:
            for file in uploaded_files:
                ext = os.path.splitext(file.name)[1].lower()
                
                # Logic: Extensions ke hisab se folders
                if ext in ['.jpg', '.png', '.jpeg', '.gif']:
                    folder = "Images"
                elif ext in ['.pdf', '.docx', '.txt', '.xlsx']:
                    folder = "Documents"
                elif ext in ['.mp4', '.mkv', '.mov']:
                    folder = "Videos"
                else:
                    folder = "Others"
                
                zf.writestr(f"{folder}/{file.name}", file.getvalue())
        
        memory_file.seek(0)
        st.download_button(
            label="📥 Download Organized ZIP",
            data=memory_file,
            file_name="Cleaned_Files.zip",
            mime="application/zip"
        )