[English](Step-2-Add-Cafe) · [Dansk](Step-2-Add-Cafe-da) · **Bahasa Melayu**

# Langkah 2: Tambah kafe

Langkah kedua membolehkan pelawat menambah kafe melalui borang.

![Borang tambah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-form.png)

Apabila input salah, borang dipaparkan semula dengan masalahnya dan nilai yang ditaip:

![Borang dengan ralat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-errors.png)

## Apa yang dibina

- `GET /add` memaparkan borang kosong; `POST /add` mengesahkannya dan menyimpan kafe dengan `add_cafe()`.
- Fungsi pengesahan tulen yang memberi satu ralat bagi setiap medan: nama dan lokasi wajib, pautan peta dan gambar mestilah `http` atau `https`, dan tiada medan lebih panjang daripada lajur pangkalan data.
- Rekod `NewCafe`, `DuplicateCafeError` untuk nama yang sudah wujud, dan kes guna `AddCafe` yang menukar ralat itu kepada mesej pada medan nama.
- Pautan "Add a cafe" pada pengepala halaman.

## Apa yang kita peroleh

- **Mengendalikan borang.** Borang dihantar sebagai `application/x-www-form-urlencoded`; pelayan membaca bilangan bait yang terhad dan mengurainya dengan `urllib.parse`. Kotak semak hanya dihantar apabila ditandakan, jadi medan yang tiada bermaksud "tidak".
- **Pengesahan di satu tempat.** Peraturan ialah fungsi tulen dalam lapisan domain dan diuji tanpa pelayan atau pangkalan data.
- **Post, redirect, get.** Selepas post berjaya, pelayan menjawab `303 See Other` dan pelayar memuatkan senarai. Muat semula memaparkan senarai sekali lagi dan tidak menghantar borang dua kali.
- **SQL berparameter.** Nilai tidak pernah dicantum ke dalam teks SQL. Satu ujian menyimpan nama yang kelihatan seperti serangan SQL dan menyemak bahawa ia disimpan sebagai teks biasa dan jadual masih utuh.
- **Pangkalan data sebagai pengawal peraturan.** Nama unik dikuatkuasakan oleh pangkalan data; repositori menterjemah ralatnya kepada ralat domain yang boleh dipaparkan oleh borang.

## Cuba

Mulakan laman web dengan `python -m cafe_wifi` dan buka <http://127.0.0.1:8000/add>.
