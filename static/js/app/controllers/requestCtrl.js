(function () {
    'use strict';

    angular.module('ondriveApp')
        .controller('requestCtrl', ['$scope', 'services', '$timeout', function ($scope, services, $timeout) {

            $scope.apiUrl = '/auth/user/service/add/';
            $scope.form = {};
            $scope.ajaxLoader = false;
            $scope.result = {
                mess: 'Запрос на добавление сервиса'
            };
            $scope.form.serviceType = 'Автосервис';

            $scope.formSubmit = function (form) {
                //console.log($scope.loginUrl)
                parent.$.fancybox.update();
                if (form.$valid) {
                    $scope.ajaxLoader = true;
                    services.list($scope.apiUrl, $scope.form, function (result) {
                            $scope.result = result;
                            $scope.ajaxLoader = false;
                            console.log(result);
                            if (result.status) {
                                $timeout(function () {
                                    parent.$.fancybox.close();
                                }, 2000);
                            }


                        },
                        function () {
                            $scope.resultMess = 'Что-то пошло не так. Мы исправим это в ближайшее время';
                            $scope.success = false;
                            $scope.ajaxLoader = false;
                        });
                }

            }
        }]);
})();
