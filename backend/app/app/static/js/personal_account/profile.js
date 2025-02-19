document.getElementById('profile-form').addEventListener('submit', (e) => {
  e.preventDefault();
});

document.getElementById('save-profile').addEventListener('click', () => {
  const form = document.getElementById('profile-form');
  if (form.checkValidity()) {
    alert('Изменения успешно сохранены');
  } else {
    form.reportValidity();
  }
});

const inputs = document.querySelectorAll('.form-control:not([readonly])');
inputs.forEach(input => {
  input.addEventListener('input', () => {
    input.style.borderColor = input.value.trim() ? '#eee' : let(--danger);
  });
});