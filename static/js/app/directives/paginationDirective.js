ondriveApp.directive('pagination', function () {
    return {
        restrict: 'E',
        scope: {
            pageSize: '=pageSize',
            itemQuantity: '=itemQuantity',
            setPage: '&',
            curPage: '=page'
        },
        template: '<ul class="pagination" ng-show="itemQuantity > pageSize">' +
        '<li ng-class="{active: pageNumber==curPage}" ng-repeat="pageNumber in pagination"  class="pagination__item">' +
        '<a class="pagination__link" ng-click="setPageNumber(pageNumber)"  >{$pageNumber$}</a>' +
        '</li>' +
        '</ul>',
        controller: function ($scope, $element) {
            $scope.setPageNumber = function(pageNumber){
                console.log(pageNumber);
                console.log($scope.setPage2);
                $scope.setPage({page: pageNumber});
            },
            $scope.$watch('curPage', function(){
                console.log($scope.curPage);
            })
            $scope.$watchGroup(["pageSize",'itemQuantity'],function(newValue,OldValue,scope){
                     if (newValue !== undefined && $scope.itemQuantity !== undefined && $scope.pageSize !== undefined){

                         $scope.pagination = getPagination($scope.itemQuantity, $scope.pageSize);
                     }
                 });
        }

    };

    function getPagination (items, pageSize) {
        var items = items;
        var pageSize = pageSize;
        var paginationLength = parseInt(Math.ceil(items/pageSize));
        var pagination = [];
        for (var i= 1; i<=paginationLength; i++) {
            pagination.push(i)
        }
        return pagination

    }
})