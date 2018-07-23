//can only get the total to "print" in the alert, not console.log

<html>
  <body>
  <input id="first" type="number"></input>
  <input id="second" type ="number"></input><br><br>
<button onclick="adder()">Add</button>
<button onclick="subtracter()">Subtract</button>
<button onclick="multiplier()">Multiply</button>
<button onclick="divider()">Divide</button>
</body>
<script>
  adder = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput + +secondInput
    alert(total)
  }
  subtracter = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput - +secondInput
    alert(total)
  }
  multiplier = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput * +secondInput
    alert(total)
  }
  divider = function() {
    firstInput = document.getElementById("first").value
    secondInput = document.getElementById("second").value
    total = +firstInput / +secondInput
    alert(total)
  }
</script>

</html>
