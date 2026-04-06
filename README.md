# 🧩 Maze Solver Animator

Animasi pencarian jalan keluar dari labirin menggunakan algoritma **BFS** dan **DFS** — Tugas Praktikum Kecerdasan Buatan.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Deskripsi

Program ini mensimulasikan dan memvisualisasikan proses pencarian jalur dari titik awal **(`.`)** menuju titik keluar **(`E`)** di dalam sebuah labirin. Setiap langkah eksplorasi ditampilkan secara animasi langsung di terminal dengan pewarnaan ANSI.

Visualisasi mengikuti tampilan dari PDF tugas praktikum, di mana:
- 🟩 **Hijau muda** = sel yang sudah dikunjungi (`x`)
- 🟨 **Kuning muda** = sel di frontier/antrian (`o`)
- 🟢 **Hijau terang** = jalur solusi akhir (`*`)

---

## 🖥️ Tampilan Program

```
  ╔══════════════════════════════════════════════╗
  ║          🧩  MAZE SOLVER ANIMATOR  🧩         ║
  ║     Tugas Praktikum - Pencarian Jalur        ║
  ╚══════════════════════════════════════════════╝

  🔍 BFS - Breadth First Search
  Langkah:   42 | Dikunjungi:   42 | Antrian:   15

  [labirin berwarna tampil di sini]

  [.] Titik Awal  [E] Titik Akhir  [x] Dikunjungi  [o] Frontier  [*] Solusi
```

---

## ⚙️ Cara Menjalankan

### Persyaratan
- Python **3.7** atau lebih baru
- Terminal yang mendukung **ANSI color codes** (Linux, macOS, Windows Terminal)

### Instalasi & Menjalankan

```bash
# Clone repositori
git clone https://github.com/username/maze-solver.git
cd maze-solver

# Jalankan program
python maze_solver.py
```

### Opsi Interaktif

Saat dijalankan, program akan menampilkan menu:

```
Pilih labirin:
  [1] Labirin Normal (19x27)
  [2] Labirin Sulit  (21x37)

Pilih algoritma:
  [1] BFS - Breadth First Search (jalur terpendek)
  [2] DFS - Depth First Search (eksplorasi dalam)
  [3] Bandingkan keduanya

Kecepatan animasi (detik, default=0.05):
```

---

## 🔬 Algoritma

### BFS (Breadth-First Search)
- Menggunakan struktur data **Queue (antrian)**
- Menjelajahi semua tetangga sebelum maju ke lapisan berikutnya
- **Menjamin jalur terpendek**
- Cocok untuk labirin yang membutuhkan solusi optimal

### DFS (Depth-First Search)
- Menggunakan struktur data **Stack**
- Menjelajahi satu jalur sedalam mungkin sebelum mundur
- **Tidak menjamin jalur terpendek**, tapi lebih hemat memori
- Cocok untuk mendeteksi apakah jalur ada atau tidak

### Perbandingan

| Kriteria            | BFS              | DFS              |
|---------------------|------------------|------------------|
| Struktur Data       | Queue            | Stack            |
| Jaminan Optimal     | ✅ Ya            | ❌ Tidak         |
| Penggunaan Memori   | Lebih besar      | Lebih kecil      |
| Kompleksitas Waktu  | O(V + E)         | O(V + E)         |
| Cocok untuk         | Jalur terpendek  | Deteksi jalur    |

---

## 🗺️ Format Labirin

Labirin direpresentasikan sebagai list of strings:

| Karakter | Arti           |
|----------|----------------|
| `#`      | Dinding        |
| ` `      | Jalan kosong   |
| `.`      | Titik awal     |
| `E`      | Titik keluar   |

### Contoh:

```python
MAZE = [
    "###########",
    "#.        #",
    "# ####### #",
    "#         #",
    "######### E",
    "###########",
]
```

Kamu bisa **membuat labirin sendiri** dengan mengedit variabel `MAZE_DEFAULT` atau `MAZE_HARD` di dalam file `maze_solver.py`.

---

## 📁 Struktur File

```
maze-solver/
│
├── maze_solver.py   # File utama program
└── README.md        # Dokumentasi ini
```

---

## 🧠 Konsep yang Dipelajari

- Representasi graf/grid sebagai struktur data
- Algoritma pencarian **BFS** dan **DFS**
- Teknik **backtracking** dalam pencarian jalur
- Visualisasi algoritma secara real-time di terminal

---

## 👨‍💻 Dibuat untuk

> **Tugas Praktikum** — Kecerdasan Buatan / Algoritma & Pemrograman  
> Membuat animasi pencarian jalan keluar dari titik awal (`.`) sampai titik (`E`)

---

## 📄 Lisensi

Proyek ini menggunakan lisensi [MIT](https://opensource.org/licenses/MIT).
