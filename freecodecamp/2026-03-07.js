// HSL Validator
// Given a string, determine whether it is a valid CSS hsl() color value.
//
// A valid HSL value must be in the format "hsl(h, s%, l%)", where:
//
// h (hue) must be a number between 0 and 360 (inclusive).
// s (saturation) must be a percentage between 0% and 100%.
// l (lightness) must be a percentage between 0% and 100%.
// Spaces are only allowed:
//
// After the opening parenthesis
// Before and/or after the commas
// Before and/or after closing parenthesis
// Optionally, the value can end with a semi-colon (";").
//
// For example, "hsl(240, 50%, 50%)" is a valid HSL value.
//
function isValidHSL(args) {
  const t = args.match(/hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)/);

  if (!t) return false;

  const h = parseInt(t[1]);
  const s = parseInt(t[2]);
  const l = parseInt(t[3]);

  return h >= 0 && h <= 360 && s >= 0 && s <= 100 && l >= 0 && l <= 100;
}
// Tests
const tests = [
  [isValidHSL("hsl(240, 50%, 50%)"), true],
  [isValidHSL("hsl( 200 , 50% , 75% )"), true],
  [isValidHSL("hsl(99,60%,80%);"), true],
  [isValidHSL("hsl(0, 0%, 0%) ;"), true],
  [isValidHSL("hsl(  10  ,  20%   ,  30%   )    ;"), true],
  [isValidHSL("hsl(361, 50%, 80%)"), false],
  [isValidHSL("hsl(300, 101%, 70%)"), false],
  [isValidHSL("hsl(200, 55%, 75)"), false],
  [isValidHSL("hsl (80, 20%, 10%)"), false],
];

tests.forEach(([result, expected], i) => {
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  // console.log(pass, JSON.stringify(result), JSON.stringify(expected));
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
});
