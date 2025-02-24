const storedData = localStorage.getItem('db');
let s=storedData.split('');
s.pop()
let name=s.join('');
localStorage.setItem("endpointname", name);
if (storedData) {
    document.querySelector(".namebd").textContent = "Записи таблицы " + storedData;

}
async function regaccept() {
    await link()
    await perebor(storedData)
    const res = await fetch(`/${name}/read`);
    data = await res.json();
   await perebor2(storedData,data)
    
  
 
 
 


}
async function  link() {

   
    const res = await fetch("/admin/database_schema");
    data =await res.json();
 
    let a=Object.keys(data)

    for(let i=0;i<a.length;i++){
        
        let namedb=a[i];

        let sidebar=document.querySelector(".sidebar");
        const link = document.createElement('a');
        link.href = "#";
        link.textContent = namedb;
        
      
        link.classList.add('nav-item1');
     
    
      
        sidebar.appendChild(link);
           
        link.addEventListener("click", function() {
            window.location.href = '/admin_db_tables';
            localStorage.setItem("db", namedb); 
          });}
        }
async function  perebor(namebd) {
    let theadHTML = '<thead><tr>';
   
    const res = await fetch("/admin/database_schema");
    data =await res.json();

    let a=Object.keys(data)

    for(let i=0;i<a.length;i++){
      
        
        if(a[i]==namebd){
            for(let j=1;j<data[namebd].length;j++){
           
                for (let j = 1; j < data[namebd].length; j++) {
                    let v = data[namebd][j].name;
                    theadHTML += `<th>${v}</th>`;
                    
                } break}
        }
       
    
    
    
    }
    theadHTML += '</tr></thead>'; 

    document.querySelector(".table").innerHTML+= theadHTML;
  
    

}
async function  perebor2(namebd,data) {
    let tbodyHTML = '<tbody>';
    const res = await fetch("/admin/database_schema");
    ff =await res.json();

    let a=Object.keys(ff)
   

    for(let i=0;i<a.length;i++){

        if(a[i]==namebd){
            for(let j=1;j<ff[namebd].length;j++){
                let s=0
                for (let j = 1; j < ff[namebd].length; j++) {      
                s+=1

                            for(let l=0;l<data.length;l++){
                                if (s<2){
                                    tbodyHTML+= `<tr>`
                                    for (let j = 1; j < ff[namebd].length; j++) {
                                        let va=ff[namebd][j].name
                                        tbodyHTML += `<td>${data[l][va]}</td>`;
                                    
                                    
                                    }
                                    tbodyHTML+= `</tr>`}
                                    
                                }
   
                } break}
                tbodyHTML+=`</tbody>`;
                document.querySelector(".table").innerHTML+= tbodyHTML;
        }
       
    
    
    
    }


}
regaccept();



