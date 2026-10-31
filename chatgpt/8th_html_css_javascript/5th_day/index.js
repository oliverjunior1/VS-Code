/* for (let i = 0; i < 10; i++) {
    if (i===3) {break;}
    console.log("The number is " + i)
}
 */

/* switch (new Date().getDay()) {
    case 0:
        day = "Sunday"
        break
    case 1:
        day = "Monday"
        break
    case 2:
        day = "Tuesday"
        break
    case 3:
        day = "Wednesday"
        break
    case 4:
        day = "Thursday"
        break
    case 5:
        day = "Friday"
        break
    case 6:
        day = "Saturday"
    }

console.log(day) */

let text = " "

loop1: for (let j = 1; j < 5; j++) {
    loop2: for (let i = 1; i < 5; i++) {
        if (i===3) {break loop1}
        text += i
        console.log(text)
    }
}

