const storedData = localStorage.getItem('db');

console.log(storedData);
let s=storedData.split('');
s.pop()
let name=s.join('');
console.log(name);
if (storedData) {
    document.querySelector(".namebd").textContent = "Записи таблицы " + storedData;

}
async function regaccept() {

    const res = await fetch(`http://www.intelligent-digital-systems.ru/${name}/read`);
    data = await res.json();
   
    let a = Object.keys(data)
    console.log(data)
 


}
regaccept();