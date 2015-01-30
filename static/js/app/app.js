ymapsApp = angular.module('ymapsApp', ['ymaps', 'ngResource', 'caco.ClientPaginate', 'ngCookies', 'checklist-model'])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }).run(function ($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    });
