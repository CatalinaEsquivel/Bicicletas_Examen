$("#enviar").show(function() {
    $.get("http://127.0.0.1:5503/api.json",
        function(data) {
            $.each(data.categories, (function(i, item) {
                $("#categorias").append("<tr><td>" + item.idCategory + "</td> <td>" +
                    item.strCategory + "</td> <td> <img src ='" + item.strCategoryThumb + "'></td> <td>" +
                    item.strCategoryDescription + "</td></tr>");
            }));
        });

});