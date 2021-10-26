
// Update quantity of item in bag
$('.update-link').click(function (e) {
    var form = $(this).next('.update-form');
    form.submit();
})

// Remove item from bag
$('.remove-item').click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})
