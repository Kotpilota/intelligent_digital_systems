
const endpointname = localStorage.getItem('endpointname');

let dbname = endpointname;
let names=dbname+"s"

async function osnov() {
   
    const res = await fetch(`/${dbname}/read`);
    data = await res.json();
  
 
   console.log(data)
   document.addEventListener('click', function(event) {
  
    if (event.target.classList.contains('btn-rec')) {
        postbd()  
        window.location.reload();
    }
  });
  document.addEventListener('click', function(event) {
    if (event.target.classList.contains('close')) {
        document.querySelector('.new-record').style.display="none"
        clear()
    }
  });
   
}
async function clear() {
    document.querySelector('.form').innerHTML=""
    document.querySelector(".btn-osn").innerHTML=""
}
async function formgenerates(fun) {
let form=document.querySelector('.form')
 const res = await fetch("/admin/database_schema");
 data = await res.json();


 let a = Object.keys(data);
 for (let i = 0; i < a.length; i++) {
    
     if (a[i] == names) {
         for (let j = 1; j < data[names].length+1; j++) {
           
             let v = data[names][j].name
             console.log(data[names].length,j);
             if(fun==1&&j>=data[names].length-1){
                document.querySelector(".btn-osn").innerHTML+=`<button class=" btn-rec">Добавить</button><button class="close">Закрыть</button>`
            }
            if(fun==2&&j>=data[names].length-1){
                document.querySelector(".btn-osn").innerHTML+=`<button class=" btn-save">Изменить</button><button class="close">Закрыть</button>`
            }
                if(v=="id"||v=="created_at"||v=="updated_at"){
                    continue
                }
                
            else{
                
               
                    
               
                    form.innerHTML+='<div class="form-group" ><h3 class="form-label">'+v+'</h3><input type="text" class="form-input" name="'+v+'>"'+'</div>'
                
                
            }
             
            
         }
         break;
     }
 }


}
 
async function postbd()
{
    let input=document.querySelectorAll('.form-input')

    const data = {}; 

    input.forEach(element => {
    const names=element.name
    const name=names.slice(0,-1)
      let value = element.value; 
      
      console.log(name,value); 

     
      
        data[name]= value;
      
    });
    console.log(data);
   const rec=await fetch(`/${dbname}/create`, {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify(data)

   
   })


  const responseData = await rec.json(); 
  console.log("Успешный ответ:", responseData);


} 
osnov()
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('btn-primary')) {
        document.querySelector('.new-record').style.display="flex"
         formgenerates(1)
    }
  });
