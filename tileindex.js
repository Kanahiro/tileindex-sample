//Library Import
var fs = require('fs')
var cover = require('@mapbox/tile-cover');

//Load local GeoJSON file
var geojson_str = fs.readFileSync('./dissolved_hokkaido.geojson')
var geojson_obj = JSON.parse(geojson_str);

//use tile-cover
var limits = {
    min_zoom: 7,
    max_zoom: 7
};
var tile_index = []
tile_index = cover.tiles(geojson_obj.features[0].geometry, limits)

console.log(tile_index)