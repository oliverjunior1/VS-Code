// any
/* let u = true
u = "string"
Math.round(u) */

/* let v: any = true
v = "string"
Math.round(v) */


/* let w: unknown = 1;
w = "string"; // no error
w = {
  runANonExistentMethod: () => {
    console.log("I think therefore I am");
  }
} as { runANonExistentMethod: () => void}
// How can we avoid the error for the code commented out below when we don't know the type?
// w.runANonExistentMethod(); // Error: Object is of type 'unknown'.
if(typeof w === 'object' && w !== null) {
  (w as { runANonExistentMethod: Function }).runANonExistentMethod();
}
// Although we have to cast multiple times we can do a check in the if to secure our type and have a safer casting */

// Optional parameter (implicitly `string | undefined`)
/* function greet(name?: string) {
  return `Hello, ${name || 'stranger'}`;
}

// Optional property in an interface
interface User {
  name: string;
  age?: number; // Same as `number | undefined`
} */

/* // Nullish coalescing (??) - only uses default if value is null or undefined
const value = input ?? 'default';

// Optional chaining (?.) - safely access nested properties
const street = user?.address?.street; */

