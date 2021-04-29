import folium


m = folium.Map(location=[53.350140, -6.266155])



folium.Marker(
    location=[53.350140, -6.266155],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[53.45972 ,-6.21806],
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.Marker(
    location=[53.0853 ,-6.82],
    popup="Some Other Location",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(m)
m.save("index2.html")