https://courses.bootcampspot.com/

var playerName = window.prompt("What is your robot's name?");
var playerHealth = 100;
var playerAttack = 10;

// You can also log multiple values at once like this
console.log(playerName, playerAttack, playerHealth);

var enemyName = "Roborto";
var enemyHealth = 50;
var enemyAttack = 12;

enemyHealth = enemyHealth - playerAttack;
playerHealth=playerHealth-enemyAttack;
var fight = function() {
 // window.alert("Welcome to Robot Gladiators!");
 //console.log(playerName+" attacked"+enemyName+" ."+enemyName+" now has"+enemyHealth+" health remaining"); 
// console.log(enemyName+" attacked"+playerName+" ."+playerName+" now has"+playerHealth+" health remaining"); 
};



fight();
//var playerHealth=10;
//var enemyHealth=enemyHealth-playerAttack;
//var playerHealth=playerHealth-enemyAttack;

if(playerHealth<=0){
    window.alert(playerName+" has died!");
}
else{
    window.alert(playerName+" still has"+playerHealth+" health left.");
}
