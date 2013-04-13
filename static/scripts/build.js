({
    appDir: "../",
    baseUrl: "scripts/",
    dir: "../../static-build",

    optimize: "uglify2",

    stubModules: ['cs'],

    paths: {
        "jquery": "empty:"
    },

    modules: [
        //Optimize the application files. jQuery is not 
        //included since it is already in require-jquery.js
        {
            name: "main",
            exclude: ['coffee-script']
        }
    ]
})
