import streamlit as st
import pickle

# Load model Forward Chaining
with open('ForwardChaining_Model.sav', 'rb') as file:
    engine = pickle.load(file)

st.title("Test Diagnosa Tipe Kepribadian")
st.write("Jawablah pertanyaan berikut dengan pilihan **Ya** atau **Tidak**.")

# Input checklist gejala
user_facts = []
for code, description in engine.descriptions.items():
    response = st.radio(f"{code} - {description}", ["Ya", "Tidak"], key=code)
    if response == "Ya":
        user_facts.append(code)

# Tambahkan fakta ke mesin Forward Chaining
for fact in user_facts:
    engine.add_fact(fact)

# Diagnosa ketika tombol ditekan
if st.button("Diagnosa"):
    diagnoses = engine.infer()

    # Tampilkan hasil diagnosa
    st.subheader("Hasil Diagnosa:")
    for diagnosis in diagnoses:
        st.write(f"**{diagnosis['diagnosis']}**: Gejala Terdeteksi {diagnosis['matched']} dari total {diagnosis['total']} gejala. Persentase: **{diagnosis['percentage']}%**")

    # Tipe dominan
    if diagnoses:
        highest = max(diagnoses, key=lambda d: d['percentage'])
        st.subheader(f"Tipe Kepribadian Dominan Anda: **{highest['diagnosis']}** ({highest['percentage']}%)")
