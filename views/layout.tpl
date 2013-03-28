<!DOCTYPE html>
<html>
<head>
    <title>{{ title or 'No title' }}</title>

    <link rel="stylesheet" type="text/css" href="/plugins/select2/select2.css" />
    <link rel="stylesheet" type="text/css" href="/styles/style.css" />
    <link rel="stylesheet" type="text/css" href="/plugins/kickstart/css/kickstart.css" />

    <script type="text/javascript" src="/scripts/jquery-1.9.1.js"></script>
    <script type="text/javascript" src="/scripts/jquery-migrate-1.1.1.js"></script>
    <script type="text/javascript" src="/plugins/select2/select2.js"></script>
    <script type="text/javascript" src="/plugins/kickstart/js/kickstart.js"></script>
    <script type="text/javascript">
    jQuery(document).ready(function($) {
        config = {
          width: '100%',
          ajax: {
            dataType: 'json',
            url: '/ajax',
            data: function(term, page) {
              return {
                q: term,
                per: 10,
                page: page
              }
            },
            results: function(data, page) {
              return {
                results: data.results,
                more: data.more
              }
            }
          }
        };

        $('select.local').select2({ width: '100%' });

        $('input.ajax').select2(config);

        config.multiple = true;
        $('input.ajax-multiple').select2(config);
    });
    </script>
</head>
<body>
    %include
</body>
</html>
