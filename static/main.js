requirejs.config({
    paths: {
        knockout: 'components/knockout/build/output/knockout-latest',
        cs: 'components/require-cs/cs',
        select2: 'components/select2/select2',
        jquery: 'components/jquery/jquery',
        domReady: 'components/requirejs-domready/domReady',
        'coffee-script': 'components/require-cs/coffee-script'
    }
});

require(['jquery', 'knockout', 'cs!scripts/view-model', 'domReady!'], function($, ko, ViewModel) {
    $.ajax({
        url: '/ajax',
        dataType: 'json',
        success: function(data) {
            ko.applyBindings(new ViewModel(data.results));
        }
    });
});
