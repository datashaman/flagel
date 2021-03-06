requirejs.config({
    paths: {
        knockout: 'components/knockout/build/output/knockout-latest',
        cs: 'components/require-cs/cs',
        domReady: 'components/requirejs-domready/domReady',
        'coffee-script': 'components/require-cs/coffee-script',
        kickstart: 'vendor/kickstart/js/kickstart',
        template: 'components/knockout-require-templates/template',
        stringTemplateEngine: 'components/knockout-require-templates/stringTemplateEngine',
        text: 'components/text/text',
        sammy: 'components/sammy/lib/sammy'
    },
    shim: {
        kickstart: {
            deps: ['jquery']
        }
    }
});

require(['jquery', 'knockout', 'cs!models/view', 'cs!models/auth', 'domReady!', 'kickstart'], function($, ko, ViewModel, AuthModel, doc) {
    var viewModel = new ViewModel();
    ko.applyBindings(viewModel, document.getElementById('content'));
    ko.applyBindings(viewModel, document.getElementById('menu'));

    var authModel = new AuthModel();
    ko.applyBindings(authModel, document.getElementById('auth'));
});
