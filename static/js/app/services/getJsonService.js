ymapsApp.service('getJsonService', ['$http', '$resource', function ($http, $resource) {

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

ymapsApp.factory('services', ['$http', function ($http) {

    return {
        list: function (url, data, callback, error) {
            $http({
                method: 'POST',
                data: $.param(data),
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
