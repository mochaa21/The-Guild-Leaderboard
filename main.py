from typing import List

def urutkan_leaderboard(players: List[str]) -> List[str]:
    # TUGAS: Buat inner function untuk custom key
    def kalkulasi_kda(data: str) -> tuple:
        # 1. Pecah teksnya menggunakan .split('-')
        # 2. Ambil nama (indeks 0), kills (indeks 1), dan deaths (indeks 2)
        # 3. Ubah kills dan deaths jadi integer, lalu hitung net_score (kills - deaths)
        # 4. Return tuple-nya! (Ingat trik minus untuk net_score)
        
        pass # Hapus pass dan tulis logika lu di sini

    # Terapkan custom key ke dalam fungsi sorted
    return sorted(players, key=kalkulasi_kda)


# --- EKSEKUSI ---
data_server = ["Zane-10-5", "Bob-12-6", "Alice-15-10", "Charlie-8-1"]
hasil_ranking = urutkan_leaderboard(data_server)
print(hasil_ranking)