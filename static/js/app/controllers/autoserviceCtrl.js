(function() {
    'use strict';
    angular.module('ondriveApp')
        .controller('autoserviceCtrl', ['$scope', '$cookieStore', 'services', function ($scope, $cookieStore, services) {

            $scope.init = function (filterName, apiUrl, filterParam, filterValue) {
                $scope.preloader = false;
                $scope.gridView = false;
                $scope.filterName = filterName;
                $scope.apiUrl = apiUrl;

                var filterParam = filterParam,
                    filterValue = filterValue,
                    filterCook = $cookieStore.get($scope.filterName),
                    activeTabsCook = $cookieStore.get('activeTabs');
                if (filterParam == undefined) {
                    $scope[$scope.filterName] = (filterCook) ? filterCook : {};
                    $scope.activeTabs = (activeTabsCook) ? activeTabsCook : [];
                }
                else {
                    var singleFilter = {};
                    singleFilter['options'] = {};
                    singleFilter['options'][filterParam] = [parseInt(filterValue)];

                    $scope[$scope.filterName] = singleFilter;
                    $scope.activeTabs = [];
                }
                //$scope[$scope.filterName] = (filterCook) ? filterCook : {};
                //    $scope.activeTabs = (activeTabsCook) ? activeTabsCook : [];
                $scope.quantity = 6;
                $scope.curPage = 1;
                $scope[$scope.filterName].meta = {
                    quantity: $scope.quantity,
                    page: $scope.curPage - 1
                };
                $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
            };

            var setCookie = function () {
                $cookieStore.put($scope.filterName, $scope[$scope.filterName]);
                $cookieStore.put('activeTabs', $scope.activeTabs);

            };

            //Функция загрузки данных
            $scope.loadRemoteData = function (apiUrl, data) {
                $scope.preloader = false;
                services.list(apiUrl, data, function (services) {
                        $scope.services = services.objects.info;
                        $scope.meta = services.objects.meta;
                        $scope.mapObjects = services.mapObjects;
                        $scope.preloader = true;
                        setCookie();
                        resetPagination($scope.meta, $scope.quantity);
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
            };

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
            };

            // Функция изменения отображения сервисов
            $scope.changeView = function (view) {
                $scope.gridView = view; // path not hash
            };

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

            $scope.changeFilter = function () {
                resetPage()
            };

            $scope.clearFilter = function (filterName) {
                angular.forEach($scope[filterName].options, function (value, key) {
                    $scope[filterName]['options'][key] = [];
                });
                resetPage()

            };

            $scope.changePage = function (curPage) {
                $scope.curPage = curPage + 1;
                $scope[$scope.filterName].meta.page = curPage;
                $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
            };

            $scope.changeQuantity = function () {
                $scope[$scope.filterName].meta.quantity = $scope.quantity;
                resetPage()
                //$scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
            };

            var resetPagination = function (objQuantity, displayQuantity) {

                $scope.pagination = _getArray(Math.ceil(objQuantity / displayQuantity))
            };


            var _getArray = function (n) {
                return new Array(n);
            };

            function resetPage() {
                console.log('dfndfnfd');
                $scope.curPage = 1;
                $scope[$scope.filterName].meta.page = $scope.curPage - 1;
                console.log($scope[$scope.filterName]);
                $scope.loadRemoteData($scope.apiUrl, $scope[$scope.filterName]);
            }

        }]);
})();
