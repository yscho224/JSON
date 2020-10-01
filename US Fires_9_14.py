import json

in_file = open('US_fires_9_14.json','r')
out_file = open('readable_US_fires_9_14.json','w')


fire_9_14_data = json.load(in_file)


json.dump(fire_9_14_data, out_file, indent =4)


list_of_fires = fire_9_14_data[0:]


brights,lons, lats = [],[],[]

for fr in list_of_fires:
    lat = fr['latitude']
    lon = fr['longitude']
    brig = fr['brightness']
    if brig > 450:
        brights.append(brig)
    lons.append(lon)
    lats.append(lat)


print(brights[:10])

print(lons[:10])


print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size': [brig/25 for brig in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Brightness'}
    },
}]


my_layout = Layout(title = 'US Fires - 9/14/2020 through 9/20/2020')

fig = {'data':data , 'layout':my_layout}

offline.plot(fig, filename = 'US Fires_2.html')


