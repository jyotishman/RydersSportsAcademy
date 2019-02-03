module.exports = function(grunt) {
    var path = require('path');
    // Project configuration.
    grunt.initConfig({
        meta: {
            basePath: path.resolve('.'),
            cssSrcPath: 'src/css/',
            sassSrcPath: 'src/sass/',
            jsSrcPath: 'src/scripts',
            dashboardController: 'controllers/dashboard',
            endUserController: 'controllers/enduser',
            bowerSrcPath: 'bower_components'
        },
        
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'sass',
                    src: ['*.scss'],
                    dest: 'css',
                    ext: '.css'
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');

    

    


    // Default task(s).
    grunt.registerTask('build', ['sass']);
};