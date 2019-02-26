$(document).ready(function() {
    $('#search-btn').on("click",function() {
        query = $("#search").val();
        console.log("Search query:: " + query);
        if (query.length == 0)
            M.toast({html: 'Please enter something!'})
        else
            M.toast({html: 'Finding results...'})
            window.location = "/search?q=" + query;
    });
});