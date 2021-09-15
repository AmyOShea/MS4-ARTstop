/*
    Core taken from Stripe:
    https://stripe.com/docs/payments/accept-a-payment

*/

// Handles card errors

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    invalid: {
        color: '#bb3744',
        iconColor: '#bb3744'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors')
    if (event.error) {
        var html = `
            <span role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span><strong>${event.error.message}</strong></span>
            `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handles form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                    <i class="fas fa-exclamation-circle"></i>
                </span>
                <span><strong>${result.error.message}</strong></span>
                `;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});