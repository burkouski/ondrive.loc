ymapsApp.controller('serviceCtrl', ['$scope', function ($scope) {


    $scope.starsInit = function (rating) {
        var rating = rating,
            positiveStar = ~~rating,
            halfStar = 0,
            negativeStar,
            fractional = rating - positiveStar;
        if (fractional > 0.25 && fractional < 0.85) {
            halfStar = 1;
        }

        else if (fractional > 0.85) {
            positiveStar += 1;
        }
        else {
            halfStar = 0;
        }
        negativeStar = 5 - positiveStar - halfStar;
        return {
            positiveStar: _getArray(positiveStar),
            halfStar: _getArray(halfStar),
            negativeStar: _getArray(negativeStar)
        }
    };

    _getArray = function (n) {
        return new Array(n);
    };
    $scope.error = {
        textError: '',
        rateerror: ''
    }
    $scope.reviewSubmit = function () {
        if (!$scope.review.text) {

            $scope.error.textError = 'Пожалуйста заполните поле отзыва';
            console.log($scope.error.textError)
        }
        else {
            $scope.error.textError = '';
        }
        if (!$scope.review.text) {

            $scope.error.rateError = 'Пожалуйста выставьте оценку качества';
            console.log($scope.error.textError)
        }
        else {
            $scope.error.rateError = '';
        }
    };

}]);
