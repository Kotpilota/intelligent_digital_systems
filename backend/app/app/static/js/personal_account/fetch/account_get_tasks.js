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

async function task_status_data() {
    try {
        const response = await fetch("/assigned_task/read", {
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
const obj_task_status = await task_status_data();


console.log(obj_task_data);
console.log(obj_task_status);

const task_form = document.getElementById("task_table");

function Table_task(obj_task_data, obj_task_status) {
    let tableContent = '';
    for (let i = 0; i < Object.keys(obj_task_data, obj_task_status).length; i++) {
        const task = obj_task_data[i];
        const data_status = obj_task_status[i];
        const name = task && task.name ? task.name : "Имя не указано";
        const description = task && task.description ? task.description : "Описание не указано";
        const task_status_id = data_status && data_status.task_status_id ? data_status.task_status_id : "Статус не указан";
        const deadline = data_status && data_status.deadline ? data_status.deadline : "Дедлайн не указан";
        if(task_status_id == 1){
            var stat = "Ожидает"
            var color = "yellow"
        } else if(task_status_id == 2){
            var stat = "В процессе"
            var color = "blue"
        } else if(task_status_id == 3){
            var stat = "Выполнено"
            var color = "green"
        };
        tableContent += `<tr><td class="px-6 py-4 whitespace-nowrap"><div class="text-sm font-medium text-gray-900">${name}</div><div class="text-sm text-gray-500">${description}</div></td><td class="px-6 py-4 whitespace-nowrap"><span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-${color}-100 text-${color}-800">${stat}</span></td><td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${deadline.slice(0, 10).split('-').reverse().join('.')}</td></tr>`;
    }
    if (task_form) {
        task_form.innerHTML = tableContent;
    } else {
        console.error("Element with class 'task_form' not found.");
    }
};
Table_task(obj_task_data, obj_task_status);

const progress_bar = document.getElementById("task_bar");

function Progress_bar(obj_task_data, obj_task_status){
    let status_to_do = 0;
    let status_in_progress= 0;
    let status_done = 0;
    let sum = 0;
    let complete_task = 0;
    let procent = 0;
    for (let i = 0; i < Object.keys(obj_task_data, obj_task_status).length; i++){
        const data_status = obj_task_status[i];
        const task_status_id = data_status && data_status.task_status_id ? data_status.task_status_id : "Статус не указан";
        console.log(task_status_id)
        if(task_status_id == 1){
            status_to_do += 1
        } else if(task_status_id == 2){
            status_in_progress += 1
        } else if(task_status_id == 3){
            status_done += 1
        };
        sum += 1;
    };
    let barContent = ''
    procent = Math.round(100 / (status_to_do + status_in_progress + status_done))
    console.log(procent)
    complete_task = status_done * procent
    barContent += `<div class="flex items-center justify-between mb-4"><h3 class="text-lg font-semibold">Активные задачи</h3><span class="text-2xl font-bold text-blue-600">${sum}</span></div><div class="h-2 bg-gray-200 rounded"><div class="h-2 bg-blue-600 rounded" style="width:${complete_task}%"></div></div>`
    progress_bar.innerHTML = barContent;
};
Progress_bar(obj_task_data, obj_task_status)