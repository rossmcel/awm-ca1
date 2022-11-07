const copy =
    "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });

const marker = L.marker();

map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));
   
map.on('click', function (e) {
    console.log("Map Clicked");
    marker
        .setLatLng(e.latlng)
        .addTo(map);
    console.log(marker);
    //document.getElementById("selectedLocationLat").innerHTML = marker._latlng.lat;
    //document.getElementById("selectedLocationLng").innerHTML = marker._latlng.lng;
    const latElement = document.getElementById("id_lat");
    const lngElement = document.getElementById("id_lng");
    latElement.value = marker._latlng.lat;
    lngElement.value = marker._latlng.lng;
});

async function load_markers() {
    const markers_url = `/api/WorldBorder/?in_bbox=${map
        .getBounds()
        .toBBoxString()}`;
    const response = await fetch(markers_url);
    const geojson = await response.json();
    return geojson;
}

async function render_markers() {
    const markers = await load_markers();
    L.geoJSON(markers)
        .bindPopup((layer) => layer.feature.properties.name)
        .addTo(map);
}

map.on("moveend", render_markers);
