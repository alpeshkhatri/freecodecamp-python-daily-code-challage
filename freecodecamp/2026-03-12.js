// Domino Chain Validator
// Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
//
// Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
// For the chain to be valid, the second number of each domino must match the first number of the next domino.
// The first number of the first domino and the last number of the last domino don't need to match anything.

function isValidDominoChain(args) {
  console.log(args);
  for (let i = 0; i < args.length - 1; i++) {
    if (args[i][1] !== args[i + 1][0]) {
      return false;
    }
  }
  return true;
}
// Tests
const tests = [
  [
    isValidDominoChain([
      [1, 3],
      [3, 6],
      [6, 5],
    ]),
    true,
  ],
  [
    isValidDominoChain([
      [6, 2],
      [3, 4],
      [4, 1],
    ]),
    false,
  ],
  [
    isValidDominoChain([
      [2, 5],
      [5, 6],
      [5, 1],
    ]),
    false,
  ],
  [
    isValidDominoChain([
      [4, 3],
      [3, 1],
      [1, 6],
      [6, 6],
      [6, 5],
      [5, 1],
      [1, 1],
      [1, 4],
      [4, 4],
      [4, 2],
    ]),
    true,
  ],
  [
    isValidDominoChain([
      [2, 3],
      [3, 3],
      [3, 6],
      [6, 1],
      [1, 4],
      [3, 5],
      [5, 5],
      [5, 4],
      [4, 2],
      [2, 2],
    ]),
    false,
  ],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
