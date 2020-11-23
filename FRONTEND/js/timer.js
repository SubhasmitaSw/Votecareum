var CountDownDate = new Date("Nov 21,2020 20:39:00").getTime();

var x = setInterval(function() {
    var now = new Date().getTime();
    var Distance = CountDownDate - now;

    var Days = Math.floor(Distance / (1000 * 60 * 60 * 24));
    var Hours = Math.floor((Distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var Minutes = Math.floor((Distance % (1000 * 60 * 60)) / (1000 * 60));
    var Seconds = Math.floor((Distance % (1000 * 60)) / 1000);


    if (Distance <= 0) {
        clearInterval(x);
        document.getElementById("Days").innerHTML = 0;
        document.getElementById("Hours").innerHTML = 0;
        document.getElementById("Minutes").innerHTML = 0;
        document.getElementById("Seconds").innerHTML = 0;
        document.getElementById("Expire").innerHTML = "VOTE NOW";
    }
    else{
        document.getElementById("Days").innerHTML = Days;
        document.getElementById("Hours").innerHTML = Hours;
        document.getElementById("Minutes").innerHTML = Minutes;
        document.getElementById("Seconds").innerHTML = Seconds;
        document.getElementById("Expire").innerHTML = "Wait!!! 🙏";
    }
}, 1000);
