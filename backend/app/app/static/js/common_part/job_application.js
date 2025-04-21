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

    progress.classList.add('active');

    try {
        const file = fileInput.files[0];
        if (!file) {
            throw new Error('Необходимо загрузить резюме');
        }

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

        progressBar.style.width = '50%';

        const formData = new FormData(form);
        const jobData = {
            fullname: formData.get('fullname'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            letter: formData.get('letter'),
            job_id: parseInt(formData.get('job_id')),
            cv_id: fileResult.id
        };

        const applicationResponse = await fetch('/job_application/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jobData),
            credentials: 'include'
        });

        if (!applicationResponse.ok) {
            const error = await applicationResponse.json();
            throw new Error(`Ошибка отправки заявки: ${error.detail}`);
        }

        progressBar.style.width = '100%';

        setTimeout(() => {
            alert('Ваша заявка успешно отправлена!');
            window.location.href = '/job_postings';
        }, 500);

    } catch (error) {
        console.error('Ошибка:', error);

        const errorMessage = document.querySelector('.error-message');
        errorMessage.textContent = error.message;
        errorMessage.style.display = 'block';

        progressBar.style.width = '0%';
    } finally {
        setTimeout(() => {
            progress.classList.remove('active');
        }, 2000);
    }
});