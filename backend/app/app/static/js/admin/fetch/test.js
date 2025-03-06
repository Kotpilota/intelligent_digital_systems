setInterval(() => {
  const nickname = document.querySelector("#nickName").value;
  const phone = document.querySelector("#phone1").value;
  let password = document.querySelector("#password1").value;
  const password_check = document.querySelector("#confirmPassword").value;
  const active = true;
  const role = document.querySelector("#role").value;
  const roles = parseInt(role);
  console.log(nickname, phone, password, password_check, active, roles);
}, 2000);
