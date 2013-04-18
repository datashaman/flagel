({
    mainConfigFile: "./app/static/main.js",
    appDir: "./app/static/",
    dir: "./static/",
    baseUrl: "./",
    skipDirOptimize: true,
    optimize: "uglify2",
    optimizeCss: "standard.keepComments",
    stubModules: ["cs"],
    modules: [
        {
            name: "main",
            exclude: ["coffee-script"]
        },
        {
            name: 'components/requirejs/require',
        }
    ]
})
