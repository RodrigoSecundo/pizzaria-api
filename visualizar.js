document.addEventListener('DOMContentLoaded', function() {
    const clientList = document.getElementById('clientList');

    // Função para buscar clientes do backend
    async function fetchClients() {
        const response = await fetch('/api/clients');
        const clients = await response.json();
        renderClients(clients);
    }

    // Função para renderizar os clientes na tabela
    function renderClients(clients) {
        clientList.innerHTML = ''; // Limpa a tabela antes de preencher
        clients.forEach(client => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <th scope="row">${client.id}</th>
                <td>${client.name}</td>
                <td>${client.email}</td>
            `;
            clientList.appendChild(row);
        });
    }

    // Função para registrar cliente
    document.getElementById('registerForm').addEventListener('submit', async function(event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        const response = await fetch('/api/clients', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email })
        });

        if (response.ok) {
            alert('Cliente cadastrado com sucesso!');
            fetchClients(); // Atualiza a lista de clientes
        } else {
            alert('Erro ao cadastrar cliente.');
        }
    });

    // Busca os clientes ao carregar a página
    fetchClients();
});
