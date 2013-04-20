<!DOCTYPE html>
<html>

<head>
<title>{{ title or 'No title' }}</title>
<link href="/styles/screen.css" media="screen, projection" rel="stylesheet" type="text/css" />
<link href="/styles/print.css" media="print" rel="stylesheet" type="text/css" />
<!--[if IE]>
    <link href="/styles/ie.css" media="screen, projection" rel="stylesheet" type="text/css" />
<![endif]-->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script data-main="main" src="/components/requirejs/require.js"></script>
</head>

<body>
<div id="root">
    <div id="top-bar">
        <div class="grid">
            <ul class="menu">
                <li><a href="/">Home</a></li>
                <li class="right"><a href="">Profile</a></li>
                <li class="right"><a href="/about">About</a></li>
            </ul>
        </div>
    </div>

    <div id="content" class="clearfix">
        %include
    </div>

    <div id="root-footer"></div>
</div>

<div id="footer" class="center">
    Footer
</div>

</body>

</html>
