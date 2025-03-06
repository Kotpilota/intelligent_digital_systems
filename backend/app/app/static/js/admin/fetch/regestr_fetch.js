async function regp1ost() {
  const nickname = document.querySelector("#nickName").value;
  const phone = document.querySelector("#phone1").value;
  const password = document.querySelector("#password1").value;
  const password_check = document.querySelector("#confirmPassword").value;
  const active = true;
  const role = document.querySelector("#role").value;
  const roles = parseInt(role);

  const res = await fetch("/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nickname,
      phone,
      password,
      password_check,
      active,
      roles,
    }),
  });

  const data = await res.json();
  console.log(data);
  if (data) {
    alert("Регистрация прошла успешно!");
  }
}
document.addEventListener("click", async function (event) {
  if (event.target.classList.contains("button")) {
    regp1ost();
  }
});
