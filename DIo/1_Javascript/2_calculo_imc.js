let weight = Number(prompt("Type your weight: "))
let height = Number(prompt("Type your height: "))

let imc = weight / (height ** 2)

if (imc < 18.5) {
    alert("low weight")
}
else if (imc >= 18.5 && imc < 25) {
    alert("normal weight")
}
else if (imc >= 25 && imc < 30) {
    alert("overweight")
}
else if (imc >= 30 && imc < 35) {
    alert("obesity")
}
else {
    alert("severe obesity")
}