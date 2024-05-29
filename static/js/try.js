const geolocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPostion, showError)
    }
    else {
        alert('GEO Location is not Support this Browser..')
    }
};

const showPostion = (position) => {
    let lat = position.coords.latitude
    let long = position.coords.longitude
    const des = document.querySelector('p');
    des.innerHTML = `Latitude : ${lat} <br>Longitude : ${long}`;

}



const showError = (error) => {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied The Request of GeoLocation...")
            break;

        case error.POSITION_UNAVAILABLE:
            alert("Location Information IS Unavailable...")
            break;

        default:
            alert("An Unknown error Occurred...")
    }
}

