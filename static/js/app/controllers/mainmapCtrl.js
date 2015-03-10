ymapsApp.controller('mainmapCtrl', ['$scope','$cookieStore', 'services', function ($scope, $cookieStore, services) {

    init = function(){
        $scope.preloader = false;
        $scope.gridView = false;

        var apiUrlCook = $cookieStore.get('apiUrl'),
            asFilterCook = $cookieStore.get('asFilter'),
            cwFilterCook = $cookieStore.get('cwFilter'),
            activeTabsCook = $cookieStore.get('activeTabs');

        $scope.apiUrl = (apiUrlCook)? apiUrlCook : "/autoservices/";
        $scope.asFilter = (asFilterCook)? asFilterCook : {};
        $scope.cwFilter = (cwFilterCook)? cwFilterCook : {};
        $scope.activeTabs = (activeTabsCook)? activeTabsCook : [];

        var curFilter = ($scope.apiUrl == "/autoservices/")? $scope.asFilter :
                        ($scope.apiUrl == "/carwash/") ? $scope.cwFilter : {};

        $scope.loadRemoteData($scope.apiUrl, curFilter);
    }

    setCookie = function() {
         $cookieStore.put('apiUrl', $scope.apiUrl),
         $cookieStore.put('asFilter', $scope.asFilter),
         $cookieStore.put('cwFilter', $scope.cwFilter),
         $cookieStore.put('activeTabs', $scope.activeTabs);
    }

    //Функция загрузки данных
    $scope.loadRemoteData = function (apiUrl, data) {
        $scope.preloader = false;
        console.log(data);
        services.list(apiUrl, data, function (services) {
                //alert(true)
                $scope.services = services.info;
                $scope.meta = services.meta
                //console.log($scope.services)
                $scope.preloader = true
                setCookie()
            },
            function () {
                //console.log($scope.filter)
                alert('wrong')
            });
    };

    //Функция изменения сервиса (очищает фильтры при переключении)
    $scope.changeService = function(apiUrl, filter) {
        $scope.loadRemoteData(apiUrl, filter);
    }

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

    init();

    _getArray = function (n) {
        return new Array(n);
    };

}]);
