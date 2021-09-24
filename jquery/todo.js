$(function () {
    let lastClicked = undefined;
    let previous = undefined;

    function onTarefaDeleteClick() {
        console.log($(this).parent(".tarefa-item").text().trim());
        $(this).parent(".tarefa-item").hide("slow", () => $(this).remove());
    }
    $(".tarefa-delete").click(onTarefaDeleteClick);


    function onTarefaEditKeydown(event) {
        const presseed_enter = event.which === 13;
        if (presseed_enter) {
            console.log("keydown", this)
            const text = $(".tarefa-edit").val()?.trim();
            $(".tarefa-edit").remove();
            $(lastClicked).parent(".tarefa-item").prepend(previous);
            $(this).text(text);
            lastClicked = undefined;
        }
    }

    function onTarefaTextoClick() {
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
    $(".tarefa-texto").click(onTarefaTextoClick);

});