// Array Insertion
// Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.
//

function insertIntoArray(arr, value, index) {
  console.log(arr, value, index);
  arr.splice(index, 0, value);
  return arr;
}
// Tests
const tests = [
  [insertIntoArray([2, 4, 8, 10], 6, 2), [2, 4, 6, 8, 10]],
  [
    insertIntoArray(["the", "quick", "fox"], "brown", 2),
    ["the", "quick", "brown", "fox"],
  ],
  [insertIntoArray([], 0, 0), [0]],
  [insertIntoArray([0, 1, 1, 2, 3, 8, 13], 5, 5), [0, 1, 1, 2, 3, 5, 8, 13]],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
