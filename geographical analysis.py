import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

# Group by city and calculate total sales
city_sales = data.groupby('ship-city')['Amount'].sum().reset_index()

# Create a map centered around the average coordinates
map_center = [20.5937, 78.9629]  # Coordinates for India
m = folium.Map(location=map_center, zoom_start=5)

# Add city sales as markers on the map
for _, row in city_sales.iterrows():
    folium.CircleMarker(location=[row['Latitude'], row['Longitude']],
                        radius=5,
                        popup=f"City: {row['ship-city']}<br>Sales: {row['Amount']}",
                        color='blue',
                        fill=True).add_to(m)

# Save the map as an HTML file
m.save('city_sales_map.html')
