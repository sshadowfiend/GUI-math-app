import matplotlib.pyplot as plt


def plot(t: list[float], u: list[float], n: int, name: str) -> None:
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 4)
    ax.set_xlabel("t")
    ax.set_ylabel(name)
    ax.set_facecolor("#90CAF9")
    plt.gcf().set_facecolor('#EDF5E1')
    ax.grid(color='#000000')
    ax.plot(t, u, color='#000000', linewidth=3)
    plt.savefig(f"plot_{name}_{n}.png")
