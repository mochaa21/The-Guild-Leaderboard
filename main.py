from typing import List

def urutkan_leaderboard(players: List[str]) -> List[str]:
    def kalkulasi_kda(data: str) -> tuple:
        raw_data = data.split('-')
        name = raw_data[0]
        kills = int(raw_data[1])
        deaths = int(raw_data[2])
        new_data = (kills - deaths)
        return (-new_data, name)

    # Terapkan custom key ke dalam fungsi sorted
    return sorted(players, key=kalkulasi_kda)


# --- EKSEKUSI ---
data_server = ["Zane-10-5", "Bob-12-6", "Alice-15-10", "Charlie-8-1"]
hasil_ranking = urutkan_leaderboard(data_server)
print(hasil_ranking)