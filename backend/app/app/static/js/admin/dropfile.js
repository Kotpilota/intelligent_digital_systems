async function authme() {
  const res = await fetch("/auth/me");
  const data = await res.json();
  console.log(data);
  if (data) {
    const massiv = [
      { nickname: data.nickname },
      { firstname: data.firstname },
      { lastname: data.lastname },
      { email: data.email },
      { activated: data.activated },
      { phone: data.phone },
      { role_id: data.role_id },
      { id: data.id },
    ];
    console.log(massiv);

    localStorage.setItem("token", JSON.stringify(massiv));
  }
}
authme();
