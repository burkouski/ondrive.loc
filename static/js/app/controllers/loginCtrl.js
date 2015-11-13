ondriveApp.controller('loginCtrl', ['$scope', 'Request', '$timeout', function ($scope, Request, $timeout) {

    $scope.user = {};
    $scope.pattern = /^[a-zA-Z0-9]*$/;
    $scope.initForm = function (loginUrl, path) {
        if (path) {
            $scope.user.prevPath = path;
        }
        $scope.loginUrl = loginUrl;

    };
    $scope.ajaxLoader = false;
    $scope.result = {
        mess: 'Авторизация'
    };

    $scope.loginSubmit = loginFormSubmit;


    function loginFormSubmit(form) {
        parent.$.fancybox.update();
        if (form.$valid) {
            $scope.ajaxLoader = true;
            Request.sendRequest($scope.loginUrl, $scope.user, loginCallback, loginError)
        }
    }
    function loginCallback(result) {
        $scope.result = result;
        $scope.ajaxLoader = false;

        if (result.prevPath) {
            location.href = result.prevPath;
        }

        if (result.status) {
            $timeout(function () {
                parent.$.fancybox.close();
            }, 2000);
        }
    }

    function loginError(result) {
        $scope.resultMess = 'Что-то пошло не так. Мы исправим это в ближайшее время';
        $scope.success = false;
        $scope.ajaxLoader = false;
    }
}]);
