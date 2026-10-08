const API_URL = "http://localhost:8030/livros/";
const listaLivros = document.getElementById("livrosList");
const formLivro = document.getElementById("formLivro");
const formMessage = document.getElementById("formMessage");

function mostrarMensagem(texto, tipo) {
    formMessage.textContent = texto;
    formMessage.className = `message ${tipo}`;
}

function mensagemDaApi(detail) {
    if (Array.isArray(detail)) {
        return detail.map((erro) => {
            const campo = erro.loc?.at(-1);
            if (erro.type === "string_too_short") {
                return `${campo === "titulo" ? "Título" : "Autor"} deve ter pelo menos 3 caracteres.`;
            }
            if (erro.type === "string_too_long") {
                return `${campo === "titulo" ? "Título" : "Autor"} deve ter no máximo 100 caracteres.`;
            }
            if (erro.type === "greater_than_equal") {
                return "O ano de publicação não pode ser negativo.";
            }
            return erro.msg;
        }).join(" ");
    }

    return typeof detail === "string" ? detail : "Não foi possível salvar o livro.";
}


//Carregar Livros
async function carregarLivros() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Falha ao carregar os livros (HTTP ${response.status}).`);
        }

        const livros = await response.json();
        listaLivros.innerHTML = "";

        livros.forEach((livro) => {
            listaLivros.innerHTML += `
                <div class="livro">
                    <div>
                        <strong>Título:</strong> ${livro.titulo}<br>
                        <strong>Autor:</strong> ${livro.autor}<br>
                        <strong>Ano de Publicação:</strong> ${livro.ano_publicacao}
                    </div>
                    <div class="acoes">
                        <button onclick="removerLivro(${livro.id})">Remover</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        mostrarMensagem(error.message || "Não foi possível conectar à API.", "error");
    }
}

//Remover Livros
async function removerLivro(id) {
    await fetch(`${API_URL}${id}`, {
        method: "DELETE"
    });
    carregarLivros();
}


//Adicionar Livros
formLivro.addEventListener("submit", async (event) => {
    event.preventDefault();

    const submitButton = formLivro.querySelector("button[type='submit']");
    submitButton.disabled = true;

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                titulo: document.getElementById("titulo").value.trim(),
                autor: document.getElementById("autor").value.trim(),
                ano_publicacao: Number(document.getElementById("ano_publicacao").value)
            })
        });

        const resultado = await response.json();
        if (!response.ok) {
            throw new Error(mensagemDaApi(resultado.detail));
        }

        formLivro.reset();
        mostrarMensagem("Livro salvo com sucesso.", "success");
        await carregarLivros();
    } catch (error) {
        mostrarMensagem(error.message || "Não foi possível conectar à API. Os dados não foram apagados.", "error");
    } finally {
        submitButton.disabled = false;
    }
});

carregarLivros();