$(document).ready(function(){

    $('#cargar').on('click',function(){
        cargar();
    })

    function cargar(){
        let url_base='https://akabab.github.io/starwars-api/api/all.json';
    
        $.get(url_base,function(data){
    
            let personajes = data.slice(0,9);
    
            personajes.forEach(p => {
                console.log(p);
    
                let carta=`
                <div>
                    <img src="${p.image}" width="200px" heigth="250px" >
                    <p></p>
                    <p5>${p.name} </p5>
                    <p>${p.species}-${p.homeworld} </p>
                </div>     
                `;
                $("body").append(carta);
    
            } );
        });
        
    }
});