# This file was run with a different output.txt file than the one uploaded, as explained
# in the README, since the distance matrixes were hardcoded. The output.txt tour distance values
# used for this chart are shown since they are hardcoded

import random
import matplotlib.pyplot as plt

hk_lengths = [
    2, 6, 7, 11, 11, 8, 13, 20, 20, 22, 15, 19, 23, 22, 23, 23, 22, 29, 25, 28, 33
]
ls_lengths = [
    8, 10, 18, 17, 18, 20, 24, 31, 26, 28, 23, 21, 32, 30, 35, 36, 38, 41, 45, 44, 39, 44, 51, 50, 49,
    62, 54, 57, 61, 73, 82, 74, 78, 88, 90, 91, 79, 86, 102, 96, 98, 92, 112, 125, 109, 116, 125, 131,
    128, 138
]

hk_x = list(range(2, 2 + len(hk_lengths)))
ls_x = list(range(2, 2 + len(ls_lengths)))

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(hk_x, hk_lengths, marker='o', label='Held-Karp')
ax.plot(ls_x, ls_lengths, marker='o', label='Local Search')

ax.set_xlabel("Number of Cities")
ax.set_ylabel("Tour Length")
ax.set_title("TSP Tour Length Comparison: Held-Karp vs Local Search")
ax.legend()
ax.grid(True)

plt.tight_layout()
file_path = "./tsp_tour_length_comparison.png"
plt.savefig(file_path, dpi=300)
file_path
