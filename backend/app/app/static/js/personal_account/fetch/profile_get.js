// import {$, jQuery} from 'jquery';
// import 'jquery-cookie'; 

// window.$ = $; 
// window.jQuery = jQuery;

// const cooca = $.cookie('ids_user_access_token'); 
// console.log("Значение куки ids_user_access_token:", cooca);

// if (cooca === null || cooca === undefined) { 
//     alert("Кука не была установлена!");
// }

// console.log("Все куки:", $.cookie()); 
/*
function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    console.log("Cookies: "+ $.cookie("ids_user_access_token"))   
    return keyValue ? keyValue[2] : null;
}
    */



async function profile_data() {
    console.log("data: ")
    try {
        const response = await fetch("/user/read", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            console.error(`HTTP error! Status: ${response.status}`);
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        
        console.log(data);
    } catch (error) {
        console.error("Ошибка получения данных профиля:", error);
    }
}

function headers(set_cookie = false) {
    let headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    };

    if (set_cookie) {
        headers['Authorization'] = "Bearer " + $.cookie('remember_user_token');
    }

    return headers;
}

profile_data();