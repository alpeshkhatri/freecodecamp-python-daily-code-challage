//
// Playing Card Values
// Given an array of playing cards, return a new array with the numeric value of each card.
//
// Card Values:
//
// An Ace ("A") has a value of 1.
// Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
// Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
// Suits:
//
// Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
// Card Format:
//
// Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
//
function cardValues(str) {
  console.log(str);
  const values = { A: 1, J: 10, Q: 10, K: 10 };
  const ret = [];
  str.forEach((s) => {
    let s1 = s.slice(0, -1);
    if (s1 in values) {
      ret.push(values[s1]);
    } else {
      ret.push(parseInt(s1, 10));
    }
  });

  return ret;
}
// Tests
const tests = [
  [cardValues(["3H", "4D", "5S"]), [3, 4, 5]],
  [cardValues(["AS", "10S", "10H", "6D", "7D"]), [1, 10, 10, 6, 7]],
  [cardValues(["8D", "QS", "2H", "JC", "9C"]), [8, 10, 2, 10, 9]],
  [cardValues(["AS", "KS"]), [1, 10]],
  [cardValues(["10H", "JH", "QH", "KH", "AH"]), [10, 10, 10, 10, 1]],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
