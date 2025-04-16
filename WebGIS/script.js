var map = L.map('map', {
  center: [51.505, -0.09],
  zoom: 10,
  minZoom: 6,
  maxZoom: 16
}); 
var mapId = document.getElementById('map')
var geocoder = L.Control.geocoder({defaultMarkGeocode: false}).addTo(map);
var markers = {};


// ----------------Base Maps--------------------------------------------
var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


var satelite = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'jpg'
});

var dark = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
});
// -----------------------------------------------------------------------------------------


// create generic alert handler
function handleAlerts(alertID, alertType, message){
    const alertObject = `<div id = "${alertID}" class="alert alert-${alertType} alert-dismissible fade show" role="alert">${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
      </button>
    </div>`;
    const container = document.getElementById('alert-container');
    container.insertAdjacentHTML('beforeend', alertObject);
    setTimeout(() => {
      const alertEl = document.getElementById(alertID);
      if (alertEl) {
        alertEl.classList.remove('show');
        alertEl.classList.add('fade');
        setTimeout(() => alertEl.remove(), 250); 
      }
    }, 3000);
}

// add layer control
var baseLayer = {
    'Default': osm,
    'Satellite': satelite,
    'Dark': dark
};
L.control.layers(baseLayer).addTo(map);


// add map scale
L.control.scale().addTo(map)

// display full screen
function displayFullScreen(){
    if (document.fullscreenElement){
        document.exitFullscreen();
    }
    else{
      mapId.requestFullscreen();  
    }
}

// Add and remove marker on the map
function addMarker(latlng, name=null){
    if (Object.keys(markers).length == 2){
        handleAlerts('alert-markers', 'warning', 'Please remove a marker first. Marker limit: 2');
        return;
    }
    const popupText = name || `${latlng.lat.toFixed(6)}, ${latlng.lng.toFixed(6)}`;
    const marker = L.marker(latlng).addTo(map).bindPopup(popupText).openPopup();
    markers[latlng] = marker;
    marker.on('dblclick', function(){
        map.removeLayer(marker);
        delete markers[latlng];
    });
}
// Add marker by clicking or searching
map.on('click', function(e){
    addMarker(e.latlng);
});
geocoder.on('markgeocode', function(e){
    const latlng = e.geocode.center;
    const name = e.geocode.name;
    addMarker(latlng, name);
    map.setView(latlng, 16);
});

// add print leaflet control
L.control.browserPrint().addTo(map);


// display mouse coordinates
map.on('mousemove', function(e){
    var lat = e.latlng.lat.toFixed(4);
    var lng = e.latlng.lng.toFixed(4);
    $('.coordinates').html(`Lat: ${lat}, Lng: ${lng}`);
});



