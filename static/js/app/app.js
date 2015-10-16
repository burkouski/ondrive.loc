ondriveApp = angular.module('ondriveApp', ['ymaps', 'ngResource', 'ngCookies', 'checklist-model','ngMask'])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }).run(function ($http, $cookies) {

        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    });
