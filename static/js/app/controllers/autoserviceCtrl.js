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
                //console.log(data.objects)
                $scope.objects = data.objects
                for (var i = 0; i < $scope.objects.length; i++) {
                    var curObject = $scope.objects[i];
                        curObject['work_list'] = {};
                    console.log(curObject['body_repair__work'])
                    for (var j = 0; j < list.length; j++) {
                        curObject['work_list']= angular.extend({}, curObject['work_list'], curObject[list[j]])
                    }

                    curObject['work_list'] = angular.extend({}, curObject['work_list'], curObject['body_repair__work'])
                    console.log(curObject)
                }
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
        angular.forEach($scope.options, function (val, key) {
            if (val == false) {
                delete $scope.options[key];
            }
        })
        for (var i = 0; i < $scope.objects.length; i++) {
            selected = true
            var curObject = $scope.objects[i];
            //console.log($scope.options)
            angular.forEach($scope.options, function (val, key) {
                //console.log(val, ids.workTypes[key])
                if (val != curObject.work_list[key]) {
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