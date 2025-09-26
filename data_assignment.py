import sys
import matplotlib.pyplot as plt

def ivory_coast_table():
    col_labels = ["Year", "Area Harvested(ha)", "Yield(t/ha)", "Production"]
    data = [["" for _ in range(4)] for _ in range (10)]
    fig, ax = plt.subplots()
    ax.axis("off")
    table = ax.table(cellText=data, colLabels=col_labels, loc="center")

    table.set_fontsize(12)
    table.scale(1, 1)
    plt.show()

def ghana_table():
    col_labels = ["Year", "Area Harvested(ha)", "Yield(t/ha)", "Production"]
    data = [["" for _ in range(4)] for _ in range(10)]
    fig, ax= plt.subplots()
    ax.axis("off")
    table = ax.table(cellText=data, colLabels=col_labels, loc="center")

    table.set_fontsize(13)
    table.scale(1, 1)
    plt.show()

def main():
    ivory_coast_table()
    ghana_table()

    return 0

if __name__ =="__main__":
    sys.exit(main())

