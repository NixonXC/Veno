document.getElementById("menu").onclick = function() {
    menuList = document.getElementById("menu-ul")
    if (menuList.style.display == "none") {
        menuList.style.display = "flex"
    }
    else {
        menuList.style.display = "none"
    }
}
window.addEventListener('click', function(e){
    menuList = document.getElementById("menu-ul")
    if (!document.getElementById('menu-ul').contains(e.target) && (!document.getElementById('container').contains(e.target))){
    menuList.style.display = "none"
  } 
})