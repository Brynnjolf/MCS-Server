$('document').ready(function() {
    // Click the generate button, will take all information in form and send it to API endpoint via AJAX
    $('.generate').click(function() {
        // TODO: send these three variables to an endpoint for processing
        var risk = $('#risk').val();
        var index = $('#index').val();
        var blacklist = $('#blacklist').val();
        console.log(risk,index,blacklist);
        // pseudo loading for client immersion, using settimeout
        setTimeout(function() {
            // TODO: Change from redirecting to homepage, to redirecting to company table page
            window.location = '/';
        }, 3000);

    });
});