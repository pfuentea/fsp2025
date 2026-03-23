$(document).ready(function(){

    $('#cargar').on('click',function(){
        cargar();
    })

    function cargar(){
        //definimos la url de la api (endpoint)
        let url_base='https://akabab.github.io/starwars-api/api/all.json';
        // hacemos una llamada a la API
        $.get(url_base,function(data){ // en data queda la respuesta
            // tomamos los primeros 10 elemento 0-9 y los dejamos en el arreglo personajes
            let personajes = data.slice(0,9);
            // recorremos el arreglo y vamos tomando los campos que vamos a usar
            personajes.forEach(p => {
                
                console.log(p);// mostrando la info por cada elemento del arreglo
                //construimos la visualización de la data
                let carta=`
                <div>
                    <img src="${p.image}" width="200px" heigth="250px" >
                    <p></p>
                    <p5>${p.name} </p5>
                    <p>${p.species}-${p.homeworld} </p>
                </div>     
                `;
                // lo agregamos al DOM al final de todo
                $("body").append(carta);
    
            } );
        });
        
    }
});