function caller(callback) {
  callback();
}

// function anotherFunc() {
//   console.log("hello");
// }

caller(function() {
  console.log("hello");
});