function changeText(){
    document.getElementById("message").innerText="This text changed";

}
function changeColor(){
    document.getElementById("message").style.color="Blue";
}
function showText() {
  let name = document.getElementById("name").value;
  document.getElementById("title").innerText = "Hello, " + name;
}
