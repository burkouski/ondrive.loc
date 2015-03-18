ymapsApp.controller('contactsCtrl', ['$scope','services', function ($scope, services) {

    var apiUrl = '/api/sendmessage/'
    $scope.error = {
        emailError: '',
        messageError: ''
    }
    $scope.contacts = {}
    $scope.resultMess = 'Отправить сообщение'


    $scope.contactsSubmit = function () {

            services.list(apiUrl, $scope.contacts, function (result) {
                //alert(true)
                $scope.resultMess = 'Ваше сообщение успешно отправлено';
                $scope.success = true
            },
            function () {
                $scope.resultMess = 'Что-то пошло не так. Мы исправим это в ближайшее время';
                $scope.success = false
            });

    };

}]);
