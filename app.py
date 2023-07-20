import ee
import geemap
import ipywidgets as widgets

# Inicializa la API de Google Earth Engine
ee.Initialize()

Map = geemap.Map()
Map.add_basemap('HYBRID')

region = Map.user_roi
if region is None:
    region = ee.Geometry.BBox(-89.7088, 42.9006, -89.0647, 43.2167)
    Map.addLayer(region, {}, 'Region')

Map.centerObject(region)
start_date = '2014-01-01'
end_date = '2023-01-01'

# Obtener serie temporal de imágenes para clasificación de cobertura terrestre
images = geemap.dynamic_world_timeseries(
    region, start_date, end_date, frequency='year', return_type="class"
)
vis_params = {
    "min": 0,
    "max": 8,
    "palette": [
        "#419BDF",
        "#397D49",
        "#88B053",
        "#7A87C6",
        "#E49635",
        "#DFC35A",
        "#C4281B",
        "#A59B8F",
        "#B39FE1",
    ],
}
Map.ts_inspector(images, left_vis=vis_params, date_format='YYYY')

Map.add_legend(title="Dynamic World Land Cover", builtin_legend='Dynamic_World')

Map.centerObject(region)

# Obtener serie temporal de imágenes para sombreado del relieve
images = geemap.dynamic_world_timeseries(
    region, start_date, end_date, frequency='year', return_type="hillshade"
)
Map.ts_inspector(images, date_format='YYYY')

Map

