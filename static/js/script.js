$('.toast').toast('show')

let currentUrl = window.location.href;
const nav = document.getElementById("main-nav");
const viewBag = document.getElementById("toast-viewbag-btn");
const contShopping = document.getElementById("toast-cont-shopping-btn");
const formUsername = document.getElementById("id_username");

if (currentUrl === 'https://8000-emerald-marlin-uaty91sq.ws-eu17.gitpod.io/' || currentUrl === 'https://ms4-artstop.herokuapp.com/' ) {
    nav.classList.add("home-main-nav")
}

if (currentUrl === 'https://8000-emerald-marlin-uaty91sq.ws-eu17.gitpod.io/bag/' || currentUrl === 'https://ms4-artstop.herokuapp.com/bag/' ) {
    viewBag.style.display = "none";
    contShopping.style.display = "inline-block";
} else {
    if (contShopping) {
        contShopping.style.display = "none";
        viewBag.style.display = "inline-block";
    }
};

// Override the autofocus bug on allauth forms
if (formUsername) {
    formUsername.blur();
}
