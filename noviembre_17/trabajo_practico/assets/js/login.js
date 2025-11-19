let usuarioValido='admin' ;
let contrasenaValida='adm123';

$(document).ready(function(){

   $('#loginForm').on('submit',function(e){
        e.preventDefault();
        const user=$('#username').val();
        const pwd=$('#clave').val();
        console.log('usr:',user)
        console.log('pwd:',pwd)

        if(user==usuarioValido && pwd==contrasenaValida){
            console.log('ok login')
            localStorage.setItem('currentUser',user);
            window.location.href='index.html';            
        }
        else{
            $('#errorMsg').removeClass('d-none')
        }

   })
});

 



