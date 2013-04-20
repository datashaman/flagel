({
    mainConfigFile: "../apps/flagel/static/main.js",
    appDir: "../apps/flagel/static/",
    dir: "../static/flagel/",
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
            name: 'require-jquery'
        }
    ],
    paths: {
        jquery: 'empty:'
    }
})
