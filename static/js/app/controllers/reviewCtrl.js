(function () {
    'use strict';

    angular.module('ondriveApp')
        .controller('reviewCtrl', ['$scope', 'Request', function ($scope, Request) {

            var apiUrl = '/reviews/api/createreview/';

            $scope.error = {};

            $scope.reviewSubmit = function () {
                if (!$scope.review.review) {

                    $scope.error.textError = 'Пожалуйста заполните поле отзыва';
                }
                else {
                    $scope.error.textError = '';
                }
                if (!$scope.review.rate) {

                    $scope.error.rateError = 'Пожалуйста выставьте оценку качества';
                }
                else {
                    $scope.error.rateError = '';
                }

                if ($scope.review.review && $scope.review.rate) {

                    Request.sendRequest(apiUrl, $scope.review, createReviewCallback, createReviewError)

                }
            };


            function createReviewCallback() {
                $scope.result = 'Спасибо за ваше мнение! Отзыв будет опубликован после модерации.';
            };

            function createReviewError() {
                $scope.result = 'Что-то пошло не так. Мы исправим это в ближайшее время';
            };

        }]);
})();