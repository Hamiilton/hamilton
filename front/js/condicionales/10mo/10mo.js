// let hora =parseFloat(prompt('Ingrese la hora'))
// let minutos =parseFloat(prompt('Ingrese la minutos'))
// let segundos =parseFloat(prompt('Ingrese la segundos'))

// if (segundos<59){
//     seg=segundos+1
//     console.log(`La hora un segundo despues es: ${hora}:${minutos}:${seg}`)
// }
// else if(segundos==59 && minutos <=58){
//     min=minutos+1
//     console.log(`La hora un segundo despues es: ${hora}:${min}:00`)
// }
// else if (hora==24 && minutos==59 && segundos==59){
//     console.log(`La hora un segundo despues es: 00:00:00`)
// }
// else if(segundos==59 && minutos==59){
//     h=hora+1
//     console.log(`La hora un segundo despues es: ${h}:00:00`)
// }

function decimo(){
    let hora =parseFloat(prompt('Ingrese la hora'))
    let minutos =parseFloat(prompt('Ingrese la minutos'))
    let segundos =parseFloat(prompt('Ingrese la segundos'))

    if (segundos<59){
        seg=segundos+1
        console.log(`La hora un segundo despues es: ${hora}:${minutos}:${seg}`)
    }
    else if(segundos==59 && minutos <=58){
        min=minutos+1
        console.log(`La hora un segundo despues es: ${hora}:${min}:00`)
    }
    else if (hora==24 && minutos==59 && segundos==59){
        console.log(`La hora un segundo despues es: 00:00:00`)
    }
    else if(segundos==59 && minutos==59){
        h=hora+1
        console.log(`La hora un segundo despues es: ${h}:00:00`)
    }
}

console.log(decimo())