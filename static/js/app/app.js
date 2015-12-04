(function() {
    'use strict';

    angular.module('ondriveApp.carService', []);

    angular.module('ondriveApp', [
        'ymaps',
        'ngResource',
        'ngCookies',
        'checklist-model',
        'ngMask',
        'ui.bootstrap',
        'ondriveApp.carService'
    ])
        .config(appConfig)
        .run(appRun);

    function appConfig($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }

    function appRun($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = CSRF_TOKEN;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    }

})();
