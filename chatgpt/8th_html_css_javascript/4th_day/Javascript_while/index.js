// while

/*let  i = 0
while (i < 10) {
    console.log(i)
    i++
} */

// do while
/* let i = 0
do {
    console.log(i)
    i++
} while (i < 10) */

// do while with text
/* let i = 0;
do {
    console.log("The number is " + i)
    i++
} while (i < 10) */

// Comparing for and while

/* let cars = ["BMW", "Volvo", "Saab", "Ford"]
let i = 0;
let text = " "

for (;cars[i];) {
    text += cars[i] + " "
    console.log(text)
    i++
}
 */

const cars = ["BMW", "Volvo", "Saab", "Ford"];
let i = 0;
let text = "";

while (cars[i]) {
    text += cars[i] + " "
    console.log(text)
    i++
    
}