ondriveApp.factory('services', ['$resource', function ($resource) {
    return {
        getServices: function (apiUrl) {
            return $resource(apiUrl, {}, {query:{isArray:false}})
        }
    };
}]);

ondriveApp.factory('services2', ['$http', function ($http) {

    return {
        list: function (url, data, callback, error) {
            $http({
                method: 'POST',
                data: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                },
                //dataType: 'json',
                url: url,
                responseType: 'json'
            }).success(callback).error(error);
        }
    };
}]);

