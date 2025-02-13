document.getElementById('profile-form').addEventListener('submit', (e) => {
    e.preventDefault();
<<<<<<< HEAD
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
=======
  });
  
  document.getElementById('save-profile').addEventListener('click', () => {
    const form = document.getElementById('profile-form');
    if (form.checkValidity()) {
      alert('РР·РјРµРЅРµРЅРёСЏ СѓСЃРїРµС€РЅРѕ СЃРѕС…СЂР°РЅРµРЅС‹');
    } else {
      form.reportValidity();
    }
  });
  
  const inputs = document.querySelectorAll('.form-control:not([readonly])');
  inputs.forEach(input => {
    input.addEventListener('input', () => {
      input.style.borderColor = input.value.trim() ? '#eee' : var(--danger);
    });
  });
>>>>>>> e23564bfb991c86043ff3d49617e1900305438b0
