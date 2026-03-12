// Word Length Converter
// Given a string of words, return a new string where each word is replaced by its length.
//
// Words in the given string will be separated by a single space
// Keep the spaces in the returned string.
// For example, given "hello world", return "5 5".

function convertWords(args) {
  console.log(args);
  const wordArray = args.split(/\s+/);
  let ret = [];
  for (const word of wordArray) {
    ret.push(word.length);
  }
  const ret1 = ret.join(" ");
  return ret1;
}
// Tests
const tests = [
  [convertWords("hello world"), "5 5"],
  [convertWords("Thanks and happy coding"), "6 3 5 6"],
  [
    convertWords("The quick brown fox jumps over the lazy dog"),
    "3 5 5 3 5 4 3 4 3",
  ],
  [
    convertWords(
      "Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl",
    ),
    "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4",
  ],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
