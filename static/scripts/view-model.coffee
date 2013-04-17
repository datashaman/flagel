define ['knockout', 'scripts/knockout-select2'], (ko) ->
    (options) =>
        @options = options
        @short_point = ko.observable(5)
        @medium_point = ko.observable(9)
        @short_options = ko.computed =>
            @options.slice 0, @short_point()
        @medium_options = ko.computed =>
            @options.slice 0, @medium_point()
        @ajax =
            dataType: 'json'
            url: '/ajax'
            data: (term, page) ->
                q: term
                per: 10
                page: page
            results: (data, page) ->
                results: data.results
                more: data.more
