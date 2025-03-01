
const endpointname = localStorage.getItem('endpointname');

let dbname = endpointname;
let names=dbname+"s"

async function osnov() {
   
    const res = await fetch(`/${dbname}/read`);
    data = await res.json();
  console.log(names)
 
   console.log(data)
   document.addEventListener('click',async function(event) {

   
      
    if (event.target.classList.contains('btn-rec')) {
       
     
      
       
      
      if(names=="files"){
        postbd2()
      }else{
        postbd()
      }
       
           
      

    }
  });
  document.addEventListener('click', function(event) {
    if (event.target.classList.contains('close')) {
        document.querySelector('.new-record').style.display="none"
        clear()
        andiasble()
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
                document.querySelector(".btn-osn").innerHTML+=`<button class="btnform btn-rec">Добавить</button><button class="btnform  close">Закрыть</button>`
            }
            if(fun==2&&j>=data[names].length-1){
                document.querySelector(".btn-osn").innerHTML+=`<button class="btnform btn-save">Изменить</button><button class="btnform close">Закрыть</button>`
            }
                if(v=="id"||v=="created_at"||v=="updated_at"){
                    continue
                }
                
            else{
   
                if(names=="files"){
                 form.innerHTML+='<div class="form-group" ><h3 class="form-label" style="display:none">'+v+'</h3>'+'<input  type="file" id="fileInput" multiple>'+'</div>'

                }else{
                    if(v=="started_at"||v=="deadline"||v=="ended_at"||v=="assigned_at"){
                        form.innerHTML+='<div class="form-group" ><h3 class="form-label">'+v+'</h3><input  type="date" class="form-input inp-date" name="'+v+'"'+'>'+'</div>'}
                        else{
                                form.innerHTML+='<div class="form-group" ><h3 class="form-label">'+v+'</h3><input  type="text" class="form-input" name="'+v+'"'+'>'+'</div>'
                        }
                      
                }
                    
               
                    
                
                
            }
             
            
         }
         break;
     }
 }


}

  
  async function postbd2() { 
    const fileInput = document.getElementById('fileInput');
  
    fileInput.addEventListener('change', async  function ass(event)  {
      const files = event.target.files;
  
      if (files.length > 0) {
        console.log("Выбранные файлы:", files);
        return files
      
      } else {
        console.log("Файлы не выбраны");
      }  });
   
      try {
        const files = await fileInput.files;
       
        const formData = new FormData();
    
        
        for (let i = 0; i < files.length; i++) {
          formData.append('myfile', files[i], files[i].name); 
        }
    
        const response = await fetch(`/${dbname}/create`, {
          method: 'POST',
          body: formData,
        });
    
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
    
        const responseData = await response.json();
        if (responseData) {
          window.location.reload();
        }
        console.log("Успешный ответ (файлы):", responseData);
        
      } catch (error) {
        console.error("Ошибка при отправке данных файлов:", error);
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
  if (responseData) {
    window.location.reload();
  }

} 
async function andiasble() {
  document.querySelector(".backgr").style.display="none"
}
async function disable(){

  console.log("disable") 
  document.querySelector(".backgr").style.display="flex"


  
}
osnov()
document.addEventListener('click',async function(event) {
    if (event.target.classList.contains('btn-primary')) {
        document.querySelector('.new-record').style.display="flex"
        console.log("disable")
       formgenerates(1)
      
        disable()
     
    }
  });
