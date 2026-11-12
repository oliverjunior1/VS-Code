"use strict";
/* enum CardinalDirections {
    North,
    East,
    South,
    West
}

let currentDirection = CardinalDirections.North

console.log(currentDirection) */
/* enum CardinalDirections {
    North = 1,
    East,
    South,
    West
}

console.log(CardinalDirections.North)
console.log(CardinalDirections.West) */
/* enum StatusCodes {
    NotFound = 404,
    Success = 200,
    Accepted = 202,
    BadRequest = 400
}

console.log(StatusCodes.NotFound)
console.log(StatusCodes.Success) */
var CardinalDirections;
(function (CardinalDirections) {
    CardinalDirections["North"] = "North";
    CardinalDirections["East"] = "East";
    CardinalDirections["South"] = "South";
    CardinalDirections["West"] = "West";
})(CardinalDirections || (CardinalDirections = {}));
console.log(CardinalDirections.North);
console.log(CardinalDirections.West);
