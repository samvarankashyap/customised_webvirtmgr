$.expr[':'].Contains = $.expr.createPseudo(function(arg) {
    return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

$(document).ready(function() {
    $('#filter_button').click(function(event) {
        var filter_val = $('#filter_input').val();
        if(filter_val == '') {
            $('tbody tr').show();
        } else {
		$('#hello .class_name tag').doThis();
		$("#i").find("span")

	    // $('tbody tr td:Contains(\'' + filter_val + '\')').show();
           // $('tbody tr td:not(:Contains(\'' + filter_val + '\'))').hide();
        }
    });

    $('#filter_clear').click(function(event) {
        $('#filter_input').val('');
        $('#filter_button').click();
    });

    $('#filter_input').keyup(function(event){
        if(event.keyCode == 13){
            $('#filter_button').click();
        }
    });
});
