$(document).ready(function(){
    $('#datepicker').datepicker();
    $('#datepicker-2').datepicker();

    $('#inputName').on('input', function(e){
        e.preventDefault();
        $.ajax({
            url: '/filter_name/',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                console.log("Received this from server: ", serverResponse)
            }
        })
    })
    $('.inputFromDate').on('input', function(e){
        e.preventDefault();
        $.ajax({
            url: '/filter_from_date/',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                console.log("Received this from server: ", serverResponse)
            }
        })
    })
    $('#inputDate').on('input', function(e){
        e.preventDefault();
        $.ajax({
            url: '/filter_date/',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                console.log("Received this from server: ", serverResponse)
            }
        })
    })
})