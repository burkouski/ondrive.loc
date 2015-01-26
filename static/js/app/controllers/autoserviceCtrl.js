ymapsApp.controller('autoserviceCtrl', ['$scope', 'getJsonService', function ($scope, getJsonService) {

    $scope.isLoading = false;
    $scope.objects = []
    var apiUrl = "/api/v1/autoservices/?format=jsonp",
        workList = ['electrician_work','body_repair__work']
    loadRemoteData(apiUrl, workList);

    function loadRemoteData(url, list) {

        $scope.isLoading = true;

        getJsonService.square(url).getJson().$promise.then(
            function (data) {
                console.log(data.objects)
                $scope.objects = data.objects

                $scope.filteredService = $scope.objects

            },
            function (error) {

                alert("Something went wrong!");

            }
        )

    };


    $scope.options = {}

    $scope.$watch('options', function () {
        $scope.filteredService = [],
            selected = true;
        angular.forEach($scope.options, function (key, val) {
            if (val == false) {
                delete $scope.options[key];
            }
        })
        //console.log($scope.options)
        for (var i = 0; i < $scope.objects.length; i++) {
            selected = true
            var curObject = $scope.objects[i];
            //console.log($scope.options)
            angular.forEach($scope.options, function (val, key) {
                if (val) {
                    console.log(key )
                    for (var j= 0; j < curObject.work_list.length; j++) {

                        if (curObject.work_list[j].work_name !== key) {selected = false;}
                        else {
                            selected = true
                        }
                    }


                }

            })
            if (selected) {
                $scope.filteredService.push(curObject)
            }
        }
        //console.log($scope.filteredService)
    }, true)

}]);