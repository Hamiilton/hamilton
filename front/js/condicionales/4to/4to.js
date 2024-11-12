// let nota=parseFloat(prompt('Ingrese su nota: '))

// if (nota<=2){
//     console.log('Reprobado')
// }
// else if (nota <=4){
//     console.log('NO PASA')
// }
// else if(nota<=6){
//     console.log('INSUFICIENTE')
// }
// else if (nota <=8){
//     console.log('Bien')
// }
// else if (nota <=10){
//     console.log('EXELENTE')
// }
// else{
//     console.log('Nota invalida - Recuerde que es de 0 a 10')
// }

function cuarto(){
    let nota=parseFloat(prompt('Ingrese su nota: '))

    if (nota<=2){
        console.log('Reprobado')
    }
    else if (nota <=4){
        console.log('NO PASA')
    }
    else if(nota<=6){
        console.log('INSUFICIENTE')
    }
    else if (nota <=8){
        console.log('Bien')
    }
    else if (nota <=10){
        console.log('EXELENTE')
    }
    else{
        console.log('Nota invalida - Recuerde que es de 0 a 10')
    }
}

console.log(cuarto())