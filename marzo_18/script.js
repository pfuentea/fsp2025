function cambiarTexto(){

}


function validarRut(rutCompleto) {
    if (!rutCompleto) return false;

    // Limpiar puntos y espacios
    rutCompleto = rutCompleto.replace(/\./g, '').replace(/\s/g, '');

    // Validar formato general
    if (!/^\d+-[\dkK]$/.test(rutCompleto)) return false;

    const partes = rutCompleto.split('-');
    const cuerpo = partes[0];
    let dvIngresado = partes[1].toLowerCase();

    let suma = 0;
    let multiplo = 2;

    for (let i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo[i], 10) * multiplo;
        multiplo = multiplo < 7 ? multiplo + 1 : 2;
    }

    const resto = suma % 11;
    const dvEsperado = 11 - resto;

    let dvCalculado = '';
    if (dvEsperado === 11) {
        dvCalculado = '0';
    } else if (dvEsperado === 10) {
        dvCalculado = 'k';
    } else {
        dvCalculado = String(dvEsperado);
    }

    return dvCalculado === dvIngresado;
}
