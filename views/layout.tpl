<!DOCTYPE html>
<html>

<head>
    <title>{{ title or 'No title' }}</title>
    <link rel="stylesheet" type="text/css" href="/plugins/select2/select2.css" />
    <link rel="stylesheet" type="text/css" href="/plugins/kickstart/css/kickstart.css" />
    <link rel="stylesheet" type="text/css" href="/styles/style.css" />
</head>

<body>
    %include

    <script type="text/javascript" src="/scripts/jquery-1.9.1.js"></script>
    <script type="text/javascript" src="/scripts/jquery-migrate-1.1.1.js"></script>

    <script type="text/javascript" src="/scripts/jquery.tools.min.js"></script>
    <script type="text/javascript" src="/plugins/select2/select2.js"></script>
    <script type="text/javascript" src="/plugins/kickstart/js/kickstart.js"></script>
    <script type='text/javascript' src='/scripts/knockout-2.2.1.js'></script>

    <script type="text/javascript">
    jQuery(document).ready(function($) {
      ko.bindingHandlers.select2 = {
        init: function(element, valueAccessor, allBindingsAccessor) {
          var obj = valueAccessor(),
              allBindings = allBindingsAccessor(),
              lookupKey = allBindings.lookupKey;
          $(element).select2(obj);
          if (lookupKey) {
            var value = ko.utils.unwrapObservable(allBindings.value);
            $(element).select2('data', ko.utils.arrayFirst(obj.data.results, function(item) {
              return item[lookupKey] === value;
            }));
          }

          ko.utils.domNodeDisposal.addDisposeCallback(element, function() {
            $(element).select2('destroy');
          });
        },
        update: function(element) {
          $(element).trigger('change');
        }
      };

      var config = {
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

      $.ajax({
        url: '/ajax',
        dataType: 'json',
        success: function(data) {
          var ViewModel = function() {
            var that = this;

            this.numbers = data.results;
            this.short_point = ko.observable(5);
            this.medium_point = ko.observable(9);
            this.short_options = ko.computed(function() { return that.numbers.slice(0, that.short_point()); });
            this.medium_options = ko.computed(function() { return that.numbers.slice(0, that.medium_point()); });
          };

          ko.applyBindings(new ViewModel());

          /*
          $(':date').dateinput();
          $(':range').rangeinput();
          */

          $('select.local').select2({ width: '100%' });
          $('input.ajax').select2(config);
          config.multiple = true;
          $('input.ajax-multiple').select2(config);
        }
      });
    });
    </script>
</body>

</html>
