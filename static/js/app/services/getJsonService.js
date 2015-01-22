ymapsApp.service('getJsonService',['$http','$resource', function ($http, $resource) {

this.square = function(url) { return $resource(
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
                ); };


}])
