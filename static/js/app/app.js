ymapsApp =angular.module('ymapsApp', ['ymaps', 'ngResource', 'caco.ClientPaginate', 'ngCookies']).run(function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});
