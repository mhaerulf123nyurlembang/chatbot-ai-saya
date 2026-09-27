from openai import OpenAI

# Masukkan API Key Anda di sini
client = OpenAI(api_key="AQ.Ab8RN6IPfyaUcud03KtkDaNPul4OTDa6f_GGbWlhXaWhsHvnSg")

print("Halo! Chatbot AI siap membantu. Ketik 'keluar' untuk berhenti.\n")

while True:
    pesan_pengguna = input("Anda: ")
    
    if pesan_pengguna.lower() == 'keluar':
        print("Chatbot: Sampai jumpa!")
        break

    # Mengirim pesan ke model AI
    respons = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Anda adalah asisten yang ramah dan membantu."},
            {"role": "user", "content": pesan_pengguna}
        ]
    )

    # Menampilkan jawaban dari AI
    jawaban_ai = respons.choices[0].message.content
    print(f"Chatbot: {jawaban_ai}\n")
