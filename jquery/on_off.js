console.log("I was loaded")

// Create two events for the same object - both should be run in sequence.
$("#tarefa").keydown(function (event) {
    const keydownEnter = event.which === 13;
    if (keydownEnter) {
        console.log("1. Here we add our task.")
    }
});
$("#tarefa").keydown(function (event) {
    const keydownEnter = event.which === 13;
    if (keydownEnter) {
        console.log("2. Here we add our task.")
    }
});

// Uses the off to disable both of the events associated with the element
// Diable the keydown event
$("#tarefa").off("keydown")

// Using namespaces with on()
$("#tarefa").on("keydown.primeiro", function () {
    console.log("This is the first event");
});

$("#tarefa").on("keydown.segundo", function () {
    console.log("This is the second event");
});

// Disable only one of the events
$("#tarefa").off("keydown.primeiro");