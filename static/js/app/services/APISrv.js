angular.module('ondriveApp')
    .service('APISrv', [function(){
        var prefix = '/api/v1/'
        var getAPIPath = function(path){
            return prefix+path
        }

        return {
            getAPIPath: getAPIPath
        }

    }]);

