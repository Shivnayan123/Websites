
let bread1 = prompt("which bread would ypu like to hav:-");
let veggies1 = prompt("what are your favorite veggies");
let sauce1 = prompt("which sauce are you like ");

function makeSandwich(bread,veggies,sauce){
    let Sandwich = bread+""+sauce+""+veggies+""+ ""+
    "sandwich is read";
    return Sandwich;

}
let vegSandwich = makeSandwich(bread1,veggies1,sauce1);
document.write(vegSandwich);
 document.getElementsByName("vegSandwich").style.color="blue";

switch (fruittype){
    case "apple":
       console.log("grepabvui")
        break;
        case "Orange":
            document.write("orange is 50rs kg");
            break;
            case "grapes":
        document.write("grapes is 90rs kg");
        break;
        case "Banana":
        document.write("banana is 30rs kg");
        break;  
        default:
            document.write("sorry not avilable")  
}