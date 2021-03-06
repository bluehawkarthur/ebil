function addMessage(text, extra_tags) {
    var message = $('<li class="'+extra_tags+'">'+text+'</li>').hide();
    $("#messages").append(message);
    message.fadeIn(500);

    setTimeout(function() {
        message.fadeOut(500, function() {
            message.remove();
        });
    }, 3000);
}

$(document).ready(function() {
    $('#messages').ajaxComplete(function(e, xhr, settings) {
        console.log('dshfsjfsjfhsjfhjfs');
        var contentType = xhr.getResponseHeader("Content-Type");

        if (contentType == "application/javascript" || contentType == "application/json") {
            var json = $.evalJSON(xhr.responseText);

            $.each(json.django_messages, function (i, item) {
                console.log(item.message);
                addMessage(item.message, item.extra_tags);
            });
        }
    }).ajaxError(function(e, xhr, settings, exception) {
        addMessage("There was an error processing your request, please try again.", "error");
    });
});