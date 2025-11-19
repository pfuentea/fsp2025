let usuarioValido='admin' ;
let contrasenaValida='adm123';
const LS_CURRENT_USER_KEY= 'currentUser';


$(document).ready(function(){

   $('#loginForm').on('submit',function(e){
        e.preventDefault();
        const user=$('#username').val();
        const pwd=$('#clave').val();
        console.log('usr:',user)
        console.log('pwd:',pwd)

        if(user==usuarioValido && pwd==contrasenaValida){
            
            localStorage.setItem(LS_CURRENT_USER_KEY , JSON.stringify(user));
            

            console.log('ok login')
            //localStorage.setItem('currentUser',user);
            window.location.href='index.html';            
        }
        else{
            $('#errorMsg').removeClass('d-none')
        }

   })
});

function getCurrentUser(){
    const data = localStorage.getItem(LS_CURRENT_USER_KEY);
    if (!data) return null;

    try{
        return JSON.parse(data);
    } catch(e){
        return null;
    }
} 



