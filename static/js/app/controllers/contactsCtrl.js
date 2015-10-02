ondriveApp.controller('contactsCtrl', ['$scope', 'services', function ($scope, services) {

    var apiUrl = '/api/sendmessage/';
    $scope.ajaxLoader = false;
    $scope.resultMess = 'Отправьте сообщение';


    $scope.contactsSubmit = function (form) {

        if (form.$valid) {
            $scope.ajaxLoader = true;
            services.list(apiUrl, $scope.contacts, function (result) {
                    console.log(result);
                    $scope.resultMess = 'Ваше сообщение успешно отправлено';
                    $scope.success = true;
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
