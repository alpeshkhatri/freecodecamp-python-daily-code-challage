function sumLetters(str) {
  console.log(str);
  let sum = 0;
  for (const x of str) {
    let y = x.toLowerCase();
    if (/^[a-zA-Z]$/.test(y)) {
      sum += 1 + (y.charCodeAt(0) - "a".charCodeAt(0));
      // console.log(sum);
    }
  }
  return sum;
}
// Tests
const tests = [
  [sumLetters("Hello"), 52],
  [sumLetters("freeCodeCamp"), 94],
  [sumLetters("The quick brown fox jumps over the lazy dog."), 473],
  [
    sumLetters(
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.",
    ),
    1681,
  ],
  [sumLetters("</404>"), 0],
];

tests.forEach(([result, expected], i) => {
  const pass = result === expected;
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
