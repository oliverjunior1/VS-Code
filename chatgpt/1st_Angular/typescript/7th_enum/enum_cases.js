"use strict";
/* enum CardinalDirections {
    North,
    East,
    South,
    West
}

let currentDirection = CardinalDirections.North

console.log(currentDirection) */
var CardinalDirections;
(function (CardinalDirections) {
    CardinalDirections[CardinalDirections["North"] = 1] = "North";
    CardinalDirections[CardinalDirections["East"] = 2] = "East";
    CardinalDirections[CardinalDirections["South"] = 3] = "South";
    CardinalDirections[CardinalDirections["West"] = 4] = "West";
})(CardinalDirections || (CardinalDirections = {}));
console.log(CardinalDirections.North);
console.log(CardinalDirections.West);
