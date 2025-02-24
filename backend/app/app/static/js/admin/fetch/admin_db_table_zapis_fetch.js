const endpointname = localStorage.getItem('endpointname');

let dbname = endpointname;
let names=dbname+"s"

async function osnov() {
    const res = await fetch(`/${dbname}/read`);
    data = await res.json();
  
   await formgenerates(names)
   document.querySelector('.btn-rec').addEventListener('click',postbd)

   
}
async function formgenerates(storedData) {
let form=document.querySelector('.form')
 const res = await fetch("/admin/database_schema");
 data = await res.json();


 let a = Object.keys(data);
 for (let i = 0; i < a.length; i++) {
    
     if (a[i] == storedData) {
         for (let j = 1; j < data[storedData].length; j++) {
             let v = data[storedData][j].name;
        
          
                
                
                
                
            
                 form.innerHTML+='<div class="form-group" ><h3 class="form-label">'+v+'</h3><input type="text" class="form-input" name="'+v+'">"'+'</div">'
            
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
    const name=element.name
      let value = element.value; 
      
      console.log(name,value); 

    
        if (name=="created_at"||name=="updated_at"){
          value="2023-01-01 00:00:00"
        }
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
