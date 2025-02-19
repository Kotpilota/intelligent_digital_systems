let searchbut=document.querySelector(".search-button")
searchbut.addEventListener("click",function(event){
            event.stopPropagation();
            document.querySelector(".search").style.width="200px";
            document.querySelector(".search").style.marginLeft="20px"
           

})
document.querySelector(".search").addEventListener("click",function(event){
    event.stopPropagation();})
window.addEventListener("click",function(){
    document.querySelector(".search").style.width="0px";
     document.querySelector(".search").style.marginLeft="0px"

})