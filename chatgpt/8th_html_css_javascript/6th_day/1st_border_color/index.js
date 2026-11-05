/* for (let i =1; i < 10; i++) {
    if (i === 3) { continue;}
    console.log( "The number is " + i )
} */

let text = ""

loop1: for (let j = 1; j < 5; j++) {
    loop2: for (let i = 1; i < 5; i++) {
        if (i === 3) {continue loop1;}
        text += 1
        console.log(text)
    }
}

