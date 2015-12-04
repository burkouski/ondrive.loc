(function () {
    'use strict';

    angular.module('ondriveApp.carService')
        .service('CarServiceSrv', ['$resource', function ($resource) {
            var getService = getService;
            var setMapIcon = setMapIcon;
            var getFilter = getFilter;

            return {
                getService: getService,
                setMapIcon: setMapIcon,
                getFilter: getFilter,
            };

            function getService(apiPath) {
                return $resource(apiPath, {}, {query: {isArray: false}})
            };

            function setMapIcon(apiPath) {
                if (apiPath === 'autoservice') {
                    return 'as-ico.png';
                }
                else if (apiPath === 'carwash') {
                    return 'cw-ico.png';
                }
                else if (apiPath === 'tireservice') {
                    return 'ts-ico.png';
                }
            }

            function getFilter(apiPath) {
                if (apiPath === 'autoservice') {
                    return 'asFilter';
                }
                else if (apiPath === 'carwash') {
                    return 'cwFilter'
                }
                else if (apiPath === 'tireservice') {
                    return 'tsFilter'
                }
            }
        }])
        .factory('services', ['$resource', function ($resource) {
            return {
                getServices: function (apiUrl) {
                    return $resource(apiUrl, {}, {query: {isArray: false}})
                }
            };
        }])
        .factory('Request', ['$http', function ($http) {

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
    //    .factory('services', ['$resource', function ($resource) {
    //        return {
    //            getServices: function (apiUrl) {
    //                return $resource(apiUrl, {}, {query: {isArray: false}})
    //            }
    //        };
    //    }]);
    //
    //angular.module('ondriveApp').factory('Request', ['$http', function ($http) {
    //
    //    return {
    //        sendRequest: function (url, data, callback, error) {
    //            $http({
    //                method: 'POST',
    //                data: JSON.stringify(data),
    //                url: url,
    //                responseType: 'json'
    //            }).success(callback).error(error);
    //        }
    //    };
    //}]);
    //
    //angular.module('ondriveApp').factory('Review', function ($resource) {
    //    return $resource('/reviews/api/createreview/'); // Note the full endpoint address
    //});

})();