const SERVER_URL = "http://livro-capitulo07.herokuapp.com/hello"
const ERROR_SERVER_URL = "http://livro-capitulo07.herokuapp.com/error"
// const POSTMON_URL = "http://api.postmon.com.br/v1/cep/04101-300"
// Invalid
const POSTMON_URL = "http://api.postmon.com.br/v1/cep/-"

$(function() {

    function onGetMessageButtonClick() {
        const payload = {
            nome: "Naomi Takemoto"
        }

        // Option 1
        // const response = $.get(SERVER_URL, payload, function(data) {
        //     alert(data);
        // })

        // Option 2
        const response = $.get(SERVER_URL, payload)

        response.done(function(data){
            alert(data);
        })
    }

    function onGetErrorMessageButtonClick() {
        $.get(ERROR_SERVER_URL).fail(function(data) {
            alert(data.responseText);
        })
    }


    function onGetPostmonResponse() {
        const response = $.getJSON(POSTMON_URL);
        response.done(function(data) {
            alert(data.logradouro);
        });
        response.fail(function(error) {
            alert(error.statusText);
        })
    }

    // Buttons
    const $getMessageButton = $(`<input type="button" value="Get Message" />`)
                                .click(onGetMessageButtonClick);
    $("body").append($getMessageButton);

    const $getErrorMessageButton = $(`<input type=button value="Get error"/>`)
                                    .click(onGetErrorMessageButtonClick);
    $("body").append($getErrorMessageButton)

    const $getPostmonResponse = $(`<input type=button value="Get Postmon" />`)
                                    .click(onGetPostmonResponse);
    $("body").append($getPostmonResponse);
});