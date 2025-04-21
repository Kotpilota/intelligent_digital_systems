const form = document.getElementById('jobApplicationForm');
const fileUpload = document.querySelector('.file-upload');
const fileInput = fileUpload.querySelector('input[type="file"]');
const progress = document.querySelector('.progress');
const progressBar = document.querySelector('.progress-bar__fill');


fileUpload.addEventListener('dragover', (e) => {
    e.preventDefault();
    fileUpload.style.borderColor = 'var(--primary-color)';
});

fileUpload.addEventListener('dragleave', (e) => {
    e.preventDefault();
    fileUpload.style.borderColor = '#ddd';
});

fileUpload.addEventListener('drop', (e) => {
    e.preventDefault();
    fileUpload.style.borderColor = '#ddd';

    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        updateFileName(e.dataTransfer.files[0].name);
    }
});


fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        updateFileName(e.target.files[0].name);
    }
});

function updateFileName(name) {
    const span = fileUpload.querySelector('span');
    span.textContent = name;
}


document.getElementById('jobApplicationForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const file = formData.get('myfile');

    try {
        const fileFormData = new FormData();
        fileFormData.append('myfile', file);

        const fileResponse = await fetch('/file/create', {
            method: 'POST',
            body: fileFormData,
            credentials: 'include'
        });

        if (!fileResponse.ok) {
            const error = await fileResponse.json();
            throw new Error(`Ошибка загрузки файла: ${error.detail}`);
        }

        const fileResult = await fileResponse.json();
        console.log(fileResult);

        const jsonData = {
            ...Object.fromEntries(formData),
            file_id: fileResult.id
        };

        const formResponse = await fetch('/job_application/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData),
            credentials: 'include'
        });

        if (!formResponse.ok) {
            const error = await formResponse.json();
            throw new Error(`Ошибка отправки формы: ${error.detail}`);
        }

        const formResult = await formResponse.json();
        console.log('Результаты:', {file: fileResult, form: formResult});
        alert('Данные успешно отправлены!');

    } catch (error) {
        console.error('Ошибка:', error);
        alert(error.message);
    }
});