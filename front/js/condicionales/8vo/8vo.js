// const llamada =parseInt(prompt('¿Cuanto tiempo duró la llamada? En minutos por favor'))

// costo=0
// if (llamada<=3){
//     console.log('El costo es de 200')
// }
// else if (llamada>3){
//     minutosDeMas=llamada-3
//     calculo=minutosDeMas*50
//     costo=200+calculo
//     console.log(`El valor a pagar es de ${costo}`)
// }

function llam(){
    const llamada =parseInt(prompt('¿Cuanto tiempo duró la llamada? En minutos por favor'))
    costo=0
    if (llamada<=3){
        console.log('El costo es de 200')
    }
    else if (llamada>3){
        minutosDeMas=llamada-3
        calculo=minutosDeMas*50
        costo=200+calculo
        console.log(`El valor a pagar es de ${costo}`)
    }
}

console.log(llam())