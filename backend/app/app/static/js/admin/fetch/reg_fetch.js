async function  regaccept() {
  
   
  const res = await fetch("/admin/database_schema");
  data =await res.json();
  console.log(data);
  let a=Object.keys(data)
  
  for(let i=0;i<a.length;i++){
     
      let namedb=a[i];
      let db=data[namedb].length;
      let bd_size="-";
      let active="-";
     
  
      let table=document.querySelector(".table");
      let sidebar=document.querySelector(".sidebar");
    
      
      
   if(i<5){
      table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
      }
      
      const link = document.createElement('a');
      link.href = "#";
      link.textContent = namedb;
  
    
      link.classList.add('nav-item1');
   
  
    
      sidebar.appendChild(link);
        
      link.addEventListener("click", function() {
        window.location.href = '/admin_db_tables';
        localStorage.setItem("db", namedb); 
      });
  
    console.log(namedb,db,bd_size,active);


   

  
  
}

}
async function page1() {
let table=document.querySelector(".table");
table.innerHTML="";
const res = await fetch("/admin/database_schema");
data =await res.json();
console.log(data);
let a=Object.keys(data)
table.innerHTML+="<thead><tr><th>Название таблицы</th><th>Количество записей</th><th>Размер</th><th>Последнее обновление</th><th>Действия</th></tr></thead>"
for(let i=5;i<a.length;i++){
  
  let namedb=a[i];
  let db=data[namedb].length;
  let bd_size="-";
  let active="-";
  let table=document.querySelector(".table");

  if(i>5&&i<11){
  table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
  }
} }
async function page2() {
let table=document.querySelector(".table");
table.innerHTML="";
const res = await fetch("/admin/database_schema");
data =await res.json();
console.log(data);
let a=Object.keys(data)
table.innerHTML+="<thead><tr><th>Название таблицы</th><th>Количество записей</th><th>Размер</th><th>Последнее обновление</th><th>Действия</th></tr></thead>"
for(let i=10;i<a.length;i++){
  
  let namedb=a[i];
  let db=data[namedb].length;
  let bd_size="-";
  let active="-";
  let table=document.querySelector(".table");

  if(i>10&&i<16){
  table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
  }
} }
async function page3() {
let table=document.querySelector(".table");
table.innerHTML="";
const res = await fetch("/admin/database_schema");
data =await res.json();
console.log(data);
let a=Object.keys(data)
table.innerHTML+="<thead><tr><th>Название таблицы</th><th>Количество записей</th><th>Размер</th><th>Последнее обновление</th><th>Действия</th></tr></thead>"
for(let i=15;i<a.length;i++){
  
  let namedb=a[i];
  let db=data[namedb].length;
  let bd_size="-";
  let active="-";
  let table=document.querySelector(".table");

  if(i>15&&i<21){
  table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
  }
} }
async function page4() {
let table=document.querySelector(".table");
table.innerHTML="";
const res = await fetch("/admin/database_schema");
data =await res.json();
console.log(data);
let a=Object.keys(data)
table.innerHTML+="<thead><tr><th>Название таблицы</th><th>Количество записей</th><th>Размер</th><th>Последнее обновление</th><th>Действия</th></tr></thead>"
for(let i=20;i<a.length;i++){
  
  let namedb=a[i];
  let db=data[namedb].length;
  let bd_size="-";
  let active="-";
  let table=document.querySelector(".table");

  if(i>20&&i<26){
  table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
  }
} }
async function page() {
  let table=document.querySelector(".table");
  table.innerHTML="";
  const res = await fetch("/admin/database_schema");
  data =await res.json();
  console.log(data);
  let a=Object.keys(data)
  table.innerHTML+="<thead><tr><th>Название таблицы</th><th>Количество записей</th><th>Размер</th><th>Последнее обновление</th><th>Действия</th></tr></thead>"
  for(let i=0;i<a.length;i++){
    
    let namedb=a[i];
    let db=data[namedb].length;
    let bd_size="-";
    let active="-";
    let table=document.querySelector(".table");
  
    if(i<5){
    table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
    }
  } }
  

regaccept()
  
  document.querySelector(".page-btn0").addEventListener("click", page)
  document.querySelector(".page-btn1").addEventListener("click", page1)
  document.querySelector(".page-btn2").addEventListener("click", page2)
  document.querySelector(".page-btn3").addEventListener("click", page3)
  document.querySelector(".page-btn4").addEventListener("click", page4)
