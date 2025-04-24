document.getElementById('profile-form').addEventListener('submit', (e) => {
  e.preventDefault();
});

const inputs = document.querySelectorAll('.form-control:not([readonly])');
inputs.forEach(input => {
  input.addEventListener('input', () => {
    input.style.borderColor = input.value.trim() ? '#eee' : 'let(--danger)';
  });
});