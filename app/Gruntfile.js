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
        copy: {
            css: {
                expand: true,
                cwd: 'css',
                dest: '../public/css',
                dot: true,
                src: '**/*'
            },
            img: {
                expand: true,
                cwd: 'img',
                dest: '../public/img',
                dot: true,
                src: '**/*'
            },
        },
        watch: {
            css: {
                files: 'sass/**/*.scss',
                tasks: ['sass', 'copy'],
                options: {
                    atBegin: true,
                },
            }
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
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('build', ['sass', 'copy']);
};