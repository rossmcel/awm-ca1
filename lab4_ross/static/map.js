const copy =
    "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 2 });

const marker = L.marker();

// map.locate()
//     .on("locationfound", (e) => map.setView(e.latlng, 8))
//     .on("locationerror", () => map.setView([0, 0], 5));

map.locate({setView: true, maxZoom: 16});

function onClickCurentMarker(e) {
    const currentLocationMarker = L.marker()
        .setLatLng(e.latlng);

    const markerNameElement = document.getElementById("id_name");
    const latElement = document.getElementById("id_lat");
    const lngElement = document.getElementById("id_lng");
    markerNameElement.value = "Current Location";
    latElement.value = currentLocationMarker._latlng.lat;
    lngElement.value = currentLocationMarker._latlng.lng;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

function onLocationFound(e) {
    const radius = e.accuracy;
    const currentLocationMarker = L.marker();
    currentLocationMarker
    .setLatLng(e.latlng)
    .addTo(map)
    .on('click', onClickCurentMarker)
    .bindPopup("You are within " + radius + " meters of this point<br><h6 style='text-align: center'>Location added to database<h6>").openPopup();

    const ajaxData = {
        lat: currentLocationMarker._latlng.lat,
        lng: currentLocationMarker._latlng.lng,
      }
    $.ajax({
        url: "/map/add/",
        type: "POST",
        dataType: "json",
        data: JSON.stringify({payload: ajaxData,}),
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error.responseText);
        }
      });

    const markerNameElement = document.getElementById("id_name");
    const latElement = document.getElementById("id_lat");
    const lngElement = document.getElementById("id_lng");
    markerNameElement.value = "Current Location";
    latElement.value = currentLocationMarker._latlng.lat;
    lngElement.value = currentLocationMarker._latlng.lng;


        // fetch("/map/add", {
        //     method: "POST",
        //     credentials: "same-origin",
        //     headers: {
        //       "X-Requested-With": "XMLHttpRequest",
        //       "X-CSRFToken": getCookie("csrftoken"),
        //     },
        //     body: JSON.stringify({payload: currentLocationMarker._latlng.lat})
        //   })
        //   .then(response => console.log(response))
        //   .then(data => {
        //     console.log(data);
        //   });
}

map.on('locationfound', onLocationFound);
   
map.on('click', function (e) {
    console.log("Map Clicked");
    marker
        .setLatLng(e.latlng)
        .addTo(map);
    console.log(marker);
    //document.getElementById("selectedLocationLat").innerHTML = marker._latlng.lat;
    //document.getElementById("selectedLocationLng").innerHTML = marker._latlng.lng;
    const markerNameElement = document.getElementById("id_name");
    const latElement = document.getElementById("id_lat");
    const lngElement = document.getElementById("id_lng");
    markerNameElement.value = "Selected Point";
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



// var map = L.map('map').fitWorld();

// L.tileLayer('https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png', {
//     maxZoom: 19,
//     attribution: '© OpenStreetMap'
// }).addTo(map);

// map.locate({setView: true, maxZoom: 16});


// function onLocationFound(e) {
//     var radius = e.accuracy;

//     L.marker(e.latlng).addTo(map)
//         .bindPopup("You are within " + radius + " meters from this point").openPopup();

//     L.circle(e.latlng, radius).addTo(map);
// }

// map.on('locationfound', onLocationFound);
