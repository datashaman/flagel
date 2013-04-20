requirejs.config({
    paths: {
        knockout: 'components/knockout/build/output/knockout-latest',
        cs: 'components/require-cs/cs',
        jquery: 'components/jquery/jquery',
        domReady: 'components/requirejs-domready/domReady',
        'coffee-script': 'components/require-cs/coffee-script',
        kickstart: 'vendor/kickstart/js/kickstart'
    },
    shim: {
        kickstart: ['jquery']
    }
});

require(['jquery', 'knockout', 'domReady!', 'kickstart'], function($, ko, doc) {
});
