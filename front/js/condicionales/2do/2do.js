// let num1=parseInt(prompt('Ingrese el primer numero: '))
// let num2=parseInt(prompt('Ingrese el segundo numero: '))
// let num3=parseInt(prompt('Ingrese el tercer numero: '))

// if(num1==num2 && num1==num3){
//     console.log('Todos los numeros son iguales')
// } 
// else if (num1==num2 && num1!=num3){
//     console.log('Solo el primer y el segundo numero son iguales')
// }

// else if (num1==num3 && num1!=num2){
//     console.log('Solo el primer y el tecer numero son iguales')
// }

// else if (num3==num2 && num3!=num1){
//     console.log('Solo el segundo y tercer numero son iguales')
// }

// else{
//     console.log('Ningun numero es igual')
// }

function segundo(){
    let num1=parseInt(prompt('Ingrese el primer numero: '))
    let num2=parseInt(prompt('Ingrese el segundo numero: '))
    let num3=parseInt(prompt('Ingrese el tercer numero: '))

    if(num1==num2 && num1==num3){
        console.log('Todos los numeros son iguales')
    } 
    else if (num1==num2 && num1!=num3){
        console.log('Solo el primer y el segundo numero son iguales')
    }

    else if (num1==num3 && num1!=num2){
        console.log('Solo el primer y el tercer numero son iguales')
    }

    else if (num3==num2 && num3!=num1){
        console.log('Solo el segundo y tercer numero son iguales')
    }

    else{
        console.log('Ningun numero es igual')
    }
}

console.log(segundo())