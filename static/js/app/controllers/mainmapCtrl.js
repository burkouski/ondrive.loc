ymapsApp.controller('mainmapCtrl', ['$scope', 'services', function ($scope, services) {

$scope.apiUrl = "/api/topautoservices/";
    $scope.preloader = false;
    $scope.filter = {};
    $scope.gridView = false


    //$scope.isLoading = true;
    $scope.loadRemoteData = function(apiUrl) {

        services.list(apiUrl, '', function (services) {
                //alert(true)
                $scope.services = services;
                console.log($scope.services)
                $scope.filteredService = $scope.services
                $scope.preloader  = true
            },
            function () {
                alert('wrong')
            });


    };

    $scope.loadRemoteData($scope.apiUrl);

}]);
