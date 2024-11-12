// let num = 1
// let suma = 0
// while (num>0){
//     num =parseInt(prompt('Digite un numero'))
//     if (num>0){
//         suma=suma+num
//     }
// }
// console.log(`El resultado es ${suma}`)

function suma(){
    let num = 1
    let suma = 0
    while (num>0){
        num =parseInt(prompt('Digite un numero'))
        if (num>0){
            suma=suma+num
        }
    }
    console.log(`El resultado es ${suma}`)

}
console.log(suma())