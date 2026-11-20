[English](Home) · [Dansk](Home-da) · **Bahasa Melayu**

# Laman web Kafe dan Wifi

Sebuah laman web kecil yang menyenaraikan kafe dengan wifi dan palam kuasa untuk kerja jarak jauh. Ia ialah penyelesaian bagi tugasan hari ke-88 kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp". Ia hanya memerlukan Python 3.13 atau lebih baharu: tiada rangka kerja dan tiada kebergantungan semasa dijalankan.

Laman web ini dibina dalam tiga langkah. Setiap langkah mempunyai tangkapan skrin dan satu halaman yang menerangkan apa yang kita pelajari.

| Langkah | Apa yang ditambah | Halaman |
| --- | --- | --- |
| 1 | Halaman utama menyenaraikan semua kafe dalam `cafes.db` | [Langkah 1: Senaraikan kafe](Step-1-List-Cafes-ms) |
| 2 | Borang dengan pengesahan menambah kafe | [Langkah 2: Tambah kafe](Step-2-Add-Cafe-ms) |
| 3 | Halaman pengesahan memadam kafe | [Langkah 3: Padam kafe](Step-3-Delete-Cafe-ms) |

Tugasan meminta refleksi pada akhirnya; refleksi kami ada di [Refleksi](Reflection-ms).

## Jalankan

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m cafe_wifi
```

Buka <http://127.0.0.1:8000>. README repositori mempunyai arahan untuk Windows dan Linux, untuk ujian dan untuk tangkapan skrin.
