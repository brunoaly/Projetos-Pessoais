let tarefas = [];


function adicionarTarefa(event) {
    event.preventDefault();

    let tarefa = document.getElementById("inputTarefa").value;
    let prioridade = document.getElementById("inputPrioridade").value;
    let objTarefa = { tarefa: tarefa, prioridade: prioridade };

    tarefas.push(objTarefa);

    document.getElementById("inputTarefa").value = "";
    document.getElementById("inputPrioridade").value = "1";

    atualizarListaTarefas();
}

function atualizarListaTarefas() {

    tarefas.sort(function (a, b) {
        return b.prioridade - a.prioridade;
    });

    $("#listaTarefas").empty();

    for (let i = 0; i < tarefas.length; i++) {
        let card = '<div class="card">';
        card += '<div class="card-body">';
        card += '<h5 class="card-title">' + tarefas[i].tarefa + '</h5>';
        card += '<p class="card-text">Prioridade: ' + tarefas[i].prioridade + '</p>';
        card += '</div>';
        card += '</div>';

        $("#listaTarefas").append(card);
    }
}

$("#formTarefa").submit(adicionarTarefa);
