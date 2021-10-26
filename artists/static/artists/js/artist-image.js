/*jshint esversion: 6 */

const img = document.getElementById('artist-img');
let width = img.clientWidth;
let height = img.clientHeight;

if (width < height) {
    img.classList.add("portrait");
} else {
    img.classList.add("landscape");
}