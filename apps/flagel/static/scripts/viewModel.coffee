define ['jquery', 'knockout', 'sammy'], ($, ko, Sammy) ->
    $.fn.activateSlider = () ->
        @bxSlider
            mode: 'horizontal' # 'horizontal', 'vertical', 'fade'
            video: true
            useCSS: true
            pager: true
            speed: 2000  #transition time
            startSlide: 0
            infiniteLoop: true
            captions: true
            adaptiveHeight: false
            touchEnabled: true
            pause: 8000
            autoControls: true
            controls: false
            autoStart: true
            auto: true

    () ->
        model = @

        @menu = [['', 'Home', false]
                 ['#about', 'About', false],
                 ['#contact', 'Contact', true]]

        @currentPage = ko.observable('')

        @openPage = (page) =>
            location.hash = page

        @app = Sammy '#content', () ->
            @get '#home', (ctx) ->
                @redirect ''

            @get '#:page', (ctx) ->
                require ['template!./templates/' + @params.page + '.html'], (tpl) =>
                    @swap tpl, () =>
                        model.currentPage('#' + @params.page)

            @get '', ->
                require ['template!./templates/home.html'], (tpl) =>
                    @swap tpl, () =>
                        model.currentPage('')
                        $('.slideshow').activateSlider()

            return

        @app.run()
        return
