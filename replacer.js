<html>
<style>
</style>
<body>
        <h2><main>
		Hello</h2>
    </main>
    <input type="text" size="100">
    <button onclick="replacer()"/>Replace</button>
    <script type="text/javascript">
        var initial;
        replacer = function() {
        initial = document.querySelector('main');
        initial.innerHTML = document.querySelector(‘input’).value;
        }
    </script>
</body>
</html>
