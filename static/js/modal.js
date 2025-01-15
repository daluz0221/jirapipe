document.getElementById('crearFormulario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita el envío normal del formulario

    const form = event.target;
    const formData = new FormData(form);

    fetch("{% url 'mi_modelo_crear' %}", {
        method: "POST",
        body: formData,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Cierra el modal
            const modalElement = document.getElementById('crearModal');
            const modal = bootstrap.Modal.getInstance(modalElement);
            modal.hide();

            // Actualiza la UI con el nuevo objeto
            const nuevoObjetoHTML = `<li>${data.campo1}</li>`;
            document.getElementById('listaObjetos').innerHTML += nuevoObjetoHTML;
        } else {
            // Muestra errores en el formulario
            console.error(data.errors);
        }
    })
    .catch(error => console.error('Error:', error));
});
