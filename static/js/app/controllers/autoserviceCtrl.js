ymapsApp.controller('autoserviceCtrl', ['$scope', 'services', function ($scope, services) {

    $scope.apiUrl = "/autoservices/";
    $scope.preloader = false;
    $scope.filter = {};
    $scope.gridView = false


    //$scope.isLoading = true;
    $scope.loadRemoteData = function(apiUrl, data) {

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

    $scope.loadRemoteData($scope.apiUrl, $scope.filter);



    //initiate an array to hold all active tabs
    $scope.activeTabs = [];

    //check if the tab is active
    $scope.isOpenTab = function (tab) {
        //check if this tab is already in the activeTabs array
        if ($scope.activeTabs.indexOf(tab) > -1) {
            //if so, return true
            return true;
        } else {
            //if not, return false
            return false;
        }
    }

    //function to 'open' a tab
    $scope.openTab = function (tab) {
        //check if tab is already open
        if ($scope.isOpenTab(tab)) {
            //if it is, remove it from the activeTabs array
            $scope.activeTabs.splice($scope.activeTabs.indexOf(tab), 1);
        } else {
            //if it's not, add it!
            $scope.activeTabs.push(tab);
        }
    }

$scope.changeView = function(view){
            $scope.gridView = view; // path not hash
    console.log($scope.view)
        }
}]);