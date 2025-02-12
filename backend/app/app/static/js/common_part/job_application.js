const form = document.getElementById('jobApplicationForm');
const fileUpload = document.querySelector('.file-upload');
const fileInput = fileUpload.querySelector('input[type="file"]');
const progress = document.querySelector('.progress');
const progressBar = document.querySelector('.progress-bar__fill');

// ��������� �������������� ������
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

// ���������� ����� ����� ��� ������
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        updateFileName(e.target.files[0].name);
    }
});

function updateFileName(name) {
    const span = fileUpload.querySelector('span');
    span.textContent = name;
}

// �������� �����
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    progress.classList.add('active');

    // �������� ��������
    let width = 0;
    const interval = setInterval(() => {
        width += 5;
        progressBar.style.width = width + '%';

        if (width >= 100) {
            clearInterval(interval);
            setTimeout(() => {
                alert('������ ������� ����������! �� �������� � ���� � ��������� �����.');
                form.reset();
                progress.classList.remove('active');
                progressBar.style.width = '0%';
                fileUpload.querySelector('span').textContent = '���������� ���� ��� ������� ��� ��������';
            }, 500);
        }
    }, 100);
});