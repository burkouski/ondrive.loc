ondriveApp.factory('services', ['$resource', function ($resource) {
    return {
        getServices: function (apiUrl) {
            return $resource(apiUrl, {}, {query:{isArray:false}})
        }
    };
}]);

ondriveApp.factory('Request', ['$http', function ($http) {

    return {
        sendRequest: function (url, data, callback, error) {
            $http({
                method: 'POST',
                data: JSON.stringify(data),
                url: url,
                responseType: 'json'
            }).success(callback).error(error);
        }
    };
}]);

ondriveApp.factory('Review', function($resource) {
  return $resource('/reviews/api/createreview/'); // Note the full endpoint address
});

