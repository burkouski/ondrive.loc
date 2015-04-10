ymapsApp.controller('loginCtrl', ['$scope','services', function ($scope, services) {

    var apiUrl = '/auth/login/';
    $scope.ajaxLoader = false;
    $scope.result = {
        mess: 'Авторизация'
    }

    $scope.loginSubmit = function (form) {

        if (form.$valid) {
            $scope.ajaxLoader = true;
            services.list(apiUrl, $scope.user, function (result) {
                    //alert(true)
                    $scope.result = result
                    console.log($scope.result)
                    $scope.ajaxLoader = false;
                },
                function () {
                    $scope.resultMess = 'Что-то пошло не так. Мы исправим это в ближайшее время';
                    $scope.success = false;
                    $scope.ajaxLoader = false;
                });
        }

    }
}]);
