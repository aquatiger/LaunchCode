<html>
    <button onclick='incrementer(); sizer()' id='count' value=0 />0</button>
    <p id='test'>a</p>
    <script>
      clicks = 0
        incrementer = function () {
          clicks += 1
          click = document.querySelector("#count").textContent = clicks;
          click.innerHTML = document.getElementById("count").value = document.getElementById('test');
    }
        sizer = function changeFontSize() {
    div = document.getElementById("test");
    currentFont = div.style.fontSize.replace("pt", "");

    div.style.fontSize = parseInt(currentFont) + parseInt(clicks) + "pt";
}
</script>
</html>