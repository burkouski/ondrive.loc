ymapsApp.service('getJsonService',['$http','$resource', function ($http, $resource) {

this.square = function() { return $resource(
                    "/api/v1/allAutoservice/?format=jsonp",
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
