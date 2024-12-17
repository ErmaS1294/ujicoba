import pickle
import streamlit as st

# Load model
model = pickle.load(open('Test_Kepribadian.sav', 'rb'))

# Background styling
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #F0F8FF;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and introduction
st.title('Test Diagnosa Tipe Kepribadian')
st.write("Jawablah pertanyaan berikut dengan pilihan **Yes** atau **No**.")
st.image('Mobil BMW.jpg')

# Questions
st.subheader("Pertanyaan")
questions = [
    "Apakah Anda senang bicara tanpa dihentikan?",
    "Apakah Anda emosi bergejolak dan transparan?",
    "Apakah Anda senang menolong?",
    "Apakah Anda tidak dapat dijadikan sandaran?",
    "Apakah Anda mudah berubah mood?",
    "Apakah Anda sedikit pelupa?",
    "Apakah Anda sulit berkonsentrasi?",
    "Apakah Anda kurang disiplin waktu?",
    "Apakah Anda disiplin waktu?",
    "Apakah Anda introvert, pemikir, dan pesimis?",
    "Apakah Anda teratur, rapi, terjadwal, tersusun sesuai pola?",
    "Apakah Anda menyukai fakta-fakta?",
    "Apakah Anda cenderung menganalisa dan mempertimbangkan?",
    "Apakah Anda ingin selalu sempurna?",
    "Apakah Anda segala sesuatu ingin teratur?",
    "Apakah Anda mendominasi pembicaraan?",
    "Apakah Anda suka mengatur?",
    "Apakah Anda suka memerintah?",
    "Apakah Anda tidak punya banyak teman?",
    "Apakah Anda tidak mau kalah?",
    "Apakah Anda senang dengan tantangan?",
    "Apakah Anda suka petualangan?",
    "Apakah Anda tegas, kuat, cepat, dan tangkas?",
    "Apakah Anda tidak ada istilah tidak mungkin?",
    "Apakah Anda mau merugi agar masalah tidak berkepanjangan?",
    "Apakah Anda kurang bersemangat?",
    "Apakah Anda kurang teratur dan serba dingin?",
    "Apakah Anda cenderung diam?",
    "Apakah Anda kalem?",
    "Apakah Anda pendengar yang baik?",
    "Apakah Anda suka menunda dalam mengambil keputusan?",
    "Apakah Anda sangat memerlukan perubahan?"
]

# User inputs
responses = []
for idx, question in enumerate(questions):
    response = st.radio(f"{idx+1}. {question}", ("Yes", "No"), key=idx)
    responses.append(1 if response == "Yes" else 0)  # Convert Yes -> 1, No -> 0

# Diagnosis button
if st.button("Diagnosa"):
    # Perform prediction using the model
    prediction = model.predict([responses])[0]  # Ensure input matches model requirements

    # Interpret prediction result
    personality_types = {
        0: "Sanguinis",
        1: "Melankolis",
        2: "Koleris",
        3: "Plegmatis"
    }
    personality_result = personality_types.get(prediction, "Tipe tidak diketahui")

    # Display the result
    st.subheader("Hasil Diagnosa")
    st.write(f"Tipe kepribadian Anda adalah **{personality_result}**.")
    st.success(f"Selamat, Anda memiliki kepribadian **{personality_result}** berdasarkan jawaban Anda!")