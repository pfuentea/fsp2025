$(document).ready(function(){

    // ESTA ES LA CARGA INICIAL
   

    let url_base='https://akabab.github.io/starwars-api/api/all.json';
    let personajesTotal=[];

    $.get(url_base,function(data){
        let planetas=[];
        personajesTotal=data;
        data.forEach(p => {
            if(p.homeworld && !planetas.includes(p.homeworld)){
                planetas.push(p.homeworld);
            }
        });
        planetas.sort();

        planetas.forEach(planeta=>{
            $('#planetas').append(`<option value="${planeta}">${planeta} </option>`);
        });
    });

    $('#planetas').change(function(){
        let seleccionado=$(this).val();
        $('#resultado').empty();
        if (seleccionado==="") return;
        let filtrados=personajesTotal.filter(p=>
            p.homeworld===seleccionado
        );

        $('#titulo').text("Personajes de "+seleccionado);

        filtrados.forEach(p=>{
            let carta=`
                <div class="mx-3 mt-3">
                    <img src="${p.image}" width="200px" height="250px" >
                    <p></p>
                    <p5>${p.name} </p5>
                    <p>${p.species}-${p.homeworld} </p>
                </div>     
                `;
                // lo agregamos al DOM al final de todo
                $("#resultado").append(carta);
        });

    });


    $('#cargar').on('click',function(){
        cargar();
    })

    function cargar(){
        //definimos la url de la api (endpoint)
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
                $("#resultado").append(carta);
    
            } );
        });
        
    }
});