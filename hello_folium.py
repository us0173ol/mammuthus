import folium

map_mn = folium.Map(location=[40, -120], zoom_start=3)

# folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)

map_mn.save('map.html')
