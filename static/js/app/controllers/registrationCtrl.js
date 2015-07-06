ymapsApp.controller('registrationCtrl', ['$scope','services', function ($scope, services) {

    var apiUrl = '/auth/registration/';
    $scope.ajaxLoader = false;
    $scope.result = {
        resultMess: 'регистрация',
        resultSubMess: 'Создайте нового пользователя'
    };


    $scope.registerSubmit = function (form) {

        if (form.$valid) {
            $scope.ajaxLoader = true;
            services.list(apiUrl, $scope.user, function (result) {
                    $scope.result = result;
                    $scope.resultMess = 'Ваше сообщение успешно отправлено';
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
