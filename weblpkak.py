import streamlit as st 

st.title('Kelompok 4 LPK')
st.title('Aplikasi Perubah PPM ke Molaritas')
ppm = st.number_input("Masukkan nilai ppm (mg/L)")
ar = st.number_input("Masukkan nilai berat molekul (mg/mmol)")

tombol = st.button('hitung nilai molaritas')

if tombol:
    nilai_molaritas = round(ppm/ar)/1000
    st.success(f'Nilai molaritas adalah {nilai_molaritas}')