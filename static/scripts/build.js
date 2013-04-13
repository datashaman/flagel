({
    appDir: "../",
    baseUrl: "scripts/",
    dir: "../../static-build",

    optimize: "uglify2",

    paths: {
        "jquery": "empty:"
    },

    modules: [
        //Optimize the application files. jQuery is not 
        //included since it is already in require-jquery.js
        {
            name: "main",
        }
    ]
})
