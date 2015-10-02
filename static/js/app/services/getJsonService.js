ondriveApp.service('getJsonService', ['$http', '$resource', function ($http, $resource) {

    this.square = function (url) {
        return $resource(
            url,
            {
                callback: "JSON_CALLBACK"
            },
            {
                getJson: {
                    method: "JSONP",
                    isArray: false
                }
            }
        );
    };


}])

ondriveApp.factory('services', ['$resource', function ($resource) {

    return {
        getServices: function (apiUrl) {
            return $resource(apiUrl, {}, {query:{isArray:false}})
        }
    };
}]);
