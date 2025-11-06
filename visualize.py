import geopandas as gpd
import matplotlib.pyplot as plt
from src.config import OUTPUT_DIR

def plot_districts(partition, metrics):
    gdf = gpd.GeoDataFrame({"geometry": [p for p in partition.parts]}, crs="EPSG:4326")
    fig, ax = plt.subplots(figsize=(6, 8))
    gdf.plot(ax=ax, cmap="tab20")
    plt.title(f"Max/Min population ratio: {metrics['ratio']:.2f}")
    plt.savefig(f"{OUTPUT_DIR}/summary.png", bbox_inches="tight")
