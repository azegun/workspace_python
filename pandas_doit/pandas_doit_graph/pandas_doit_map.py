import folium as fol
import  pandas as pd
# daegu_map = fol.Map(location=[35.87, 128.60], zoom_start=12)
# daegu_map.save('../pandas_doit_graph/save/map.html')
#
# # Terrain 산악지형
# daegu_map1 = fol.Map(location=[35.87, 128.60], zoom_start=12, tiles='Stamen Terrain')
# daegu_map1.save('../pandas_doit_graph/save/map1.html')
#
# # Toner 강지형
# daegu_map2 = fol.Map(location=[35.87, 128.60], zoom_start=15, tiles='Stamen Toner')
# daegu_map2.save('../pandas_doit_graph/save/map2.html')

df = pd.read_excel('../pandas_doit_graph/data/영남인재교육원위치.xlsx')
print(df)

younam_map = fol.Map(location=[35.87, 128.60], zoom_start=13)

print(zip(df['Unnamed: 0']))
for name, lat, lng in zip(df['Unnamed: 0'], df['위도'], df['경도']):
    print(name, lat, lng)
    fol.Marker([lat, lng], popup=name).add_to(younam_map)
younam_map.save('../pandas_doit_graph/save/youngnam.html')

