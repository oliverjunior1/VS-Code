/* type CarYear = number
type CarType = string
type CarModel = string
type Car = {
    year: CarYear,
    type: CarType,
    model: CarModel
}

let carYear: CarYear = 2001
let cartType: CarType = "Toyota"
let carModel: CarModel = "Corolla"
let car: Car = {
    year: carYear,
    type: cartType,
    model: carModel
}

console.log(carYear)
console.log(cartType)
console.log(carModel) */

/* type Animal = {name: string}
type Bear = Animal & {honey: boolean}
let bear: Bear = {name: "Winnie", honey: true}

type Status = "success" | "error"
let response: Status = "success"

console.log(bear)
console.log(response)
console.log(bear) */

interface Rectangle {
    height: number,
    width: number
}

let rectangle: Rectangle = {
    height: 20,
    width: 10
}

console.log(rectangle)