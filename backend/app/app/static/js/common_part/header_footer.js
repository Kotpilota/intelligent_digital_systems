let searchbut=document.querySelector(".search-button")
searchbut.addEventListener("click",function(event){
            event.stopPropagation();
            document.querySelector(".search").style.width="200px";
            document.querySelector(".search").style.marginLeft="20px"


})
document.querySelector(".search").addEventListener("click",function(event){
    event.stopPropagation();})
window.addEventListener("click",function(){
    document.querySelector(".search").style.width="0px";
    document.querySelector(".search").style.marginLeft="0px"

})

const modalTrigger = document.querySelector(".voity");
const windowInnerWidth = document.documentElement.clientWidth;
const scrollbarWidth = parseInt(window.innerWidth) - parseInt(document.documentElement.clientWidth);

const bodyElementHTML = document.getElementsByTagName("header")[0];
const modalBackground = document.getElementsByClassName("modalBackground")[0];
const modalClose = document.getElementsByClassName("modalClose")[0];
const modalActive = document.getElementsByClassName("modalActive")[0];

function bodyMargin() {
    bodyElementHTML.style.marginRight = "-" + scrollbarWidth + "px";
}

bodyMargin();

modalTrigger.addEventListener("click", function () {
    modalBackground.style.display = "flex";
    document.body.style.overflow = "hidden"; 
});


modalBackground.addEventListener("click", function(event) {
    if (event.target === modalBackground) { 
    modalBackground.style.display = "none";
    document.body.style.overflow = "auto";
    }
});


document.querySelectorAll('.auth-form input, .auth-form button').forEach(element => {
    element.addEventListener('click', function(event) {
    event.stopPropagation(); 
    });
});

modalClose.addEventListener("click", function () {
    modalBackground.style.display = "none";
    document.body.style.overflow = "auto";
});

document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
                phone: phone,
                password: password
            }),
            credentials: 'include' 
        });

        const data = await response.json();
        
        if (response.ok) {
            modalBackground.style.display = "none";
            document.body.style.overflow = "auto";
            window.location.reload();
        } else {
            showError(data.detail || "Ошибка авторизации");
        }
    } catch (error) {
        showError("Ошибка сети или сервера");
    }
});

function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
}