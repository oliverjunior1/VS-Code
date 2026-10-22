"use strict";
/* // String
let greeting: string = "Hello, Typescript!";

// Number
let userCount: number = 42;

// Boolean
let isLoading: boolean = true;

// Array of numbers
let scores: number[] = [100, 95, 98];

// Output the values
console.log(greeting)
console.log(userCount)
console.log(isLoading)
console.log(scores)

 */
// Function with explicit parameter and return types
/* function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Typescript will ensure you pass the correct argument type
 
// greet(42); // Error


console.log(greet("Alice")) // OK */
// Basic type inference
// TypeScript infers 'string'
let username = "Alice";
// Typescript infers 'number'
let score = 100;
// Typescript infers 'boolean[]'
let flags = [true, false, true];
// Typescript infers return type as 'number'
function add(a, b) {
    return a + b;
}
console.log(username);
console.log(score);
console.log(flags);
console.log(add(5, 3));
