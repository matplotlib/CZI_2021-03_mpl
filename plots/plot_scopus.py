import pandas as pd
import matplotlib.pyplot as plt
import textwrap

fig, ax = plt.subplots(constrained_layout=True)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)


data = pd.read_csv("matplotlib.csv", index_col=0)

targets = [
    ("Biochemistry, Genetics and Molecular Biology", 0),
    ("Neuroscience", -9),
    ("Medicine", -4),
    ("Agricultural and Biological Sciences", 8),
    ("Immunology and Microbiology", 5),
    ("Psychology", 2),
    ("Health Professions ", -5),
    ("Pharmacology, Toxicology and Pharmaceutics", 7),
]

# for k, offset in zip(list(data), [0]*len(data.columns))
for k, offset in targets:
    (ln,) = ax.plot(data[k], label=k)
    # ln = ax.bar(data[k].index, height=data[k], label=k)
    ax.annotate(
        "\n".join(textwrap.wrap(k, 25)),
        (1, data[k].iloc[-1]),
        xycoords=ax.get_yaxis_transform(),
        xytext=(1, offset),
        textcoords="offset points",
        color=ln.get_color(),
        va="center",
    )

ax.set_ylim(ymin=0)
ax.set_xlim(2012, 2020)
ax.set_xlabel("year")
ax.set_ylabel("# articles mentioning Matplotlib")
ax.set_title("Matplotlib mentions in Scopus by field")
ax.grid(True, axis="y", which="major")
fig.savefig("scopus_mentions.png", dpi=200)
