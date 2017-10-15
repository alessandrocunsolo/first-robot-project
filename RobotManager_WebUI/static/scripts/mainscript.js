function updateImage() {
    var d = new Date();
    $.get("/image/"+d.getTime(), function(data) {
        if (data === "0") return;
        var imageData = "data:image/png;base64," + data;
        //$('#imgbox').attr("src", imageData);
        $('#panel').css("background","url("+imageData+") no-repeat");
        $('#panel').css("background-size","100%");
        setTimeout(function() {
            updateImage();
        }, 1);
    });
}

function sendMove(direction)
{
    $.ajax({
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Accept","application/json");
        },
        type: "POST",
        url: "/move",
        data: JSON.stringify({ "direction": direction, "value":100 }),
        success: function (msg) {
        },
        failure: function (msg) {
        }
    });
}

$(document).ready(function() {
    updateImage();
    $("#btnAvanti").click(function () {
        sendMove(1);
    });
    $("#btnIndietro").click(function () {
        sendMove(2);
    });
    $("#btnStop").click(function () {
        sendMove(0);
    });
    $("#btnSinistra").click(function () {
        sendMove(4);
    });
    $("#btnDestra").click(function () {
        sendMove(3);
    });
    $('body').keydown(function(event){
	if (event.which == 39)
	{
		sendMove(3);
	}
	if (event.which == 37)
	{
		sendMove(4);
	}
	if (event.which == 38)
	{
		sendMove(1);
	}
	if (event.which == 40)
	{
		sendMove(2);
	}
    });
});
