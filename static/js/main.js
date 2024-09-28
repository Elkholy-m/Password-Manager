const date = document.querySelector(".date")
let eye1 = document.querySelector(".toggle-button")
let eye2 = document.querySelector(".toggle-button_2")
let password = document.getElementById("password")
let re_password = document.getElementById("re-password")
const thisYear = new Date().getFullYear()
date.innerText = thisYear
eye1.addEventListener("click", function(){
    if (password.type === "password"){
        password.type = "text"
        eye1.innerText = "👁️"
    }
    else {
        password.type = "password"
        eye1.innerText = '👁️‍🗨️'
    }
})
eye2.addEventListener("click", function(){
    if (re_password.type === "password"){
        re_password.type = "text"
        eye2.innerText = "👁️"
    }
    else {
        re_password.type = "password"
        eye2.innerText = '👁️‍🗨️'
    }
})

// let search = document.getElementById("search")
// search.addEventListener("input", async function() {
//     let response = await fetch("/search?q=" + search.value)
//     let shows = response.text
//     document.querySelector("#ul").innerHTML = shows 
// })
async function copyText0() {
    try {
        const textArea = document.getElementById("textToCopy0");
        await navigator.clipboard.writeText(textArea.value);
    } catch (err) {
        console.error("Failed to copy: ", err);
    }
}
async function copyText1() {
    try {
        const textArea = document.getElementById("textToCopy1");
        await navigator.clipboard.writeText(textArea.value);
    } catch (err) {
        console.error("Failed to copy: ", err);
    }
}
