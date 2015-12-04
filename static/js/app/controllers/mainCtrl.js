(function () {
    'use strict';
    angular.module('ondriveApp')
        .controller('mainCtrl', ['$scope', '$uibModal', mainCtrl]);

    function mainCtrl($scope, $uibModal) {
        $scope.modalOpen = function (size) {

            var modalInstance = $uibModal.open({
                templateUrl: 'login_form.html',
                size: size,
            });
        };
    }
})();
