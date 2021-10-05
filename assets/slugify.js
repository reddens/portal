const fnameInput = document.querySelector("input[name=first_name]");
const lnameInput = document.querySelector("input[name=last_name]");
const fullName = fnameInput + lnameInput;
const slugInput = document.querySelector("input[name=slug]");

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-') //replace & with -and-
    .replace(/[\s\W-]+/g, '-') // replace spaces, non-word chars and dashes with a single dash
    + "-" + document.getElementById("last_name").value.toLowerCase()
};

fnameInput.addEventListener("keyup", (e) => {
    slugInput.setAttribute("value", slugify(fnameInput.value));
});

lnameInput.addEventListener("keyup", (e) => {
    slugInput.setAttribute("value", slugify(fnameInput.value));
})