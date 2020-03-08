$(document).ready(function (){

    // Отправка формы на создание страны
    $("#add_country_button").on("click",function () {
        alert("Нажали кнопку");
        let data = [];
        $.each($(".country-param"), function(){
            data.push(this);
        });
        $.ajax({
            url: "/create_country_form/",
            type: "POST",
            dataType: "html",
            headers:{
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            data: data,
            success: function(response){
                alert(response);
            },
            error: function () {
                alert("Error");
            }
        });
    });

    // Обработка формы после каждого изменения
    let func;
    $('.country-param').on('keyup', function () {
        clearTimeout(func);
        let template = $(this).val();
        let data = [];
        $.each($(".country-param"), function(){
            data.push(this);
        });
        func = setTimeout(function () {
            if (template.length > 1){
                $.ajax({
                    url: "/check_country_form/",
                    type: "POST",
                    dataType: "html",
                    headers:{
                        "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                    },
                    data: data,
                    success: function(response){
                        $(".country-result").html(response);
                    },
                    error: function () {
                        alert("Error");
                    }
                });
            }
        }, 1000)
    });
});