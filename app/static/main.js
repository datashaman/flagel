requirejs.config({
    paths: {
        knockout: 'components/knockout/build/output/knockout-latest',
        cs: 'components/require-cs/cs',
        jquery: 'components/jquery/jquery',
        domReady: 'components/requirejs-domready/domReady',
        'coffee-script': 'components/require-cs/coffee-script'
    }
});

require(['jquery', 'knockout', 'domReady!'], function($, ko, doc) {
});
