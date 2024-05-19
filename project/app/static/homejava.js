function updateTime() {
    var now = new Date();
    var date = now.toDateString();
    var time = now.toLocaleTimeString();

    document.getElementById('datetime').innerHTML = 'Current date: ' + date + '<br>' + 'Current time: ' + time;
}

setInterval(updateTime, 1000); // Update time every second