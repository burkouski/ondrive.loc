ymapsApp.directive("compareTo", function() {
    return {
        //restrict: 'A',
        require: "ngModel",
        scope: {
            otherModelValue: "=compareTo"
        },
        link: function(scope, element, attributes, ngModel) {

            ngModel.$validators.compare = function(modelValue) {
                return modelValue == scope.otherModelValue;
                //console.log()
            };

            scope.$watch("otherModelValue", function() {
                ngModel.$validate();
                console.log('true')
            });
        }
    };
})