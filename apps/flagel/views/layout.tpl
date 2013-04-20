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
</head>

<body>
<div id="root">
    <div id="top-bar">
        <div class="grid">
            <ul class="menu" data-bind="foreach: menu">
                <li data-bind="css: { right: $data[2], current: $data[0] == $root.current() }">
                    <a data-bind="attr: { href: $data[0] }, text: $data[1]"></a>
                </li>
            </ul>
        </div>
    </div>

    <div id="content" class="clearfix" data-bind="html: content">
    </div>

    <div id="root-footer"></div>
</div>

<div id="footer" class="center">
    Copyright, etc.
</div>

<script data-main="main" src="/require-jquery.js"></script>
</body>

</html>
