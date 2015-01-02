ymapsApp.controller('mainmapCtrl', ['$scope', '$http', function ($scope, $http) {


    $http({method: 'JSONP',
        params: {'callback': 'JSON_CALLBACK'},
        url: '/api/v1/autoserviceTop/?format=jsonp'}).success(function (data) {
            $scope.geoObjects = data.objects
            console.log($scope.geoObjects)

    }).error(function (err) {
        console.log(err);
    });


    console.log($scope.geoObjects)

}]);
