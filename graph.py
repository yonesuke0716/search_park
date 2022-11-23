import japanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font="IPAexGothic")

class Graph:
    def __init__(self, x_min=None, x_max=None, y_min=None ,y_max=None,
                 g_title="", x_label="", y_label="", x_ticks=None, y_ticks=None):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(g_title)
        if x_min is None and x_max is None:
            pass
        elif x_min is None:
            self.ax.set_xlim(right=x_max)
        elif x_max is None:
            self.ax.set_xlim(left=x_min)
        else:
            self.ax.set_xlim([x_min, x_max])
        if y_min is None and y_max is None:
            pass
        elif y_min is None:
            self.ax.set_ylim(top=y_max)
        elif y_max is None:
            self.ax.set_ylim(buttom=y_min)
        else:
            self.ax.set_ylim([y_min, y_max])
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        if x_ticks is not None:
            self.ax.set_xticks(x_ticks)
        if y_ticks is not None:
            self.ax.set_yticks(y_ticks)

    # 縦棒グラフ
    def plot_bar(self, x, y, layout):
        self.ax.bar(x, y)
        layout.pyplot(self.fig)


