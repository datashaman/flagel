<!DOCTYPE html>
<html>

<head>
    <title>{{ title or 'No title' }}</title>
    <link rel="stylesheet" type="text/css" href="/styles/style.css" />
</head>

<body>
    <div class="grid">
      <div id="header">
        <div id="logo" class="col_8">Logo</div>
        <div id="panel" class="col_4">Panel</div>
      </div>

      <div id="content">
        %include
      </div>

      <div id="footer" class="col_12">
        Footer
      </div>
    </div>
    <script data-main="main" src="/components/requirejs/require.js"></script>
</body>

</html>
