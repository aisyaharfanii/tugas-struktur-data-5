"""
Maze Solver - Animasi Pencarian Jalan Keluar
Tugas Praktikum: Mencari jalan dari titik (.) ke titik (E)
Algoritma: BFS (Breadth-First Search) & DFS (Depth-First Search)
"""

import os
import time
import sys
from collections import deque

# ──────────────────────────────────────────────
# KONFIGURASI WARNA TERMINAL (ANSI)
# ──────────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    WALL    = "\033[48;5;17m  \033[0m"        # Biru gelap (dinding)
    PATH    = "\033[48;5;255m  \033[0m"        # Putih (jalan kosong)
    START   = "\033[48;5;36m\033[97m . \033[0m"  # Hijau tua (titik awal)
    END     = "\033[48;5;214m\033[97m E \033[0m"  # Oranye (titik akhir)
    VISITED = "\033[48;5;152m\033[36m x \033[0m"  # Hijau muda (sudah dikunjungi)
    FRONTIER= "\033[48;5;222m\033[33m o \033[0m"  # Kuning muda (frontier/antrian)
    RESULT  = "\033[48;5;120m\033[32m * \033[0m"  # Hijau terang (jalur solusi)

# ──────────────────────────────────────────────
# DEFINISI LABIRIN
# '#' = dinding, ' ' = jalan, '.' = start, 'E' = exit
# ──────────────────────────────────────────────
MAZE_DEFAULT = [
    "###########################",
    "#.  #       #   #         #",
    "# # # ##### # # # ####### #",
    "# #   #     # #   #       #",
    "# ##### ##### ##### #######",
    "#       #     #     #     #",
    "####### # ##### ##### ### #",
    "#     # #       #     #   #",
    "# ### # ####### # ##### ###",
    "#   #   #     # #   #     #",
    "### ##### ### # ### # ### #",
    "#   #     #   #   # #   # #",
    "# ### ##### ##### # ### # #",
    "#     #     #     #     # #",
    "######### ### ########### #",
    "#         #   #           #",
    "# ######### ### ########### ",
    "#           #             E#",
    "###########################",
]

# Labirin alternatif lebih besar
MAZE_HARD = [
    "#####################################",
    "#.  #   #       #   #   #           #",
    "# # # # # ##### # # # # ########### #",
    "# #   # #   #   # #   #         #   #",
    "# ##### ### # ### ########### ### ###",
    "#       #   # #   #         # #   # #",
    "####### # ### # ### ####### # ### # #",
    "#     # #     #   # #     # #   # # #",
    "# ### ########### # # ### # ### ### #",
    "#   #         #   # # # # #   #     #",
    "### ######### # ### # # # ### #######",
    "#   #         #   # # # #   #       #",
    "# ### ########### # # ##### ####### #",
    "#     #           # #       #       #",
    "# ##### ########### ######### ##### #",
    "#   #   #         # #       # #     #",
    "### # ### ####### # # ##### # # ### #",
    "#   #     #     # #   #   # # # # # #",
    "# ######### ### # ##### # # # # # # #",
    "#           #             #       # E#",
    "#####################################",
]

def find_positions(maze):
    """Cari posisi titik awal (.) dan akhir (E)"""
    start = end = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == '.':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return start, end

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_maze(maze, visited=set(), frontier=set(), path=set(), start=None, end=None):
    """Tampilkan labirin dengan warna di terminal"""
    output = []
    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            pos = (r, c)
            if pos == start:
                line += Color.START
            elif pos == end:
                line += Color.END
            elif pos in path:
                line += Color.RESULT
            elif pos in frontier:
                line += Color.FRONTIER
            elif pos in visited:
                line += Color.VISITED
            elif cell == '#':
                line += Color.WALL
            else:
                line += Color.PATH
        output.append(line)
    return "\n".join(output)

def bfs_solve(maze, start, end, delay=0.05, show_animation=True):
    """
    BFS - Breadth First Search
    Menjamin jalur terpendek.
    Frontier divisualisasi sebagai antrian (queue).
    """
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    queue = deque()
    queue.append((start, [start]))
    visited = {start}
    frontier = set()
    step = 0

    while queue:
        (r, c), path = queue.popleft()
        frontier = {item[0] for item in queue}
        step += 1

        if show_animation and step % 2 == 0:
            clear_screen()
            print(f"\n  🔍 BFS - Breadth First Search")
            print(f"  Langkah: {step:4d} | Dikunjungi: {len(visited):4d} | Antrian: {len(queue):4d}\n")
            print(render_maze(maze, visited, frontier, set(), start, end))
            print(f"\n  {Color.START}  {Color.RESET} Titik Awal  "
                  f"{Color.END}  {Color.RESET} Titik Akhir  "
                  f"{Color.VISITED}  {Color.RESET} Dikunjungi  "
                  f"{Color.FRONTIER}  {Color.RESET} Frontier  "
                  f"{Color.RESULT}  {Color.RESET} Solusi")
            time.sleep(delay)

        if (r, c) == end:
            # Tampilkan jalur solusi
            path_set = set(path)
            for _ in range(3):
                clear_screen()
                print(f"\n  ✅ BFS - Jalur Ditemukan!")
                print(f"  Langkah: {step:4d} | Panjang jalur: {len(path)} sel\n")
                print(render_maze(maze, visited, set(), path_set, start, end))
                print(f"\n  Solusi ditemukan dalam {step} langkah eksplorasi!")
                time.sleep(0.4)
            return path, step

        # Arah: atas, bawah, kiri, kanan
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and maze[nr][nc] != '#':
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return None, step

def dfs_solve(maze, start, end, delay=0.05, show_animation=True):
    """
    DFS - Depth First Search
    Tidak menjamin jalur terpendek, tapi lebih hemat memori.
    Frontier divisualisasi sebagai stack.
    """
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    stack = [(start, [start])]
    visited = set()
    frontier = set()
    step = 0

    while stack:
        (r, c), path = stack.pop()

        if (r, c) in visited:
            continue
        visited.add((r, c))
        frontier = {item[0] for item in stack}
        step += 1

        if show_animation and step % 2 == 0:
            clear_screen()
            print(f"\n  🔍 DFS - Depth First Search")
            print(f"  Langkah: {step:4d} | Dikunjungi: {len(visited):4d} | Stack: {len(stack):4d}\n")
            print(render_maze(maze, visited, frontier, set(), start, end))
            print(f"\n  {Color.START}  {Color.RESET} Titik Awal  "
                  f"{Color.END}  {Color.RESET} Titik Akhir  "
                  f"{Color.VISITED}  {Color.RESET} Dikunjungi  "
                  f"{Color.FRONTIER}  {Color.RESET} Stack  "
                  f"{Color.RESULT}  {Color.RESET} Solusi")
            time.sleep(delay)

        if (r, c) == end:
            path_set = set(path)
            for _ in range(3):
                clear_screen()
                print(f"\n  ✅ DFS - Jalur Ditemukan!")
                print(f"  Langkah: {step:4d} | Panjang jalur: {len(path)} sel\n")
                print(render_maze(maze, visited, set(), path_set, start, end))
                print(f"\n  Solusi ditemukan dalam {step} langkah eksplorasi!")
                time.sleep(0.4)
            return path, step

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and maze[nr][nc] != '#':
                    stack.append(((nr, nc), path + [(nr, nc)]))

    return None, step

def print_banner():
    banner = """
  ╔══════════════════════════════════════════════╗
  ║          🧩  MAZE SOLVER ANIMATOR  🧩         ║
  ║     Tugas Praktikum - Pencarian Jalur        ║
  ╚══════════════════════════════════════════════╝
    """
    print(banner)

def main():
    clear_screen()
    print_banner()

    print("  Pilih labirin:")
    print("  [1] Labirin Normal (19x27)")
    print("  [2] Labirin Sulit  (21x37)")
    maze_choice = input("\n  Pilihan (1/2, default=1): ").strip() or "1"
    maze = MAZE_DEFAULT if maze_choice != "2" else MAZE_HARD

    print("\n  Pilih algoritma:")
    print("  [1] BFS - Breadth First Search (jalur terpendek)")
    print("  [2] DFS - Depth First Search (eksplorasi dalam)")
    print("  [3] Bandingkan keduanya")
    algo_choice = input("\n  Pilihan (1/2/3, default=1): ").strip() or "1"

    delay_input = input("\n  Kecepatan animasi (detik, default=0.05): ").strip()
    delay = float(delay_input) if delay_input else 0.05

    start, end = find_positions(maze)
    if not start or not end:
        print("  ❌ Error: Titik awal (.) atau akhir (E) tidak ditemukan!")
        return

    print(f"\n  Titik awal : baris {start[0]}, kolom {start[1]}")
    print(f"  Titik akhir: baris {end[0]}, kolom {end[1]}")
    input("\n  Tekan Enter untuk mulai animasi...")

    results = {}

    if algo_choice in ("1", "3"):
        t0 = time.time()
        path, steps = bfs_solve(maze, start, end, delay=delay)
        elapsed = time.time() - t0
        results["BFS"] = (path, steps, elapsed)
        if algo_choice == "3":
            input("\n  Tekan Enter untuk lanjut ke DFS...")

    if algo_choice in ("2", "3"):
        t0 = time.time()
        path, steps = dfs_solve(maze, start, end, delay=delay)
        elapsed = time.time() - t0
        results["DFS"] = (path, steps, elapsed)

    # Ringkasan perbandingan
    if len(results) > 1:
        clear_screen()
        print_banner()
        print("  ┌──────────────────────────────────────────┐")
        print("  │              PERBANDINGAN HASIL           │")
        print("  ├──────────────┬─────────────┬─────────────┤")
        print("  │  Algoritma   │  Langkah    │  Panjang    │")
        print("  ├──────────────┼─────────────┼─────────────┤")
        for algo, (path, steps, elapsed) in results.items():
            plen = len(path) if path else "Tidak ada"
            print(f"  │  {algo:<12}│  {steps:<11}│  {plen:<11}│")
        print("  └──────────────┴─────────────┴─────────────┘")
        print()

    print("  Program selesai. Terima kasih!\n")

if __name__ == "__main__":
    main()
