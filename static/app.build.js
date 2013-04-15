({
    mainConfigFile: "main.js",

    appDir: "../",
    dir: "../static-build",
    skipDirOptimize: true,

    optimize: "uglify2",
    optimizeCss: "standard.keepComments",

    stubModules: ["cs"],
    modules: [
        {
            name: "main",
            exclude: ["coffee-script"]
        }
    ]
})
