$(document).ready(function (){

    // Отправка формы на создание страны
    $("#add_payment_button").on("click",function () {
        alert("Нажали кнопку");
        let data = [];
        $.each($(".country-param"), function(){
            data.push(this);
        });
        $.ajax({
            url: "/create_payment_form/",
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
    $('.payment-param').on('keyup', function () {
        clearTimeout(func);
        let template = $(this).val();
        let data = [];
        $.each($(".payment-param"), function(){
            data.push(this);
        });
        func = setTimeout(function () {
            if (template.length > 1){
                $.ajax({
                    url: "/check_payment_form/",
                    type: "POST",
                    dataType: "html",
                    headers:{
                        "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                    },
                    data: data,
                    success: function(response){
                        $(".payment-result").html(response);
                    },
                    error: function () {
                        alert("Error");
                    }
                });
            }
        }, 1000)
    });
});