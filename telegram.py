import requests

# 1. BİLGİLERİNİ BURAYA GİR
TOKEN = "8211810182:AAG408mteKNxG02so75DHvbgJL_eXSc8l5k" # BotFather'dan aldığın token
CHAT_ID = "1387971751"  # Not: CHAT_ID'yi öğrenmek için @userinfobot'a mesaj atabilir ve oradan "Your Telegram ID" kısmını görebilirsin.

# 2. GÖNDERİLECEK MESAJ
MESAJ = "Python'dan Telegram'a ilk veri füzemiz ulaştı. Sistem aktif! "

# 3. TELEGRAM'IN KAPISINI ÇAL (API İsteği)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESAJ
}

# 4. ATEŞLE!
print(" Telegram'a mesaj gönderiliyor...")
response = requests.post(url, data=payload)

# 5. SONUCU KONTROL ET
if response.status_code == 200:
    print(" BAŞARILI! Telefonuna bak, mesaj geldi mi?")
else:
    print(f" HATA: {response.text}")