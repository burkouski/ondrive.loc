ymapsApp.controller('autoserviceCtrl', ['$scope', 'getJsonService', function ($scope, getJsonService) {

    $scope.isLoading = false;
    $scope.objects = []
    loadRemoteData();

    function loadRemoteData() {

        $scope.isLoading = true;

        getJsonService.square().getJson().$promise.then(
            function (data) {
                console.log(data.objects)
                $scope.objects = data.objects

                $scope.filteredService = $scope.objects
                //console.log($scope.isLoading)

            },
            function (error) {

                // If something goes wrong with a JSONP request in AngularJS,
                // the status code is always reported as a "0". As such, it's
                // a bit of black-box, programmatically speaking.
                alert("Something went wrong!");

            }
        )

    };


    $scope.options = {}

    $scope.$watch('options', function () {
        $scope.filteredService = [],
            selected = true;
        angular.forEach($scope.options, function (val, key) {
            if (val == false) {
                delete $scope.options[key];
            }
        })
        for (var i = 0; i < $scope.objects.length; i++) {
            selected = true
            curObject = $scope.objects[i];
            console.log($scope.options)
            angular.forEach($scope.options, function (val, key) {
                //console.log(val, ids.workTypes[key])
                if (val != curObject.work_types[key]) {
                    selected = false
                }

            })
            if (selected) {
                $scope.filteredService.push(curObject)
            }
        }
        //console.log($scope.filteredService)
    }, true)

}]);