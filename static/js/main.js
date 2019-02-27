var x, y = 0
function setPosition(pos) {
    x = pos.coords.latitude;
    y = pos.coords.longitude;
}
function conductQuery() {

    query = $("#search").val();
        console.log("Search query:: " + query);
        if (query.length == 0) {
            M.toast({html: 'Please enter something!'})
        }
        else {
            var arr = query.split(" ");
            let q = "";
            let search, since = "";
            for (var i=0; i<arr.length; i++) {
                let item = arr[i];
                //  Some really bad practices below --> Specify "SINCE" & "COUNT"
                if (!(item.includes("since=") || item.includes("count=") && item.length > 0)) {
                    if(item.includes("search="))
                        search += item.split("search=")[1].trim() + "%20";
                    else
                        search += item + "%20";
                }
                else if (item.includes("since=")) { // Optional
                    since = item.split("since=")[1].trim()
                    q += "&since=" + since;
                }
                else if (item.includes("count=")) { // Optional
                    count = item.split("count=")[1].trim()
                    q += "&count=" + count;
                }
                console.log(search + q);
            }
            M.toast({html: 'Finding results...'})
            let format_string = ("/search?q=" + search + q + "&loc=" + x + "," + y);
            window.location = format_string.replace("undefined","")
        }
}
$(document).ready(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(setPosition);
    }
    $('#search-btn').on("click",function() {
        conductQuery();
    });
});

$(document).on('keypress',function(e) {
    if(e.which == 13) {
        conductQuery();
    }
});