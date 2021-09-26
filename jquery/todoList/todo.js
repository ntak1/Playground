$(function () {
    let lastClicked = undefined;
    let previous = undefined;

    function onTarefaDeleteClick() {
        console.log($(this).parent(".tarefa-item").text().trim());
        $(this).parent(".tarefa-item").hide("slow", () => $(this).remove());
    }
    $(".tarefa-delete").click(onTarefaDeleteClick);


    function onTarefaEditKeydown(event) {
        const presseedEnter = event.which === 13;
        if (presseedEnter) {
            console.log("keydown", this)
            const text = $(".tarefa-edit").val()?.trim();
            $(".tarefa-edit").remove();
            $(lastClicked).parent(".tarefa-item").prepend(previous);
            $(this).text(text);
            lastClicked = undefined;
        }
    }

    function onTarefaTextClick() {
        console.log("Here we will edit the item");
        // In case we should continue the input treatment
        if (!$(this).is($(lastClicked))) {
            // Prepare the input to have the old text
            if (lastClicked === undefined) {
                const text = $(this).text().trim();
                previous = $(this);
                const content = `<input type="text" class="tarefa-edit" value="${text}" >`;
                $(this).html(content).keydown(onTarefaEditKeydown);
                lastClicked = this;
            }
        }
    }
    $(".tarefa-texto").click(onTarefaTextClick);

    function addTarefa(text) {
        let $tarefa = $("<div \>").addClass("tarefa-item")
            .append($("<div />").addClass("tarefa-texto").text(text))
            .append($("<div />").addClass("tarefa-delete").text("delete"))
            .append($("<div />").addClass("clear").text("clear"));
        console.log($tarefa);
        $("#tarefa-lista").append($tarefa);
        $(".tarefa-delete").click(onTarefaDeleteClick)
        $(".tarefa-texto").click(onTarefaTextClick)
    }

    function onTextKeydown(event) {
        const presseedEnter = event.which === 13;
        console.log(presseedEnter)
        if (presseedEnter) {
            const text = $("#tarefa").val();
            console.log("Add text", text);
            addTarefa(text);
            $("#tarefa").val("");
        }
    }
    $("#tarefa").on("keydown.enter", onTextKeydown);

});