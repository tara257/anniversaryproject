window.addEventListener('message', function(event) {
    if (event.data.type === 'zoom') {
        var map = window.map;
        map.setView([event.data.lat, event.data.lng], event.data.zoom);
    }
});
