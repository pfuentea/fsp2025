const LS_CURRENT_SALDO = 'currentSaldo';

function setSaldo(saldo){
    localStorage.setItem(LS_CURRENT_SALDO,JSON.stringify(saldo));
}

function getSaldo(){
    const data = localStorage.getItem(LS_CURRENT_SALDO);
    if(!data){
        setSaldo(0);
        return 0;
    } 
    
    try{
        return JSON.parse(data);
    } catch(e){
        return null;
    }
}