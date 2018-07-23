<html>
    <button style='font-size:12px;' onclick='incrementer(); sizer()' id='count' value=0 />0</button>
    <p id='test' style='font-size:12px;'>a</p>
    <script>
      var clicks = 0
      incrementer = function () {
          clicks += 1
          click = document.querySelector("#count").textContent = clicks;
          click.innerHTML = document.getElementById("count").value = document.getElementById('test');
      }
      var sizer = function changeFontSize() {
          var div = document.getElementById("test");
          var btn = document.getElementById("count");
          var newSize = parseInt(div.style.fontSize.replace("pt", "")) + parseInt(clicks);
          div.style.fontSize = newSize + "pt";
          btn.style.fontSize = newSize + "pt";
      }
    </script>
</html>
