async function regpost() {
  const nickname = document.querySelector("#nickName").value;
  const phone = document.querySelector("#phone").value;
  const password = document.querySelector("#password").value;
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
    localStorage.setItem("token", data.nickname);
  }
}
document.querySelector(".button").addEventListener("click", regpost);
