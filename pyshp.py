import shapefile
import pandas as pd
ireland = gpd.read_file(r"/Ireland/ie_1km.shp")
confirmed = pd.read_csv(confirmed_file)

