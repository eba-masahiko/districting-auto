import folium, geopandas as gpd
from src.config import OUTPUT_DIR

def publish_map(geojson_path="outputs/districts.geojson", output_html="outputs/summary.html"):
    gdf = gpd.read_file(geojson_path)
    total_pop = gdf["population"].sum()
    avg_pop = total_pop / len(gdf)
    gdf["vote_weight"] = avg_pop / gdf["population"]
    center = gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()
    m = folium.Map(location=center, zoom_start=6, tiles="cartodbpositron")
    folium.Choropleth(
        geo_data=gdf,
        data=gdf,
        columns=["district", "vote_weight"],
        key_on="feature.properties.district",
        fill_color="YlGnBu",
        legend_name="一票の重み（平均=1.0）",
        fill_opacity=0.7,
        line_opacity=0.2,
    ).add_to(m)
    for _, row in gdf.iterrows():
        popup_text = f"<b>区番号:</b> {row['district']}<br><b>人口:</b> {int(row['population']):,}<br><b>一票の重み:</b> {row['vote_weight']:.3f}"
        folium.Marker(
            location=[row.geometry.centroid.y, row.geometry.centroid.x],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
    m.save(output_html)
    print(f"✅ 地図を {output_html} に出力しました。")
