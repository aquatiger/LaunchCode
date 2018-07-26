<html>
  <body>
  <input id="first" type="number"></input>
  <input id="second" type ="number"></input><br><br>
<button onclick="adder()">Add</button>
<button onclick="subtracter()">Subtract</button>
<button onclick="multiplier()">Multiply</button>
<button onclick="divider()">Divide</button>
<h3><br/></h3>
<script type="text/javascript">
  adder = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput + +secondInput
    element = document.querySelector("h3")
    para = document.createElement("h3")
    contents = document.createTextNode(total)
    element.appendChild(contents)
  }
  subtracter = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput - +secondInput
    element = document.querySelector("h3")
    para = document.createElement("h3")
    contents = document.createTextNode(total)
    element.appendChild(contents)
  }
  multiplier = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput * +secondInput
    element = document.querySelector("h3")
    para = document.createElement("h3")
    contents = document.createTextNode(total)
    element.appendChild(contents)
  }
  divider = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput / +secondInput
    element = document.querySelector("h3")
    para = document.createElement("h3")
    contents = document.createTextNode(total)
    element.appendChild(contents)
  }
</script>
</body>
</html>
