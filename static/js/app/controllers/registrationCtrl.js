ondriveApp.controller('registrationCtrl', ['$scope','services2', function ($scope, services2) {

    var apiUrl = '/auth/registration/';
    $scope.pattern = /^[a-zA-Z0-9]*$/;
    $scope.ajaxLoader = false;
    $scope.result = {
        resultMess: 'регистрация',
        resultSubMess: 'Создайте нового пользователя'
    };


    $scope.registerSubmit = function (form) {

        if (form.$valid) {
            $scope.ajaxLoader = true;
            services2.list(apiUrl, $scope.user, function (result) {
                    $scope.result = result;
                    $scope.success = true;
                    $scope.ajaxLoader = false;
                },
                function () {
                    $scope.resultMess = 'Что-то пошло не так. Мы исправим это в ближайшее время';
                    $scope.success = false;
                    $scope.ajaxLoader = false;
                });
        };

    };
}]);
