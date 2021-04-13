// $(document).ready(function(){
//     $('form').submit(function(e){
//         e.preventDefault();
//         $.ajax({
//             url: "{% url 'products' %}",
//             type: "POST",
//             data: $(this).serialize(),
//             success: function(data) {
//                 if (!(data['success'])) {
//                     // Here we replace the form, for the
//                     $(this).replaceWith(data['form_html']);
//                 }
//                 else {
//                     // Here you can show the user a success message or do whatever you need
//                     $(this).find('.success-message').show();
//                 }
//             },
//             error: function () {
//                 $(this).find('.error-message').show()
//             }
//         });
//     })
// })