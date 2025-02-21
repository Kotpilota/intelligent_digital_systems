const storedData = localStorage.getItem('db');

console.log(storedData);
let s=storedData.split('');
s.pop()
let ss=s.join('');
console.log(data);
if (storedData) {
    document.querySelector(".namebd").textContent = "Записи таблицы " + storedData;

}
async function regaccept() {

    const res = await fetch(`http://www.intelligent-digital-systems.ru/${data}/read`);
    data = await res.json();
   
    let a = Object.keys(data)
    console.log(data)
 


}
regaccept();