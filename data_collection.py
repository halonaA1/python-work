import sys
import pandas as pd
import matplotlib.pyplot as plt

class CountryData:
    def __init__(self, name):
        self.name = name
        self.data = None

    def load_data(self, filepath):
        df = pd.read_csv(filepath)
        df = df[df["Area"] == self.name]
        df = df.pivot_table(index="Year", columns="Element", values="Value").reset_index()
        df = df.rename(columns={"Area harvested": "Area harvested", "Yield":"Yield", "Production":"Production"})
        self.data = df

    def show_table(self):
        print(f"\n---{self.name}---")
        print(self.data)


    def plot_yield(self):
        fig, ax = plt.subplots()
        ax.scatter(self.data["Year"], self.data["Yield"], color="tab:blue")
        ax.set_title(f"Yield over Years in {self.name}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Yield")
        ax.grid(True, linestyle="--", alpha=0.8)
        plt.show()

    def plot_area(self):
        fig, ax = plt.subplots()
        ax.bar(self.data["Year"], self.data["Area harvested"], color="tab:green")
        ax.set_title(f"Area harvested in {self.name}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Area harvested")
        ax.grid(True, linestyle="--", alpha=0.8)
        plt.show()

class Ghana(CountryData):
    def __init__(self):
        super().__init__("Ghana")

class IvoryCoast(CountryData):
    def __init__(self):
        super().__init__("Côte d'Ivoire")


def main():
    filepath = "./data/FAOSTAT_data_7-23-2022.csv"

    ghana = Ghana()
    ghana.load_data(filepath)
    ghana.show_table()
    ghana.plot_yield()
    ghana.plot_area()

    ivory_coast = IvoryCoast()
    ivory_coast.load_data(filepath)
    ivory_coast.show_table()
    ivory_coast.plot_yield()
    ivory_coast.plot_area()

    return 0

if __name__=="__main__":
    sys.exit(main())
