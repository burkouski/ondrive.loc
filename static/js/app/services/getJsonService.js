ymapsApp.service('getJsonService', ['$http', '$resource', function ($http, $resource) {

    this.square = function (url) {
        return $resource(
            url,
            {
                callback: "JSON_CALLBACK"
            },
            {
                getJson: {
                    method: "JSONP",
                    isArray: false
                }
            }
        );
    };


}])

ymapsApp.factory('services', ['$http', function ($http) {
    data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
    return {
        list: function (url, callback, error) {
            $http({
                method: 'POST',
                data: { 'text': 'this is really important', 'date': '2014-06-09'},
//                headers: {
//                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
//                },
                contentType: "application/x-www-form-urlencoded",
                //dataType: 'json',
                url: url,
                cache: true,
                responseType: 'json',
                isArray: true
            }).success(callback).error(error);
        }
    };
}]);
