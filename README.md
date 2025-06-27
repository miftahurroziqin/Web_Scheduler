# 🗓️ WordPress Auto Post Scheduler (Streamlit Web)

Web ini adalah aplikasi berbasis Streamlit yang memungkinkan pengguna untuk menjadwalkan posting artikel ke situs WordPress.com secara otomatis menggunakan file Excel (`posts.xlsx`) sebagai basis datanya. Proses autentikasi menggunakan OAuth2 dengan WordPress Public API.

---

## 🚀 Fitur Utama

- 🔒 Autentikasi OAuth2 via WordPress (menggunakan Client ID dan Secret)
- 📂 Upload file Excel berisi daftar post
- ⏳ Menjadwalkan posting otomatis berdasarkan tanggal publish
- 💬 Menampilkan log hasil posting (berhasil / gagal)
- ✅ Mendukung tag dan konten HTML
- 🔗 Menggunakan API resmi WordPress.com (`rest/v1.1/sites/...`)

---

## 📁 Format File Excel (`posts.xlsx`)

File yang diunggah harus memiliki kolom:

| judul             | konten_html                  | tag              | tanggal_publish |
|------------------|------------------------------|------------------|-----------------|
| Hello World       | `<p>Selamat datang!</p>`     | berita, umum     | 2025-07-01      |

- `judul`: Judul artikel
- `konten_html`: Isi konten dalam format HTML
- `tag`: Daftar tag dipisahkan koma
- `tanggal_publish`: Tanggal publish dalam format `YYYY-MM-DD`

---

## 🔐 OAuth2 Configuration (WordPress Developer Console)

Kamu membutuhkan:
- Client ID
- Client Secret
- Redirect URI → `http://localhost:8501`

URL otorisasi:
https://public-api.wordpress.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:8501&response_type=code&scope=global

URL token exchange:
https://public-api.wordpress.com/oauth2/token


---

## ▶️ Cara Menjalankan

1. Install dependensi
2. Jalankan aplikasi: streamlit run app.py
3.Buka browser ke http://localhost:8501

