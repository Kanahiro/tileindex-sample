import json

import shapely
import tiletanic

if __name__ == "__main__":
    zoomlevel = 7

    #geojson読み込み
    geojson_dict = {}
    with open('./dissolved_hokkaido_3857.geojson', 'r') as f:
        geojson_dict = json.load(f)

    #ディゾルブにより地物数は1
    feature = geojson_dict['features'][0]['geometry']
    feature_shape = shapely.geometry.shape(feature)

    #タイルスキームの初期化
    tiler = tiletanic.tileschemes.WebMercator()

    covering_tiles_itr = tiletanic.tilecover.cover_geometry(tiler, feature_shape, zoomlevel)
    covering_tiles = []
    for tile in covering_tiles_itr:
        tile_xyz = [tile[0], tile[1], tile[2]]
        covering_tiles.append(tile_xyz)

    print(covering_tiles)