// Inside the <script> element, complete the following steps:
// Write a for loop that counts i from 1 to 10
let text = ""
for (let i = 1; i <=10; i++) {
    if (i==4) {continue}
    console.log(i)
    text += i + " "
}
// Inside the loop, use continue to skip the number 4
// Add each number and a space to text
// The page should show: 1 2 3 5 6 7 8 9 10