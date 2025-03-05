async function task_data() {
    try {
        const response = await fetch("/task/read", {
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

const obj_task_data = await task_data();

console.log(obj_task_data);

const task_form = document.getElementById("task_table");

function Table_task(obj_task_data) {
    let tableContent = '';
    for (let i = 0; i < Object.keys(obj_task_data).length; i++) {
        const task = obj_task_data[i];
        const name = task && task.name ? task.name : "Имя не указано";
        const description = task && task.description ? task.description : "Описание не указано";
        tableContent += `<tr><td class="px-6 py-4 whitespace-nowrap"><div class="text-sm font-medium text-gray-900">${name}</div><div class="text-sm text-gray-500">${description}</div></td><td class="px-6 py-4 whitespace-nowrap"><span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Выполнено</span></td><td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">19 декабря</td></tr>`;
    }
    if (task_form) {
        task_form.innerHTML = tableContent;
    } else {
        console.error("Element with class 'task_form' not found.");
    }
};
Table_task(obj_task_data);