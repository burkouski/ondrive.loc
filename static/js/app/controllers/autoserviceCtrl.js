ymapsApp.controller('autoserviceCtrl', ['$scope', 'services', function ($scope, services) {

    var apiUrl = "/autoservices/";
     $scope.preloader = false;
    $scope.objects = []
    $scope.filter = {}
    data = $scope.filter

    loadRemoteData(apiUrl, data);
    //$scope.isLoading = true;
    function loadRemoteData(apiUrl, data) {

        services.list(apiUrl, data, function (services) {
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

    $scope.$watchCollection('filter.electrician_work', function () {
        $scope.preloader  = false
        data = $scope.filter
        loadRemoteData(apiUrl, data);

    }, true)
    $scope.$watchCollection('filter.fuel_system_repair_work', function () {
        $scope.preloader  = false
        console.log($scope.filter)
        data = $scope.filter
        loadRemoteData(apiUrl, data);


    }, true)


}]);