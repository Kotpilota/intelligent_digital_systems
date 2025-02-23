// ���������� ���������� ��������
document.querySelector('.filters__form').addEventListener('input', (e) => {
    // ����� ����� �������� ������ ����������
    console.log('���������� ��������:', e.target.value);
});

// ��������� �������� �� ��������
document.querySelectorAll('.job-card .button').forEach(button => {
    button.addEventListener('click', () => {
        alert('������� �� ������! �� �������� � ���� � ��������� �����.');
    });
});