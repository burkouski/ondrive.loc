ondriveApp.controller('loginCtrl', ['$scope','services2','$timeout', function ($scope, services2, $timeout) {

    $scope.user = {};
    $scope.pattern = /^[a-zA-Z0-9]*$/;
    $scope.initForm = function(loginUrl, path) {
        if (path) {
            $scope.user.prevPath = path;
        }
        $scope.loginUrl = loginUrl;

    };
    $scope.ajaxLoader = false;
    $scope.result = {
        mess: 'Авторизация'
    };

    $scope.loginSubmit = function (form) {
        parent.$.fancybox.update();
        if (form.$valid) {
            $scope.ajaxLoader = true;
            services2.list($scope.loginUrl, $scope.user, function (result) {
                    $scope.result = result;
                    $scope.ajaxLoader = false;
                    if(result.prevPath) {
                        location.href = result.prevPath;
                    }
                    if(result.status)  {
                        $timeout(function(){
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
