

ondriveApp.factory('localStorage', ['$resource', function ($resource) {
    return {
        getItem: function (apiUrl) {
            return $resource(apiUrl, {}, {query:{isArray:false}})
        },
        setItem: function (apiUrl) {
            return $resource(apiUrl, {}, {query:{isArray:false}})
        }
    };
}]);
