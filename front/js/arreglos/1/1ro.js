const llenar_lista=()=>{
    var vec=Array()
    let tam=parseInt(Math.random()*(15-5)+5)
    for (var i=0;i<tam;i++){
        vec[i]=parseInt(Math.random()*10)
    }
    return vec
}

let vector=llenar_lista()

let menu=()=>{

    // console.log(vector)
    // console.log(vector.length)
    
    let opcion=prompt('Seleccione una opcion:\n 1. Para imprimir el arreglo original \n 2. Suma \n 3. Promedio \n 4. Mayor \n 5. Menor \n 6. Ordenar ascendente \n 7. Ordenar descendente \n 8.Moda \n 9. Mediana \n 10. Buscar')
    switch(opcion){
        case '1':
            console.log(vector)
            return console.log(menu())
        case '2':
            let suma_vector=vec=>{
                let suma=0
                for (var i=0; i<vec.length;i++){
                    suma+=vec[i]
                }
                return suma
            }
            console.log(suma_vector(vector))
            return console.log(menu())

        case '3':
            let suma_promedio=vec=>{
                let suma=0
                for (var i=0; i<vec.length;i++){
                    suma+=vec[i]
                }
                promedio=suma/(vector.length)
                return promedio
            }
            console.log(`Tamaño de la lista ${vector.length}`)
            console.log(suma_promedio(vector))
            return console.log(menu())
        case '4':
            let numero_mayor=(vec)=>{
                mayor=0

                mayor=vec[0]
                for (var i=1;i<vec.length;i++){
                    if (vec[i]>=mayor){
                        mayor=vec[i]
                    }
                }
                return mayor
            }
            console.log(numero_mayor(vector))
            return console.log(menu())
        case '5':
            let numero_menor=(vec)=>{
                minimo=0

                minimo=vec[0]
                for (var i=1;i<vec.length;i++){
                    if (vec[i]<=minimo){
                        minimo=vec[i]
                    }
                }
                return minimo
            }
            console.log(numero_menor(vector))
            return console.log(menu())
        case '6':
            let ascendente=vec=>{
                for (let i=0; i<vec.length; i++){
                    let minimo=i
                    for (let l=i +1;l<vec.length; l++){
                        if (vec[l]<vec[minimo]){
                            minimo=l
                        }
                    }
                    if (minimo !==i){
                        let num=vec[i]
                        vec[i]=vec[minimo]
                        vec[minimo]=num
                    }
                }
                console.log(vec)
            }
            console.log(ascendente(vector))
            return console.log(menu())

        case '7':
            let descendente=vec=>{
                for (let i=0; i<vec.length; i++){
                    let minimo=i
                    for (let l=i +1;l<vec.length; l++){
                        if (vec[l]>vec[minimo]){
                            minimo=l
                        }
                    }
                    if (minimo !==i){
                        let num=vec[i]
                        vec[i]=vec[minimo]
                        vec[minimo]=num
                    }
                }
                console.log(vec)
            }
            console.log(descendente(vector))
            return console.log(menu())

        case '8':
            let moda=vec=>{
                for (let i=0; i<vec.length; i++){
                
                }
            }
        case '9':
            break
            // let calculo_mediana=vec=>{
            //     mediana=vector.length/2
            //     console.log(mediana)

            //     for (let i=0; i<vec.length; i++){
            //         console.log((i[mediana]))

            //     }
            // }
            // console.log(calculo_mediana(vector))
        case '10':
            let buscar_numero=vec=>{
                let numero = parseInt(prompt('Ingrese el numero que desea buscar en la lista'))
                for (var i=0; i<vec.length;i++){
                    if (vec[i]===numero){
                        console.log(`El numero ${numero} se encuentra en la posicion ${i}`)
                    }
                    else if (minimo!= vec[i]){
                        console.log('NO')
                    }                
                }
            }
            console.log(buscar_numero(vector))

    }
}

menu()