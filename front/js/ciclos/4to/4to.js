for (let i=1;i<=1000;i++){
    let z =2
    let suma=0
    while (z<=i){
        if (i%z==0){
            suma+=i/z
        }
        z+=1
    }
    if (suma==i){
        console.log(`${i}`)
    }
}

function perfectos(){
    for (let i=1;i<=1000;i++){
        let z =2
        let suma=0
        while (z<=i){
            if (i%z==0){
                suma+=i/z
            }
            z+=1
        }
        if (suma==i){
            console.log(`${i}`)
        }
    }
}

console.log(perfectos())