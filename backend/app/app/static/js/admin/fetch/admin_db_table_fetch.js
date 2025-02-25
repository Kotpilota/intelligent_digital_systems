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
   document.addEventListener('click', function(event) {
    if (event.target.classList.contains('btn-danger')) {
      deletebd()
    }
  });
  
 
 
 


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
    let tbodyHTML = '<tbody class="tbody">';
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
                                    tbodyHTML+= `<tr >`
                                    for (let j = 1; j < ff[namebd].length+1; j++) {
                                      if(j<ff[namebd].length){
                                        let va=ff[namebd][j].name
                                        if(ff[namebd][j].name=="id"){
                                            document.querySelector(".main").innerHTML+=`<div class="id" style="display:none">${data[l][va]}</div>`
                                            tbodyHTML += `<td class="idtb">${data[l][va]}</td>`;
                                        }
                                        else{
                                            tbodyHTML += `<td>${data[l][va]}</td>`;
                                      
                                        }
                                       
                                    
                                      }else{
                                        tbodyHTML+=`<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>`
                                      }
                                    
                                    }
                                    tbodyHTML+= `</tr>`}
                                    
                                }
   
                } break}
                tbodyHTML+=`</tbody>`;
                document.querySelector(".table").innerHTML+= tbodyHTML;
        }
       
    
    
    
    }


}async function deletebd() {
    document.addEventListener('click', async function(event) { 
      if (event.target.classList.contains('btn-danger')) {
        const row = event.target.closest('tr');
  
        if (row) {
          const idtbCell = row.querySelector('.idtb');
  
          if (idtbCell) {
            const idtbValue = idtbCell.textContent;
            console.log('Значение idtb:', idtbValue);
  
            try {
              const response = await fetch(`/${name}/delete/${idtbValue}`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
              });
  
              if (response.ok) {
              
                console.log('Удаление прошло успешно');
                row.remove();
              } else {
                console.error('Ошибка при удалении:', response.status, response.statusText);
         
              }
            } catch (error) {
              console.error('Ошибка сети:', error);
        
            }
  
          } else {
            console.error('Не найдена ячейка с классом "idtb"');
          }
        } else {
          console.error('Не найдена строка таблицы (<tr>)');
        }
      }
    });
  }
 
let datasink = {}; 

async function handleGenerateFormClick(event) {
  if (event.target.classList.contains('btn-success')) {
   
    document.querySelector('.new-record').style.display = 'flex';

   
    await formgenerates(2);

    console.log("Форма сгенерирована");

  }
}


async function handleGenerateFormClick(event) {
    if (event.target.classList.contains('btn-success')) {

        const row = event.target.closest('tr');

        if (row) {
            const idtbCell = row.querySelector('.idtb');

            if (idtbCell) {
                const idtbValue = idtbCell.textContent; 
         
                event.target.dataset.idtbValue = idtbValue; 

                document.querySelector('.new-record').style.display = 'flex';
                await formgenerates(2);
                console.log("Форма сгенерирована");
            } else {
                console.error('Не найдена ячейка с классом "idtb"');
            }
        } else {
            console.error('Не найдена строка таблицы (<tr>)');
        }
    }
}


async function handleUpdateClick(event) {
    if (event.target.classList.contains('btn-save')) {
        const form = document.querySelector('.new-record'); 
        if (form) {

            const datasink = {}; 
            const input = form.querySelectorAll('input'); 
            input.forEach(element => {
                const names = element.name;
                const name = names.slice(0, -1);
                const value = element.value;
                datasink[name] = value;
                console.log(name, value);
            });
     
            const idtbValue = document.querySelector('.btn-success').dataset.idtbValue

            if (idtbValue) {
                console.log("idtbValue", idtbValue)
                try {
                    const response = await fetch(`/${name}/update/${idtbValue}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(datasink),
                    });

                    if (response.ok) {
                        console.log('Обновление прошло успешно');
                        window.location.reload();
                    } else {
                        console.error('Ошибка при обновлении:', response.status, response.statusText);
                    }
                } catch (error) {
                    console.error('Ошибка сети:', error);
                }
            } else {
                console.error("idtbValue не найден")
            }
        } else {
            console.error('Форма с классом ".new-record" не найдена!');
        }

    }
}


document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', handleGenerateFormClick);
    document.addEventListener('click', handleUpdateClick);
});
  
  
  
regaccept();



