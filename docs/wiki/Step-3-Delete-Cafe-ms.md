[English](Step-3-Delete-Cafe) · [Dansk](Step-3-Delete-Cafe-da) · **Bahasa Melayu**

# Langkah 3: Padam kafe

Langkah ketiga membolehkan pelawat membuang kafe selepas pengesahan.

![Pengesahan pemadaman](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-3-delete-confirm.png)

## Apa yang dibina

- Setiap kad kafe mempunyai pautan "Delete" ke `/delete/<id>`.
- `GET /delete/<id>` memaparkan halaman yang menyebut nama kafe dan meminta pengesahan; `POST /delete/<id>` membuang kafe dengan `delete_cafe()` dan menghantar pelawat kembali ke senarai.
- Id yang tidak wujud, atau bukan nombor bulat, memberi halaman "tidak ditemui" dan tidak mengubah apa-apa.

## Apa yang kita peroleh

- **Kaedah selamat dan tidak selamat.** Permintaan `GET` tidak boleh sekali-kali mengubah data, kerana pelayar, enjin carian dan pratonton pautan memanggilnya sewenang-wenangnya. Hanya `POST` memadam, dan satu ujian memanggil alamat padam dengan `GET` beberapa kali untuk membuktikannya.
- **Pengesahan.** Tindakan yang memusnahkan mendapat halamannya sendiri dengan nama perkara yang akan dibuang, dan cara untuk membatalkan.
- **Penghalaan yang ketat.** Laluan hanya menerima digit (`/delete/42`). Apa-apa lain, seperti `/delete/abc` atau `/delete/1/2`, ialah 404, jadi input pelik tidak sampai ke pangkalan data.
- **"Tidak ditemui" ialah keputusan, bukan kerosakan.** Repositori menjawab "tiada yang dipadam" dengan `False`, dan pengawal menukarnya kepada halaman 404.
- **Dibuat secara berlapis.** Peraturan baharu memerlukan satu kaedah dalam repositori, satu kes guna dan satu laluan pengawal; tiada yang lain perlu diubah.

## Cuba

Mulakan laman web dengan `python -m cafe_wifi`, kemudian klik "Delete" pada sesebuah kafe.
