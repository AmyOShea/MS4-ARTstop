/*
    Core taken from Stripe:
    https://stripe.com/docs/payments/accept-a-payment

*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    invalid: {
        color: '#bb3744',
        iconColor: '#bb3744'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');