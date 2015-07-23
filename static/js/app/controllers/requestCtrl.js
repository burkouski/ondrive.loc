ymapsApp.controller('requestCtrl', ['$scope','services','$timeout', function ($scope, services, $timeout) {


    $scope.request = {};
    $scope.ajaxLoader = false;
    $scope.result = {
        mess: 'Авторизация'
    };

    $scope.requestSubmit = function (form) {
        console.log($scope.loginUrl)
        parent.$.fancybox.update();
        if (form.$valid) {
            $scope.ajaxLoader = true;
            services.list($scope.loginUrl, $scope.user, function (result) {
                    $scope.result = result;
                    $scope.ajaxLoader = false;
                    console.log(result);
                    if(result.prevPath) {
                        location.href = result.prevPath
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
