[English](Step-1-List-Cafes) · [Dansk](Step-1-List-Cafes-da) · **Bahasa Melayu**

# Langkah 1: Senaraikan kafe

Langkah pertama memaparkan semua kafe daripada pangkalan data `cafes.db` yang disediakan pada satu halaman web.

![Senarai kafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-1-list.png)

## Apa yang dibina

- Rekod `Cafe` untuk satu baris dalam jadual `cafe`.
- Repositori dengan `get_all_cafes()` yang membaca baris menggunakan `sqlite3`.
- Pengawal untuk `GET /` dan paparan yang menukar kafe kepada kad HTML: gambar, nama, lokasi, pautan peta, wifi, palam kuasa, tandas, panggilan telefon, tempat duduk dan harga kopi.
- Pelayan yang dimulakan dengan `python -m cafe_wifi` dan dibina atas `wsgiref`, jadi tiada apa yang perlu dipasang.

## Apa yang kita peroleh

- **Membaca SQLite dengan pustaka standard.** `sqlite3` sudah cukup untuk membaca; sambungan ditutup oleh pengurus konteks dan semua pertanyaan menggunakan parameter sejak awal.
- **Melepaskan output (escape).** Setiap nilai daripada pangkalan data dilepaskan sebelum ditulis ke dalam HTML, dan hanya pautan `http` dan `https` digunakan untuk `href` dan `src`.
- **Cara permintaan WSGI berfungsi.** Aplikasi ialah fungsi yang menerima persekitaran permintaan dan mengembalikan status, pengepala dan kandungan. Rangka kerja seperti Flask dibina atas asas yang sama.
- **Data kotor.** Tanda paun dalam harga disimpan sebagai aksara pengganti. Pembetulannya berada dalam satu fungsi dengan ujian, dan fail pangkalan data tidak disentuh.
- **Lapisan.** Capaian data, peraturan dan HTML berada dalam pakej berasingan, jadi setiap lapisan boleh diuji bersendirian.
- **Dari mana gambar datang.** Gambar ialah pautan ke laman web lain. Tangkapan skrin diambil dalam kontena tanpa internet, jadi ruang gambar kelihatan kelabu; pada komputer anda gambar akan dimuatkan.

## Cuba

```bash
python -m cafe_wifi
```

Buka <http://127.0.0.1:8000>.
