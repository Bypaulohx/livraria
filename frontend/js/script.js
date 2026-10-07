const API_URL = "http://localhost:8030/livros";
const listaLivros = document.getElementById("livrosList");
const formLivro = document.getElementById("formLivro");

//Adicionar Livros
formLivro.addEventListener("submit", async (event) => {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const ano = Number(document.getElementById("ano_publicacao").value);

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            titulo: titulo,
            autor: autor,
            ano_publicacao: ano_publicacao
        })
    });
    formLivro.reset();
});
