// Captured Chess Pieces
// Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.
//
// In chess, you start with 16 pieces:
//
// Piece	Abbreviation	Quantity	Value
// Pawn	"P"	8	1
// Rook	"R"	2	5
// Knight	"N"	2	3
// Bishop	"B"	2	3
// Queen	"Q"	1	9
// King	"K"	1	0
// The given array will only contain the abbreviations above.
// Any of the 16 pieces not included in the given array have been captured.
// Return the total value of all captured pieces, unless...
// If the King has been captured, return "Checkmate".

function getCapturedValue(args) {
  console.log(JSON.stringify(args));
  if (!args.includes("K")) {
    return "Checkmate";
  }
  const quantity = { P: 8, R: 2, N: 2, B: 2, Q: 1, K: 1 };
  const value = { P: 1, R: 5, N: 3, B: 3, Q: 9, K: 0 };
  for (const piece of args) {
    quantity[piece] -= 1;
  }
  console.log(quantity);
  let sum = 0;
  for (const [piece, curr_qty] of Object.entries(quantity)) {
    sum += curr_qty * value[piece];
  }
  console.log("end of function");
  return sum;
}
// Tests
const tests = [
  [
    getCapturedValue([
      "P",
      "P",
      "P",
      "P",
      "P",
      "P",
      "R",
      "R",
      "N",
      "B",
      "Q",
      "K",
    ]),
    8,
  ],
  [getCapturedValue(["P", "P", "P", "P", "P", "R", "B", "K"]), 26],
  [
    getCapturedValue([
      "K",
      "P",
      "P",
      "N",
      "P",
      "P",
      "R",
      "P",
      "B",
      "P",
      "N",
      "B",
    ]),
    16,
  ],
  [
    getCapturedValue([
      "P",
      "Q",
      "N",
      "P",
      "P",
      "B",
      "K",
      "P",
      "R",
      "R",
      "P",
      "P",
      "B",
      "P",
    ]),
    4,
  ],
  [getCapturedValue(["P", "K"]), 38],
  [
    getCapturedValue([
      "N",
      "P",
      "P",
      "B",
      "K",
      "P",
      "Q",
      "N",
      "P",
      "P",
      "R",
      "R",
      "P",
      "P",
      "P",
      "B",
    ]),
    0,
  ],
  [
    getCapturedValue(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]),
    "Checkmate",
  ],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
