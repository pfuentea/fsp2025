fetch("menu.html")
    .then(res=> res.text())
    .then(html=>{
        const menu =document.getElementById("menu");
        menu.innerHTML=html;
        menu.style.display ="block";
        });


fetch("footer.html")
    .then(res=> res.text())
    .then(html=>{
        const foot =document.getElementById("footer");
        foot.innerHTML=html;
        foot.style.display ="block";
        });



