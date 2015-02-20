ymapsApp.controller('serviceCtrl', ['$scope', function ($scope) {


$scope.starsInit = function(rating) {
    var rating = parseFloat(rating.replace(",", ".")),
        positiveStar = ~~rating,
        halfStar = 0,
        negativeStar,
        fractional = rating - positiveStar;
console.log(rating,positiveStar,fractional)
    if (fractional > 0.25 && fractional < 0.85 ) {
        halfStar = 1;
    }

    else if (fractional > 0.85) {
        positiveStar += 1;
    }
    else {
        halfStar = 0;
    }
    negativeStar = 5 - positiveStar - halfStar;
    console.log(halfStar)
    return {
        positiveStar: _getArray(positiveStar),
        halfStar: _getArray(halfStar),
        negativeStar: _getArray(negativeStar)
    }
};

_getArray=function(n){
     return new Array(n);
};

}]);
