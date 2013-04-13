require(['jquery', 'knockout-2.2.1', 'cs!view-model', 'domReady!'], function($, ko, ViewModel) {
    $.ajax({
        url: '/ajax',
        dataType: 'json',
        success: function(data) {
            ko.applyBindings(new ViewModel(data.results));
        }
    });
});
