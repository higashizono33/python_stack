$(document).ready(function(){
    $('form').submit(function(e){
        e.preventDefault();
        var form_id = $('#id-productForm');
        $.ajax({
            url: '/products',
            type: "POST",
            data: form_id.serialize(),
            dataType: 'json',
            header: {'X-CSRFToken': '{% csrf_token %}'},
            success: function(response) {
                var success = response['success']
                if (success) {
                    $('body').html(response['page']);
                }
                else {
                    form_id.replaceWith(response['html']);
                    var button = '<div class="form-group d-flex justify-content-end mt-3"><button type="submit" class="btn btn-primary">Add</button></div>'
                    $('form').append(button);
                }
            },
            error: function () {
                alert('errors')
            }
        });
    })
    $('body').on('click', '.delete', (function(e){
        // console.log('hi')
        e.preventDefault();
        var id = $('.delete').attr('product_id');
        $.ajax({
            url: `products/${id}/delete`,
            type: "get",
            dataType: 'json',
            success: function(response) {
                // console.log('hi')
                console.log(response)
                $('.table-body').html(response['table']);
            }
        });
    }))
})