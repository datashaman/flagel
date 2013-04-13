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

            ko.applyBindings(new ViewModel());
        }
    });
});
