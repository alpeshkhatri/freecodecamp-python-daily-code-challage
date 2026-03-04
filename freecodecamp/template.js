function myFunction(args) {
  console.log(args);

  return args;
}
// Tests
const tests = [
  [myFunction("str"), "str"],
  [myFunction("str"), "str"],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
