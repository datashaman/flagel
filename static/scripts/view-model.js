define(['knockout-2.2.1', 'knockout-select2'], function(ko) {
    return function ViewModel(options) {
        var that = this;

        this.options = options;
        this.short_point = ko.observable(5);
        this.medium_point = ko.observable(9);
        this.short_options = ko.computed(function() { return that.options.slice(0, that.short_point()); });
        this.medium_options = ko.computed(function() { return that.options.slice(0, that.medium_point()); });

        this.ajax = {
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
        };
    };
});
