import geopandas as gpd
from src.config import BOUNDARY_FILE

def load_boundaries():
    gdf = gpd.read_file(BOUNDARY_FILE)
    gdf = gdf.rename(columns={"N03_007": "code"})
    return gdf
