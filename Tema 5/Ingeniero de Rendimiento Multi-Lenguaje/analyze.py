import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

dfs = [pd.read_csv(f"results/{name}.csv") for name in
       ["python_antlr", "java_antlr", "c_flexbison"]]
df = pd.concat(dfs, ignore_index=True)
df.to_csv("results/combined.csv", index=False)

# Drop the first repetition per (file, lang) group to avoid JIT/cold-start
# warm-up bias, especially significant for the Java (JVM) run.
df_warm = df[df["run"] != 0].copy()

summary = (
    df_warm.groupby("lang")["time_ms"]
    .agg(["mean", "median", "std", "min", "max", "count"])
    .reset_index()
    .sort_values("mean")
)
summary.to_csv("results/summary_by_lang.csv", index=False)
print(summary.to_string(index=False))

# Per-file mean time per language (using warm runs)
per_file = (
    df_warm.groupby(["file", "lang"])["time_ms"].mean().reset_index()
)
pivot = per_file.pivot(index="file", columns="lang", values="time_ms")
pivot = pivot.sort_index(key=lambda idx: [int(x.split("_")[-1].split(".")[0]) for x in idx])
pivot.to_csv("results/per_file_mean.csv")
print("\nPer-file mean (ms):")
print(pivot.to_string())

ok_summary = df.groupby("lang")["ok"].apply(lambda s: (s.astype(str).str.lower() == "true").mean())
print("\nFraction of runs that parsed successfully (ok=true) per lang:")
print(ok_summary.to_string())

# --- Chart 1: bar chart of mean time per language (log scale, overall) ---
colors = {"c_flexbison": "#2E86AB", "java_antlr": "#E07A5F", "python_antlr": "#81B29A"}
labels = {"c_flexbison": "C (Flex/Bison)", "java_antlr": "Java (ANTLR)", "python_antlr": "Python (ANTLR)"}

fig, ax = plt.subplots(figsize=(7, 5))
order = summary["lang"].tolist()
means = summary["mean"].tolist()
stds = summary["std"].tolist()
bar_colors = [colors[l] for l in order]
bars = ax.bar([labels[l] for l in order], means, yerr=stds, capsize=5,
              color=bar_colors, edgecolor="black")
ax.set_yscale("log")
ax.set_ylabel("Tiempo medio de parseo por archivo (ms, escala log)")
ax.set_title("Comparación de tiempo de ejecución por metacompilador/lenguaje\n(10 archivos docker-compose, 199 repeticiones c/u, sin warm-up)")
for b, m in zip(bars, means):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.15,
             f"{m:.4f} ms", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("results/chart_mean_by_lang.png", dpi=150)
plt.close()

# --- Chart 2: line chart, per-file mean, all 3 languages ---
fig, ax = plt.subplots(figsize=(9, 5))
x_labels = pivot.index.tolist()
x = range(len(x_labels))
for lang in ["c_flexbison", "java_antlr", "python_antlr"]:
    ax.plot(x, pivot[lang], marker="o", label=labels[lang], color=colors[lang])
ax.set_xticks(list(x))
ax.set_xticklabels([f.replace("docker_test_", "").replace(".yml", "") for f in x_labels])
ax.set_xlabel("Archivo de prueba (docker_test_N.yml)")
ax.set_ylabel("Tiempo medio de parseo (ms)")
ax.set_yscale("log")
ax.set_title("Tiempo de parseo por archivo y por implementación")
ax.legend()
plt.tight_layout()
plt.savefig("results/chart_per_file.png", dpi=150)
plt.close()

print("\nGraficas guardadas en results/chart_mean_by_lang.png y results/chart_per_file.png")
