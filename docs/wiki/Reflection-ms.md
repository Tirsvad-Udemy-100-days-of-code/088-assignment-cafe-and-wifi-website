[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Melayu**

# Refleksi

Tugasan meminta jurnal tentang cara projek ini didekati. Ini jurnal kami.

## Bagaimana kami mendekatinya

Kami merancang sebelum menulis kod: kes perniagaan, orang yang akan menggunakan hasilnya, pelan dengan lima pencapaian (milestone) dan senarai tugas. Kemudian setiap pencapaian ialah satu cabang dan satu pull request yang disemak berdasarkan senarai semak sebelum digabungkan. Laman web itu sendiri berkembang dalam tiga langkah (senarai, tambah, padam), dan setiap langkah berakhir dengan ujian, tangkapan skrin dan halaman wiki.

## Apa yang mudah

- Membaca data. `sqlite3` ada dalam pustaka standard, dan jadualnya kecil dan jelas.
- Lapisan. Apabila kes guna pertama mempunyai repositori, pengawal dan paparannya, dua langkah seterusnya hanyalah tambahan kecil.

## Apa yang sukar

- Bekerja tanpa rangka kerja. Penghalaan, penguraian borang dan output HTML ditulis dengan tangan. Kodnya lebih banyak, tetapi ia menunjukkan apa yang dilakukan oleh rangka kerja untuk anda.
- Data kotor. Tanda paun dalam harga hilang dalam fail pangkalan data. Kami menyahkodnya semasa membaca di satu tempat dan membiarkan fail itu.
- Mengambil tangkapan skrin tanpa mengambil alih desktop. Ia diambil dalam kontena Docker dengan pelayar tanpa kepala. Kontena itu tiada internet, jadi gambar kafe kelihatan sebagai kotak kelabu.

## Pembelajaran terbesar

Permintaan `GET` tidak boleh sekali-kali mengubah apa-apa, dan setiap nilai daripada pengguna atau pangkalan data mesti dilepaskan (escape) sebelum masuk ke dalam HTML. Kedua-duanya mudah dibuat dengan betul pada awalnya dan sukar ditambah kemudian.

## Apa yang akan kami lakukan secara berbeza

- Menambah penyuntingan kafe dan carian mengikut kawasan dan kemudahan.
- Membenarkan kontena tangkapan skrin memuatkan beberapa gambar contoh tempatan supaya gambar dipaparkan.
- Menambah token pada borang supaya laman web lain tidak dapat menghantar kepadanya.
