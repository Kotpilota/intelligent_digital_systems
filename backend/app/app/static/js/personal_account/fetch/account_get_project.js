async function project_data() {
    try {
        const response = await fetch("/project/read", {
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
        console.error("Ошибка получения данных задач:", error);
    }
};

const obj_project_data = await project_data();

console.log(obj_project_data);

const project_form = document.getElementById("project_table");

console.log(project_form);

Object.keys(obj_project_data).forEach(function(key){
    if (key == "name"){
        project_form[0].textContent = obj_project_data[key];
        return
    }else if (key == "description"){
        project_form[1].textContent = obj_project_data[key];
        return
    }else if (key == "deadline"){
        project_form[2].textContent = obj_project_data[key];
        return
    }
});