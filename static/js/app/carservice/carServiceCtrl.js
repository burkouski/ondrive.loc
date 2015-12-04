(function () {
    'use strict';

    angular.module('ondriveApp.carService')
        .controller('carServiceCtrl', ['$scope', '$cookieStore', 'services', 'CarServiceSrv', 'APISrv', function ($scope, $cookieStore, services, CarServiceSrv, APISrv) {
            var carServiceVm = this;

            carServiceVm.init = function (api) {

                if (api) {
                    carServiceVm.api = api;
                }
                else {
                    if ($cookieStore.get('carServiceVm.api')) {
                        carServiceVm.api = $cookieStore.get('carServiceVm.api')
                    }
                    else {
                        carServiceVm.api = 'autoservice';
                    }

                }

                carServiceVm.mapIcon = CarServiceSrv.setMapIcon(carServiceVm.api);
                carServiceVm.pageSize = 6;
                carServiceVm.page = 1;
                carServiceVm.mapObjects = {};
                carServiceVm.loadData = loadData;
                carServiceVm.loadMap = loadMap;
                carServiceVm.resetPage = resetPage;
                carServiceVm.setPage = setPage;
                carServiceVm.clearFilter = clearFilter;

                loadData();
                loadMap();
            };

            $scope.$watch("carServiceVm.pageSize", function (newValue, oldValue) {
                if (newValue !== oldValue) {
                    resetPage();
                    loadData();
                }

            });

            $scope.$watch("carServiceVm.api", function (newValue, oldValue) {
                if (newValue !== oldValue) {
                    carServiceVm.mapIcon = CarServiceSrv.setMapIcon(newValue);
                    loadData();
                    loadMap();

                    $cookieStore.put('carServiceVm.api', newValue);
                }

            });

            $scope.$watch('carServiceVm.page', function (newValue, oldValue) {
                if (newValue !== oldValue) {
                    loadData();
                }

            });

            function loadData() {
                var apiPath = APISrv.getAPIPath('service/' + carServiceVm.api);
                var filterName = CarServiceSrv.getFilter(carServiceVm.api);
                var query = {
                    pageSize: carServiceVm.pageSize,
                    page: carServiceVm.page,
                    filter: carServiceVm[filterName]
                };
                var service = CarServiceSrv.getService(apiPath);

                carServiceVm.services = service.query(query);

                carServiceVm.services.$promise.then(function (result) {
                    carServiceVm.services.objects = result.results;
                    carServiceVm.services.quantity = result.count;
                });
            }

            function loadMap() {
                var apiPath = APISrv.getAPIPath('service/' + carServiceVm.api);
                var filterName = CarServiceSrv.getFilter(carServiceVm.api);
                var query = {
                    filter: carServiceVm[filterName]
                };
                var map = services.getServices(apiPath);

                carServiceVm.map = map.query(query);
                carServiceVm.map.$promise.then(function (result) {
                    carServiceVm.map = result.results;
                });
            }

            function setPage(page) {
                carServiceVm.page = page
            }

            function resetPage() {
                carServiceVm.page = 1
            }

            function clearFilter(filterName) {
                carServiceVm[filterName] = {}
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
                if ($scope.activeTabs.indexOf(tab) > -1) {
                    return true;
                } else {
                    return false;
                }
            }

            //Функция открытия таба в фильтре
            $scope.openTab = function (tab) {

                if ($scope.isOpenTab(tab)) {
                    $scope.activeTabs.splice($scope.activeTabs.indexOf(tab), 1);
                } else {
                    $scope.activeTabs.push(tab);
                }
            }

        }]);
})();
