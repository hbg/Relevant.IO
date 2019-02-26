$(document).ready(function() {
    $('#search-btn').on("click",function() {
        query = $("#search").val();
        console.log("Search query:: " + query);
        if (query.length == 0) {
            M.toast({html: 'Please enter something!'})
        }
        else {
            var arr = query.split(" ");
            let q = "";
            let search= "";
            for (var i=0; i<arr.length; i++) {
                let item = arr[i];
                //  Some really bad practices below
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
                    console.log(count);
                    q += "&count=" + count;
                }
                console.log(search + q);
            }

            M.toast({html: 'Finding results...'})
            window.location = "/search?q=" + search + q;
        }
    });
});