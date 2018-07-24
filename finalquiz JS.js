<html>
<style>
body {
background-color: lightblue;
}
h1 {
color: red;
}
</style>
<body>
<h1>So Long 130</h1>
    <button onclick="finalquiz();">Click Me</button>
    <script type="text/javascript">
    finalquiz = function() {
    t = document.querySelector("h1")
    h1new = document.createElement("h1")
    newone = document.createTextNode("So Long 130")
    h1new.appendChild(newone)
    t.appendChild(h1new)
    }
    </script>
</body>
</html>
