({
    appDir: "../",
    baseUrl: "scripts/",
    dir: "../../static-build",

    optimize: "uglify2",
    uglify2: {
        output: {
            beautify: false
        }
    },

    stubModules: ['cs'],

    mainConfigFile: 'main.js',
    skipDirOptimize: true,

    modules: [
        //Optimize the application files. jQuery is not 
        //included since it is already in require-jquery.js
        {
            name: "main",
            exclude: ['coffee-script']
        }
    ]
})
