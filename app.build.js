({
    mainConfigFile: "./static/main.js",
    appDir: "./static/",
    dir: "./build/static/",
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
