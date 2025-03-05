document.getElementById("nav_main").addEventListener("click",()=>{
    window.location.href = '/account';
})
const data = localStorage.getItem("token")
console.log(data)