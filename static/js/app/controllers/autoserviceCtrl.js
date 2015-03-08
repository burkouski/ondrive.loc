ymapsApp.controller('autoserviceCtrl', ['$scope', 'services', function ($scope, services) {

    //$scope.apiUrl = "/autoservices/";
    $scope.preloader = false;
    $scope.filter = {};
    $scope.gridView = false



    //$scope.isLoading = true;
    $scope.loadRemoteData = function (apiUrl, data) {

        services.list(apiUrl, data, function (services) {
                //alert(true)
                $scope.services = services.info;
                $scope.meta = services.meta
                //console.log($scope.services)
                $scope.preloader = true
            },
            function () {
                alert('wrong')
            });
    };

    $scope.init = function(url) {
        $scope.apiUrl = url;
        $scope.loadRemoteData($scope.apiUrl, $scope.filter);
    }


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

    // function to change service view
    $scope.changeView = function (view) {
        $scope.gridView = view; // path not hash
        console.log($scope.view)
    }

    // function to convert into star
    $scope.starsInit = function (rating) {
        var rating = rating,
            positiveStar = ~~rating,
            halfStar = 0,
            negativeStar,
            fractional = rating - positiveStar;
        if (fractional > 0.25 && fractional < 0.85) {
            halfStar = 1;
        }

        else if (fractional > 0.85) {
            positiveStar += 1;
        }
        else {
            halfStar = 0;
        }
        negativeStar = 5 - positiveStar - halfStar;
        return {
            positiveStar: _getArray(positiveStar),
            halfStar: _getArray(halfStar),
            negativeStar: _getArray(negativeStar)
        }
    };

    _getArray = function (n) {
        return new Array(n);
    };
}]);