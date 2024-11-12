// let  num=parseInt(prompt('Ingrese un numero'))
// let a=1
// let y=0

// while (a <= num){
//     if (num % a ==0){
//         y+=1
//     }
//     a+=1
// }
// if (y==2){
//     console.log(`${num} es primo`)
// }

// else{
//     console.log(`${num} no es primo`)
// }

function primos(){
    let  num=parseInt(prompt('Ingrese un numero'))
    let a=1
    let y=0

    while (a <= num){
        if (num % a ==0){
            y+=1
        }
        a+=1
    }
    if (y==2){
        console.log(`${num} es primo`)
    }
    else{
        console.log(`${num} no es primo`)
    }
}

console.log(primos())