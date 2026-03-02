function myFunction(str) {
  console.log(str);

  return str;
}
// Tests
const tests = [
  [myFunction("str"), "str"],
  [myFunction("str"), "str"],
];

tests.forEach(([result, expected], i) => {
  const pass = result === expected;
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
