# OpenCV Color Spaces and Detection

Praktikum pengolahan citra digital menggunakan Python dan OpenCV untuk mempelajari konversi ruang warna, pemisahan kanal BGR, serta deteksi warna merah dan biru menggunakan HSV.

Repository ini berisi empat skrip latihan yang dapat dijalankan secara terpisah, beserta gambar contoh `gedungpnl.jpeg`.

## Materi Praktikum

| File | Materi | Hasil |
| --- | --- | --- |
| `converting_color.py` | Konversi gambar BGR ke RGB, HSV, grayscale, dan Lab | Jendela gambar asli dan hasil konversi ditampilkan bertahap |
| `perbedaan_rgb.py` | Pemisahan kanal dengan `cv2.split()` | Gambar asli serta intensitas kanal biru, hijau, dan merah |
| `deteksi_merah_HSV.py` | Seleksi warna merah berdasarkan rentang HSV | Area gambar yang memenuhi rentang dipertahankan, area lainnya menjadi hitam |
| `deteksi_biru_HSV.py` | Seleksi warna biru berdasarkan rentang HSV | Area gambar yang memenuhi rentang dipertahankan, area lainnya menjadi hitam |

## Kebutuhan

- Python 3 dan pip.
- Library `opencv-python` dan `numpy`.
- Lingkungan desktop untuk menampilkan jendela melalui `cv2.imshow()`.

## Struktur Project

```text
opencv-color-spaces-and-detection/
├── converting_color.py
├── perbedaan_rgb.py
├── deteksi_merah_HSV.py
├── deteksi_biru_HSV.py
├── gedungpnl.jpeg
└── README.md
```

## Instalasi dan Persiapan

1. Clone atau unduh repository, lalu buka terminal di folder project.

2. Instal library yang dibutuhkan:

   ```bash
   python -m pip install opencv-python numpy
   ```

3. Pastikan `gedungpnl.jpeg` berada di folder yang sama dengan skrip. Gambar contoh sudah tersedia di project ini.

## Cara Menjalankan

Jalankan salah satu perintah berikut dari folder project:

```bash
python converting_color.py
python perbedaan_rgb.py
python deteksi_merah_HSV.py
python deteksi_biru_HSV.py
```

Setiap skrip menampilkan hasil di jendela gambar. Tekan tombol keyboard saat jendela aktif untuk melanjutkan ke tampilan berikutnya atau menyelesaikan program. Hasil pengolahan hanya ditampilkan dan belum disimpan sebagai file.

## Alur Deteksi Warna

1. Baca gambar menggunakan `cv2.imread()`.
2. Konversi gambar dari BGR ke HSV menggunakan `cv2.cvtColor()`.
3. Tentukan batas bawah dan batas atas warna dalam array NumPy.
4. Buat mask dengan `cv2.inRange()` untuk memilih piksel dalam rentang tersebut.
5. Terapkan mask pada gambar asli menggunakan `cv2.bitwise_and()`.

Rentang yang digunakan dalam skrip saat ini:

| Warna | Batas bawah (H, S, V) | Batas atas (H, S, V) |
| --- | --- | --- |
| Merah | `(0, 120, 70)` | `(10, 255, 255)` |
| Biru | `(90, 150, 80)` | `(130, 255, 180)` |

Rentang ini dapat disesuaikan dengan gambar dan kondisi pencahayaan. Pada gambar 8-bit yang dikonversi menggunakan `cv2.COLOR_BGR2HSV`, OpenCV menggunakan nilai H dari 0–179, sedangkan S dan V dari 0–255.

## Catatan Penggunaan

- OpenCV membaca gambar berwarna dalam urutan **BGR** (Blue, Green, Red).
- Setiap kanal yang ditampilkan oleh `perbedaan_rgb.py` merupakan gambar satu kanal. Tampilannya berupa grayscale yang menunjukkan intensitas kanal tersebut.
- `cv2.imshow()` menganggap gambar tiga kanal sebagai BGR. Karena `converting_color.py` menampilkan array RGB, HSV, dan Lab secara langsung, warna pada jendela merupakan visualisasi nilai kanal dan tidak selalu sama dengan warna asli. Grayscale ditampilkan sebagai citra satu kanal.
- Warna merah berada di kedua ujung rentang Hue. Skrip merah saat ini hanya memilih H dari 0–10; untuk mencakup merah di dekat ujung atas, tambahkan mask kedua, misalnya H dari 170–179, lalu gabungkan kedua mask.
- Jalankan skrip dari folder project karena nama gambar dibaca relatif terhadap folder kerja terminal.
- Jika mengganti gambar, sesuaikan nama file pada skrip. Skrip belum memiliki pemeriksaan untuk gambar yang gagal dibaca.
