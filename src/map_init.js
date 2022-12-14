// funkcia spracuej response zo stranky ako json
var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};


function initMap(){
    // adresa 
    var adresos = "brno namesti svobody"
    //var adresos = document.getElementById("video-author").value;
    // premenna adresa sa prisposobi pre http request
    adresos.split(" ").join("%20");
    const Http = new XMLHttpRequest();
    const url='https://maps.googleapis.com/maps/api/geocode/json?address=' + adresos + '&key=AIzaSyA_jFvlb3oQ-FiBNlzbc5jmDuQsB0IhKJc';

    cars = [0,0];
    getJSON(url,
    function(err, data) {
    if (err !== null) {
        alert('Something went wrong: ' + err);
    } else {
        cars = [data.results[0].geometry.location.lat,data.results[0].geometry.location.lng];
        var latitude =  Number(data.results[0].geometry.location.lat);
        var length = Number(data.results[0].geometry.location.lng);
        var options = {
            zoom:14,
            center:{lat:latitude,lng:length}
        }
        var map = new google.maps.Map(document.getElementById('map'), options)
        var marker = new google.maps.Marker({
            position: {lat:latitude,lng:length},
            map: map
        });
    }
    });


} 