ondriveApp.controller('serviceCtrl', ['$scope', '$cookieStore', 'services', function ($scope, $cookieStore, services) {

    $scope.init = function (api) {
        if (api) {
            $scope.api = api;
            setMapIcon(api)
        }
        else {
            $scope.api = 'autoservice';
            setMapIcon($scope.api);
        }

        $scope.pageSize = 6;
        $scope.page = 1;
        $scope.mapObjects = {};
        $scope.loadData = loadData;
        $scope.loadMap = loadMap;
        $scope.resetPage = resetPage;
        $scope.setPage = setPage;
        $scope.clearFilter = clearFilter;
        loadData();
        loadMap();

    };

    $scope.$watch("pageSize", function (newValue, oldValue) {
        if (newValue !== oldValue) {
            resetPage();
            loadData();
        }

    });

    $scope.$watch("api", function (newValue, oldValue) {
        if (newValue !== oldValue) {
            setMapIcon(newValue);
            loadData();
            loadMap();
        }

    });

    $scope.$watch('page', function (newValue, oldValue) {
        if (newValue !== oldValue) {
            loadData();
        }

    });

    $scope.$watchGroup(['asFilter'], function (newVal, oldVal) {

    }, true);

    function loadData() {
        var apiUrl = getApiUrl($scope.api);
        var filter = getFilter($scope.api);
        var query = {
            pageSize: $scope.pageSize,
            page: $scope.page,
            filter: filter
        };

        var service = services.getServices(apiUrl);

        $scope.services = service.query(query);

        $scope.services.$promise.then(function (result) {
            $scope.services.objects = result.results;
            $scope.services.quantity = result.count;
        });

        //var aTag = $("#service-anchor");
        //$('html,body').animate({scrollTop: aTag.offset().top - 100}, 'slow');
    }

    function loadMap() {
        var apiUrl = getApiUrl($scope.api),
            filter = getFilter($scope.api),
            query = {
                filter: filter
            },
            map = services.getServices(apiUrl);

        $scope.map = map.query(query);
        $scope.map.$promise.then(function (result) {
            $scope.map = result.results;
        });
    }

    function setMapIcon(api) {
        if (api === 'autoservice') {
            $scope.mapIcon = 'as-ico.png';
        }
        else if (api === 'carwash') {
            $scope.mapIcon = 'cw-ico.png';
        }
        else if (api === 'tireservice') {
            $scope.mapIcon = 'ts-ico.png';
        }
    }

    function getApiUrl(api) {
        if (api === 'autoservice') {
            return '/api/autoservice'
        }
        else if (api === 'carwash') {
            return '/api/carwash'
        }
        else if (api === 'tireservice') {
            return '/api/tireservice'
        }
    }

    function getFilter(api) {
        var filter = {};
        if (api === 'autoservice') {
            return filter = $scope.asFilter;
        }
        else if (api === 'carwash') {
            return filter = $scope.cwFilter
        }
        else if (api === 'tireservice') {
            return filter = $scope.tsFilter
        }
    }

    function setPage(page) {
        $scope.page = page
    }

    function resetPage() {
        $scope.page = 1
    }

    function clearFilter(filterName) {
        $scope[filterName] = {}
    }

//    init = function (serviceName) {
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
    $scope.activeTabs = [];
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
        //setCookie()
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
