function getOddWords(args) {
  console.log(JSON.stringify(args));
  const ret = args.split(" ").filter((w) => w.length % 2 === 1);
  console.log(ret.join(" "));
  return ret.join(" ");
}
// Tests
const tests = [
  [getOddWords("This is a super good test"), "a super"],
  [getOddWords("one two three four"), "one two three"],
  [
    getOddWords("banana split sundae with rainbow sprinkles on top"),
    "split rainbow sprinkles top",
  ],
  [
    getOddWords("The quick brown fox jumped over the lazy river"),
    "The quick brown fox the river",
  ],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
