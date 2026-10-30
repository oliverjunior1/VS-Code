/* let names: string[] = []
names.push("Dylan")

console.log(names) */

// read only
/* let names: readonly string[] = ["Dylan"]
names.push("Jack")

console.log(names) */

// typescript can infer the type of an array if it has values
let numbers = [1,2,3]
numbers.push(4)
console.log(numbers)