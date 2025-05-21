import streamlit as st

st.title("naila pake i bukan y")
st.write(
    "pinkienaii."
)
st.image("IMG_4899.jpeg")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write("f{angka} adalah bilangan genap")
else:
  st.write("f{angka} adalah bilangan ganjil")
