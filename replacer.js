<html>
<style>
    @keyframes spinner{
     from {
        transform: rotate(0deg);
    } to {
        transform: rotate(360deg);
    }
}
    main {
        animation: spinner;
        width: 100px;
        height: 100px;
        animation-duration: 4s;
        animation-iteration-count: infinite;
        animation-direction: alternate;
      }
    }
</style>
<body>
    <h2><main>Hello</main></h2>
    <input type="text" size="100">
    <button onclick="replacer()"/>Replace</button>
    <script type="text/javascript">
        var initial;
        replacer = function() {
        initial = document.querySelector('main');
        initial.innerHTML = document.querySelector('input').value;
       }
    </script>
</body>
</html>
