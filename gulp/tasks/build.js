var config      = require('../config');
var del         = require('del');
var gulp        = require('gulp');
var outputLogo  = require('../utils/outputLogo');

outputLogo();

gulp.task('build', ['coffee', 'sass', 'imageOptimize', 'third_party', 'browserify'], function(){
    global.isBuilding = false;

    // Delete lingering compiled coffeescript src
    del([config.src + 'js']);
});
