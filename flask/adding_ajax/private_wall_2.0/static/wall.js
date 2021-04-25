$(document).ready(function(){
    $('.messageForm').on('submit', function(e){
        $.ajax({
            data: $(this).serialize(),
            method: "POST",
            url: "/process_message",
            context: this,
        })
        .done(function(data){
            if(!data.status){
                $(this).find('#success').hide();
                $(this).find('#error').show();
                $(this).find('#error').html(data.error);
            } else {
                $(this).find('#error').hide();
                $(this).find('#success').show();
                $(this).find('#success').html(data.success);
                $(this).find('#messageArea').val('');
                $('#sent_count').html(data.count);
            }
        })
        e.preventDefault();
    })
    $('.deleteLink').on('click', function(e){
        var id = $(this).attr('id')
        $.ajax({
            method: "GET",
            url: "/delete_message/"+id,
        })
        .done(function(res){
            $('.section_'+id).hide()
            $('#received_count').html(res.r_count);
        })
        e.preventDefault();
    })
})