import matplotlib.pyplot as plt
from matplotlib import font_manager


def plot(t: list[float], u: list[float], n: int, name: str) -> None:

    font_dirs = ["C:/Users/user/Desktop/Учеба/Курсач"]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)
    plt.rcParams["font.family"] = "Nunito"

    fig, ax = plt.subplots()
    fig.set_size_inches(5, 4)
    ax.set_xlabel("t")
    ax.set_ylabel(name)
    ax.set_facecolor("#90CAF9")
    plt.gcf().set_facecolor('#EDF5E1')
    ax.grid(color='#000000')
    ax.plot(t, u, color='#000000', linewidth=3)
    plt.savefig(f"plot_{name}_{n}.png")
