enemyHealth = Math.floor(Math.random() * 21) + 40;
// function to generate a random numeric value
var randomNumber = function() {
  var value = Math.floor(Math.random() * 21) + 40;

  return value;
};
var randomNumber = function(min, max) {
  var value = Math.floor(Math.random() * (max - min + 1) + min);

  return value;
};
var randomNumber = function(40, 60) {
  var value = Math.floor(Math.random() * (60 - 40 + 1)) + 40;

  return value;
};