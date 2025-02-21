async function profile_data() {
    const user = await fetch("http://localhost:8080/user/read");
    const data = await user.json()
    console.log(data)
}
profile_data()