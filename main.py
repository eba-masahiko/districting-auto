import os
from src.fetch_population import fetch_population
from src.load_boundaries import load_boundaries
from src.build_adjacency import build_graph
from src.run_districting import run_districting
from src.evaluate import evaluate_districts
from src.visualize import plot_districts
from src.publish_map import publish_map
from src.config import OUTPUT_DIR

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Fetching population...")
    pop_df = fetch_population()
    print("Loading boundaries...")
    gdf = load_boundaries()
    print("Merging...")
    gdf = gdf.merge(pop_df, on="code", how="left")
    print("Building adjacency graph...")
    graph = build_graph(gdf)
    print("Running districting...")
    partition = run_districting(gdf, graph)
    print("Evaluating...")
    metrics = evaluate_districts(partition)
    print("Visualizing...")
    plot_districts(partition, metrics)
    print("Publishing map...")
    publish_map()
    print("Done.")

if __name__ == "__main__":
    main()
