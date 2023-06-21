
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e)=>{
    let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
    arrowParent.classList.toggle("showMenu");
  });
}

let setText=true
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".btn-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", ()=>{
  let equipo=document.getElementById("equipo");
  sidebar.classList.toggle("close");
  if(setText){
    equipo.innerHTML="<b>DevCoders</b>"
    setText=false
  }else{
    equipo.innerHTML=""
    setText=true
  }
});





