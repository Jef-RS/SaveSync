function handleCredentialResponse(response) {
    // Receba a resposta do token de ID do Google
    console.log(response.credential);
}
window.onload = function () {
    // Configurar o formulário de login
    var loginForm = document.getElementById('login-form');
    loginForm.onsubmit = function (event) {
        event.preventDefault();
        var email = loginForm.email.value;
        google.accounts.id.initialize({
            client_id: 'SEU_CLIENT_ID',
            callback: handleCredentialResponse,
            cancel_on_tap_outside: false,
            prompt_parent_id: 'login-form'
        });
        google.accounts.id.prompt({
            callback: handleCredentialResponse,
            login_hint: email
        });
    };
};