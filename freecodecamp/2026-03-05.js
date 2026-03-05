// Smallest Gap
// Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).
//
// There will always be at least one pair of matching characters.
// The returned substring should exclude the matching characters.
// If two or more gaps are the same length, return the characters from the first one.
// For example, given "ABCDAC", return "DA".
//
// Only "A" and "C" repeat in the string.
// The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
// So return the string between the two "C" characters.

function smallestGap(args) {
  const seen = {};
  let smallestLen = Infinity;
  let start = 0,
    end = 0;

  for (let idx = 0; idx < args.length; idx++) {
    const s = args[idx];
    if (s in seen) {
      const length = idx - seen[s];
      if (length < smallestLen) {
        smallestLen = length;
        start = seen[s];
        end = idx;
      }
    }
    seen[s] = idx;
  }

  return args.slice(start + 1, end);
}
// Tests
const tests = [
  [smallestGap("ABCDAC"), "DA"],
  [smallestGap("racecar"), "e"],
  [smallestGap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"), "#q6e&rkf(p"],
  [smallestGap("Hello World"), ""],
  [smallestGap("The quick brown fox jumps over the lazy dog."), "fox"],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
