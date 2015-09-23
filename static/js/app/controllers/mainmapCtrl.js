ymapsApp.controller('mainmapCtrl', ['$scope', '$cookieStore', '$resource', function ($scope, $cookieStore, $resource) {
 var Regions = $resource('/api/autoservices/');

$scope.services = Regions.query({specialization_work :[20,14]});
$scope.services.$promise.then(function (result) {
    $scope.services = result;
});
    console.log($scope.services);
//    init = function () {
//        $scope.preloader = false;
//        $scope.gridView = false;
//
//        var apiUrlCook = $cookieStore.get('apiUrl'),
//            asFilterCook = $cookieStore.get('asFilter'),
//            cwFilterCook = $cookieStore.get('cwFilter'),
//            tsFilterCook = $cookieStore.get('tsFilter'),
//            mapIconCook = $cookieStore.get('mapIcon'),
//            activeTabsCook = $cookieStore.get('activeTabs');
//
//        $scope.apiUrl = (apiUrlCook) ? apiUrlCook : "/autoservices/";
//        $scope.mapIcon = (mapIconCook) ? mapIconCook : "as-ico.png";
//        $scope.asFilter = (asFilterCook) ? asFilterCook : {};
//        $scope.cwFilter = (cwFilterCook) ? cwFilterCook : {};
//        $scope.tsFilter = (tsFilterCook) ? tsFilterCook : {};
//        $scope.activeTabs = (activeTabsCook) ? activeTabsCook : [];
//        $scope.quantity = 6
//
//        $scope.filterName = ($scope.apiUrl == "/autoservices/") ? 'asFilter' :
//            ($scope.apiUrl == "/carwash/") ? 'cwFilter' : ($scope.apiUrl == "/tireservice/") ? 'tsFilter': {};
//
//
//        $scope.quantity = 6;
//        $scope.curPage = 1;
//        $scope[$scope.filterName].meta = {
//            quantity: $scope.quantity,
//            page: $scope.curPage-1
//        };
//        $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
//    }
//
//    setCookie = function () {
////        now = new Date();
////        now = now.setMinutes(now.getMinutes() + 1)
////        console.log(now);
//        $cookieStore.put('apiUrl', $scope.apiUrl),
//            $cookieStore.put('asFilter', $scope.asFilter),
//            $cookieStore.put('cwFilter', $scope.cwFilter),
//            $cookieStore.put('tsFilter', $scope.cwFilter),
//            $cookieStore.put('activeTabs', $scope.activeTabs);
//    }
//
////    //Функция загрузки данных
//   $scope.loadRemoteData = function (apiUrl, data) {
//        $scope.preloader = false;
//        console.log(apiUrl);
//        services.list(apiUrl, data, function (services) {
//                //console.log(services)
//                $scope.services = services.objects.info;
//                $scope.meta = services.objects.meta;
//                $scope.mapObjects = services.mapObjects;
//                $scope.preloader = true;
//                setCookie();
//                resetPagination($scope.meta, $scope.quantity);
//                console.log($scope.pagination);
//            },
//            function () {
//                alert('wrong');
//            });
//    };
//
//    //Функция изменения сервиса (очищает фильтры при переключении)
//    $scope.changeService = function (apiUrl, filterName, mapIcon) {
//        $scope.mapIcon = mapIcon;
//        resetPage();
//    }
//
//    //Функция проверки открытого таба в фильтре
    $scope.isOpenTab = function (tab) {
        //console.log(true)
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
//
//    // Функция изменения отображения сервисов
//    $scope.changeView = function (boll) {
//        $scope.gridView = boll;
////        if ($scope.gridView) {
////            var heights = $(".product").map(function () {
////                    console.log($(this).outerHeight());
////                    return $(this).outerHeight();
////
////                }).get(),
////
////                maxHeight = Math.max.apply(null, heights);
////            $(".product-col").height(maxHeight)
////        }
////        console.log($scope.view)
//    }
//
//
//    //Преобразования рейтинга в звёзды
//    $scope.starsInit = function (rating) {
//        var rating = rating,
//            positiveStar = ~~rating,
//            halfStar = 0,
//            negativeStar,
//            fractional = rating - positiveStar;
//        if (fractional > 0.25 && fractional < 0.85) {
//            halfStar = 1;
//        }
//
//        else if (fractional > 0.85) {
//            positiveStar += 1;
//        }
//        else {
//            halfStar = 0;
//        }
//        negativeStar = 5 - positiveStar - halfStar;
//        return {
//            positiveStar: _getArray(positiveStar),
//            halfStar: _getArray(halfStar),
//            negativeStar: _getArray(negativeStar)
//        }
//    };
//
//
//    $scope.changeFilter = function() {
//        resetPage()
//    };
//
//    $scope.clearFilter = function (filterName) {
//        angular.forEach($scope[filterName], function (value, key) {
//            $scope[filterName][key] = [];
//        });
//        $scope.loadRemoteData($scope.apiUrl, $scope[filterName]);
//
//    };
//
//    $scope.changeQuantity = function() {
//        $scope[$scope.filterName].meta.quantity = $scope.quantity;
//        resetPage()
//    };
//
//    $scope.changePage = function(curPage) {
//            $scope.curPage = curPage+1;
//            $scope[$scope.filterName].meta.page = curPage;
//            $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
//        };
//
//   init();
//
//    resetPagination = function(objQuantity, displayQuantity) {
//
//        $scope.pagination = _getArray(Math.ceil(objQuantity/displayQuantity))
//        console.log($scope.pagination)
//    };
//
//    _getArray = function (n) {
//        return new Array(n);
//    };
//
//    function resetPage() {
//        $scope.curPage = 1;
//       $scope[$scope.filterName].meta = {
//            quantity: $scope.quantity,
//            page: $scope.curPage-1
//        };
//        $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
//    }

}]);
