import matplotlib.pyplot as plt

hk_data = [
    (2, 0.01), (3, 0.01), (4, 0.01), (5, 0.01), (6, 0.01), (7, 0.02),
    (8, 0.04), (9, 0.09), (10, 0.16), (11, 0.36), (12, 0.87), (13, 2.18),
    (14, 5.13), (15, 11.70), (16, 28.34), (17, 71.63), (18, 166.78),
    (19, 416.80), (20, 910.32), (21, 2002.70), (22, 4405.94)
]

ls_data = [
    (2, 0.00), (3, 0.00), (4, 0.00), (5, 0.00), (6, 0.00), (7, 0.00),
    (8, 0.00), (9, 0.00), (10, 0.00), (11, 0.00), (12, 0.00), (13, 0.00),
    (14, 0.00), (15, 0.00), (16, 0.00), (17, 0.00), (18, 0.00), (19, 0.00),
    (20, 0.00), (21, 0.00), (22, 0.00), (23, 0.00), (24, 0.00), (25, 0.00),
    (26, 0.01), (27, 0.01), (28, 0.00), (29, 0.00), (30, 0.00), (31, 0.01),
    (32, 0.01), (33, 0.00), (34, 0.01), (35, 0.00), (36, 0.00), (37, 0.00),
    (38, 0.00), (39, 0.01), (40, 0.00), (41, 0.01), (42, 0.01), (43, 0.00),
    (44, 0.00), (45, 0.01), (46, 0.01), (47, 0.01), (48, 0.01), (49, 0.01),
    (50, 0.00), (100, 0.01), (1000, 0.10), (10000, 33.70),
    (20000, 242.53), (30000, 764.43), (40000, 1653.21), (50000, 2521.17),
    (60000, 3689.13)
]

hk_x_all, hk_y_all = zip(*hk_data)
ls_x_all, ls_y_all = zip(*ls_data)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(hk_x_all, [y / 60 for y in hk_y_all], marker='o', label='Held-Karp')
ax.plot(ls_x_all, [y / 60 for y in ls_y_all], marker='o', label='Local Search')

# Annotate HK points only for runtime >= 166.78 for readability
for x, y in hk_data:
    if y >= 166.78:
        ax.annotate(f"{y:.2f}s", (x, y / 60), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

# Annotate LS points only for x >= 100 for readability
for x, y in ls_data:
    if x >= 100:
        ax.annotate(f"{y:.2f}s", (x, y / 60), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

ax.set_xlabel("Number of Cities (log scale)")
ax.set_ylabel("Runtime (minutes)")
ax.set_title("TSP Runtime Comparison (Log Scale): Held-Karp vs Local Search")
ax.set_xscale('log')
ax.legend()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
file_path = "./tsp_runtime_comparison.png"
plt.savefig(file_path, dpi=300)
file_path