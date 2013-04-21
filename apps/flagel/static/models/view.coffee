define ['jquery', 'knockout', 'sammy', 'cs!scripts/activateSlider'], ($, ko, Sammy) ->
    () ->
        model = @

        @menu = [['',          'Home',      false]
                 ['#about',    'About',     false],
                 ['#contact',  'Contact',   true ]]

        @content = ko.observable()
        @current = ko.observable()

        @app = Sammy () ->
            @get '#home', (ctx) ->
                @redirect ''

            @get '#:page', (ctx) ->
                require ['template!./templates/' + @params.page + '.html'], (tpl) =>
                    model.content(tpl)
                    model.current('#' + @params.page)

            @get '', ->
                require ['template!./templates/home.html'], (tpl) =>
                    model.content(tpl)
                    model.current('')
                    $('.slideshow').activateSlider()

            return

        @app.run()
        return
