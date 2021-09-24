$(function () {
    let lastClicked = undefined;
    let previous = undefined;

    function onTarefaDeleteClick() {
        console.log("Good bye!");
        console.log($(this).parent(".tarefa-item").text().trim());
        $(this).parent(".tarefa-item").hide("slow", () => $(this).remove());
    }
    $(".tarefa-delete").click(onTarefaDeleteClick);


    function onTarefaEditKeydown(event) {
        const presseed_enter = event.which === 13;
        if (presseed_enter) {
            console.log("keydown", this)
            const text = $(".tarefa-edit").val();
            $(".tarefa-edit").remove();
            var txt2 = $("<div></div>").text(text === undefined ? "" : text).addClass("tarefa-texto"); 
            $(lastClicked).append(previous);
            $("tarefa-texto").text(txt2);
            lastClicked = undefined;
        }
    }

    function onTarefaItemClick() {
        console.log("Here we will edit the item", this);
        // In case we should continue the input treatment
        if (!$(this).is($(lastClicked))) {
            // Prepare the input to have the old text
            if(lastClicked === undefined) {
                const text = $(this).children(".tarefa-texto").text();
                previous = $(this).children();
                const content = `<input type="text" class="tarefa-edit" value="${text}" >`;
                $(this).html(content).keydown(onTarefaEditKeydown);
                lastClicked = this;
            }
        }
    }
    $(".tarefa-item").click(onTarefaItemClick);

});