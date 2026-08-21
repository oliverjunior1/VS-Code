let preco = Number(prompt("Insira o preço do produto"))
let totalAPagar = 0
let forma_de_pagamento = prompt("Coloque a forma de pagamento com (1) à vista, (2) em dinheiro ou Pix, \n(3) parcelado em 2x e (4) parcelado em mais de duas vezes.")
if (forma_de_pagamento==1) {
    totalAPagar = preco*0.9
}else if(forma_de_pagamento==2) {
    totalAPagar = preco*0.85
}else if(forma_de_pagamento==3) {
    totalAPagar= preco
}else {
    totalAPagar = preco*1.1
}

alert("O total a pagar é: R$ "+ totalAPagar.toFixed(2)+".")
console.log("O total a pagar é: R$ "+ totalAPagar.toFixed(2)+".")
