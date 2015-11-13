ondriveApp.directive('rating', function () {
    return {
        restrict: 'E',
        scope: {
            avgRating: '='
        },
        template: '<i ng-repeat="star in stars.positiveStars track by $index" style="color: red" class="fa fa-star"></i>' +
        '<i ng-repeat="star in stars.halfStars track by $index" style="color: red" class="fa fa-star-half-o"></i>' +
        '<i ng-repeat="star in stars.negativeStars track by $index" style="color: red" class="fa fa-star-o"></i>',
        link: function ($scope) {
            $scope.stars = getStarRating($scope.avgRating);
            console.log($scope.stars, $scope.avgRating);
        }

    };

    function getStarRating(avgRating) {
        var avgRating = avgRating;
        var positiveStar = ~~avgRating;
        var halfStar = 0;
        var negativeStar = 0;
        var fractional = avgRating - positiveStar;

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
            positiveStars: getArray(positiveStar),
            halfStars: getArray(halfStar),
            negativeStars: getArray(negativeStar)
        }
    }

    function getArray(number) {
        return new Array(number);
    };

});