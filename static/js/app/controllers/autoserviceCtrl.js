ymapsApp.controller('autoserviceCtrl', ['$scope', '$cookieStore', 'services', function ($scope, $cookieStore, services) {

    $scope.init = function (filterName, apiUrl) {
        $scope.preloader = false;
        $scope.gridView = false;
        $scope.filterName = filterName;
        $scope.apiUrl = apiUrl;
        var filterCook = $cookieStore.get($scope.filterName),
            activeTabsCook = $cookieStore.get('activeTabs');
        console.log($cookieStore.get($scope.filterName));

        $scope[$scope.filterName] = (filterCook) ? filterCook : {};
        $scope.activeTabs = (activeTabsCook) ? activeTabsCook : [];

        $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
    }

    setCookie = function () {
        $cookieStore.put($scope.filterName, $scope[$scope.filterName]);
        $cookieStore.put('activeTabs', $scope.activeTabs);

    }

    //Функция загрузки данных
    $scope.loadRemoteData = function (apiUrl, data) {
        $scope.preloader = false;
        console.log(data);
        services.list(apiUrl, data, function (services) {
                $scope.services = services.info;
                $scope.meta = services.meta
                $scope.preloader = true
                setCookie()
                console.log($scope.services)
            },
            function () {
                alert('wrong')
            });
    };

    //Функция проверки открытого таба в фильтре
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

    //Функция открытия таба в фильтре
    $scope.openTab = function (tab) {
        //check if tab is already open
        if ($scope.isOpenTab(tab)) {
            //if it is, remove it from the activeTabs array
            $scope.activeTabs.splice($scope.activeTabs.indexOf(tab), 1);
        } else {
            //if it's not, add it!
            $scope.activeTabs.push(tab);
        }
        setCookie()
    }

    // Функция изменения отображения сервисов
    $scope.changeView = function (view) {
        $scope.gridView = view; // path not hash
        console.log($scope.view)
    }

    //Преобразования рейтинга в звёзды
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

    $scope.clearFilter = function (filterName) {
        angular.forEach($scope[filterName], function (value, key) {
            $scope[filterName][key] = []
        });
        $scope.loadRemoteData($scope.apiUrl, $scope[filterName]);

    }

    _getArray = function (n) {
        return new Array(n);
    };

}]);
