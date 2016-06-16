$(document).ready(function() {
    // connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/notification');

    // receive details from server
    socket.on('notify', function(msg) {
        var msgString = msg.message;
        if (msg.priority == true) {
            msgString = '!!! ' + msg.message;
            console.log('Received PRIORITY message: ' + msgString);
        }
        else {
            console.log('Received message: ' + msgString);
        }
        $('#log').append('<p>Message: ' + msgString + '</p>');
    });
});