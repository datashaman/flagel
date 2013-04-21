define ['jquery'], ($) ->
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
            adaptiveHeight: true
            touchEnabled: true
            pause: 8000
            autoControls: true
            controls: false
            autoStart: true
            auto: true
