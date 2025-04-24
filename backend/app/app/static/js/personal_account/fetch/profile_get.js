async function profile_data() {
    try {
        const response = await fetch("/auth/me", {
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

        return data
    } catch (error) {
        console.error("Ошибка получения данных профиля:", error);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    const obj_profile_data = await profile_data();
    const profile_form = document.querySelectorAll(".form-control");

    Object.keys(obj_profile_data).forEach(function(key) {
        if (key === "firstname") {
            profile_form[0].value = obj_profile_data[key];
        } else if (key === "lastname") {
            profile_form[1].value = obj_profile_data[key];
        } else if (key === "email") {
            profile_form[2].value = obj_profile_data[key];
        } else if (key === "phone") {
            const number = `${obj_profile_data[key].slice(0, 2)} (${obj_profile_data[key].slice(2, 5)}) ${obj_profile_data[key].slice(5, 8)}-${obj_profile_data[key].slice(8, 10)}-${obj_profile_data[key].slice(10, 12)}`
            profile_form[3].value = number;
        } else if (key === "role") {
            switch (obj_profile_data[key].name) {
                case "employee":
                    profile_form[4].value = "Сотрудник компании";
                    break;
                case "teamlead":
                    profile_form[4].value = "Руководитель группы";
                    break;
                case "admin":
                    profile_form[4].value = "Администратор системы";
                    break;
                case "ceo":
                    profile_form[4].value = "Исполнительный директор";
                    break;
                default:
                    profile_form[4].value = obj_profile_data[key].name;
            }
        } else if (key == "created_at") {
            profile_form[5].value = `${obj_profile_data[key].slice(0, 10).split('-').reverse().join('.')}`;
        }
    });

    document.getElementById('save-profile').addEventListener('click', async (e) => {
        e.preventDefault();

        const firstname = document.getElementById('firstname').value.trim();
        const lastname = document.getElementById('lastname').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone-number').value.replace(/\D/g, '');

        if (!firstname || !lastname || !email) {
            alert('Заполните Имя, Фамилию и Email!');
            return;
        }

        const final_profile_form = {
            nickname: obj_profile_data.nickname,
            firstname: firstname,
            lastname: lastname,
            hashed_password: obj_profile_data.hashed_password,
            email: email,
            phone: phone,
            activated: obj_profile_data.activated,
            role_id: obj_profile_data.role_id,
        };

        try {
            const response = await fetch(`/user/update/${obj_profile_data.id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(final_profile_form),
            });

            if (!response.ok) throw new Error('Ошибка сервера');
            alert('Данные сохранены!');
            location.reload();
        } catch (error) {
            console.error('Ошибка:', error);
            alert(error.message);
        }
    });
});
