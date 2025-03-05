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

function Table_project(obj_project_data) {
    let containerContent = '';
    for (let i = 0; i < Object.keys(obj_project_data).length; i++) {
        const project = obj_project_data[i];
        const name = project && project.name ? project.name : "Имя не указано";
        const description = project && project.description ? project.description : "Описание не указано";
        const deadline = project && project.deadline ? project.deadline : "Дедлайн не указан";
        containerContent += `<div class="project-card bg-white p-6 rounded-lg shadow-md"><div class="flex justify-between items-start mb-4"><div><h3 class="text-xl font-semibold mb-2" id="project_table">${name}</h3><p class="text-gray-600">${description}</p></div><span class="bg-blue-100 text-blue-800 text-sm font-medium px-3 py-1 rounded">В процессе</span></div><div class="mb-4"><div class="flex items-center mb-2"><span class="text-sm text-gray-600">Прогресс</span><span class="ml-auto text-sm font-medium">75%</span></div><div class="h-2 bg-gray-200 rounded"><div class="h-2 bg-blue-600 rounded" style="width: 75%"></div></div></div><div class="flex items-center"><div class="flex -space-x-2"><img src="https://ui-avatars.com/api/?name=Alex" class="w-8 h-8 rounded-full border-2 border-white"><img src="https://ui-avatars.com/api/?name=Maria" class="w-8 h-8 rounded-full border-2 border-white"><img src="https://ui-avatars.com/api/?name=John" class="w-8 h-8 rounded-full border-2 border-white"></div><span class="ml-4 text-sm text-gray-600">Дедлайн: ${deadline}</span></div></div>`;
    }
    if (project_form) {
        project_form.innerHTML = containerContent;
    } else {
        console.error("Element with class 'task_form' not found.");
    }
};
Table_project(obj_project_data);