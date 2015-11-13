ondriveApp = angular.module('ondriveApp', ['ymaps', 'ngResource', 'ngCookies', 'checklist-model','ngMask'])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }).run(function ($http, $cookies) {
        console.log(CSRF_TOKEN);
        $http.defaults.headers.post['X-CSRFToken'] = CSRF_TOKEN;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    });
