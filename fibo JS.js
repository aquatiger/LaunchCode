//This code does not work properly. It creates a new bullet on each click, but not the addition of the contents

<html>
    <body>
       <button onclick="addrow()">Next</button>
       <ul id="mytable"><li id=0>0</li><li id=1>1</li></ul>
      <script>
        addrow = function() {
             t = document.querySelector("#mytable");
             trow = document.createElement("li");
             contents = document.lastChild.innerHTML;
             console.log(contents);
             prevcon = document.getElementById(1).previousElementSibling.innerHTML;
             t.appendChild(trow);
             trow.appendChild(contents + prevcon);


        }
      </script>
    </body>
</html>
