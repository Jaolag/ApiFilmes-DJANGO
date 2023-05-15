function main() {
  const input_usuario = document.getElementById("usuario");
  const input_senha = document.getElementById("senha");
  const form_login = document.getElementById("form-login");

  form_login.onsubmit = async (event) => {
    event.preventDefault();
    const username = input_usuario.value;
    const password = input_senha.value;

    const login_url = "http://localhost:8000/api/token/";
    const opcoes = {
      method: "POST",
      body: JSON.stringify({ username, password }),
      headers: {
        "Content-Type": "application/json"
      }
    };

    const response = await fetch(login_url, opcoes);

    if (response.ok) {
      const result = await response.json();
      const token = result["access"];
      alert("Login realizado com sucesso!");
      localStorage.setItem("access_token", token);
      window.location.replace("index.html");
    } else {
      alert("Usuário e/ou senha incorretos!");
    }

    input_senha.value = "";
    input_usuario.value = "";
    input_usuario.focus();
  };
}

main();
