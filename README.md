# Instrumentando uma Aplicação com o Sentry

Este projeto demonstra como instrumentar uma aplicação Flask com o Sentry para monitoramento de erros e desempenho (APM - Application Performance Monitoring).

## Funcionalidades

- **Monitoramento de Erros**: Captura e reporta erros ocorridos na aplicação.
- **APM (Application Performance Monitoring)**: Monitora o desempenho da aplicação, incluindo tempos de resposta e gargalos.

## O que é o Sentry?

O Sentry é uma plataforma de monitoramento de erros e desempenho que ajuda desenvolvedores a identificar, rastrear e corrigir problemas em tempo real. Ele oferece:

- **Captura de Erros**: Reporta exceções não tratadas e erros de código.
- **APM**: Monitora o desempenho da aplicação, ajudando a identificar gargalos e melhorar a performance.

## Configuração do Sentry

No arquivo [`__init__.py`](./__init__.py), o Sentry é inicializado com o DSN (Data Source Name) e integrações necessárias:

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://dc0ebf02fd7083942671659182a50341@sentry.io/4508019434979328",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
```

Para configurar o Sentry, é necessário criar uma conta no [site oficial](https://sentry.io) e criar um projeto. Após a criação do projeto, é possível obter o DSN para integração com a aplicação.

## Executando o projeto localmente

1. Clone o repositório:

```bash
git https://github.com/Tech-Preta/sentry-sample.git
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
export FLASK_APP=__init__.py
flask run
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Testando o Sentry

Para testar a integração com o Sentry, você pode clicar no botão "Trigger Test Error" na página inicial (`index.html`). Isso irá gerar um erro de teste que será capturado e reportado pelo Sentry.

```html
<button id="test-error">Trigger Test Error</button>
<script>
    const button = document.getElementById('test-error');
    button.addEventListener('click', () => {
        throw new Error('This is a test error');
    });
</script>
```

## CI/CD com Github Actions

O projeto inclui um pipeline de CI/CD configurado no arquivo [`.github`](dependabot.yml) para atualizar as dependências necessárias.
.github/

```yml
version: 2
updates:
  - package-ecosystem: "pip" 
    directory: "/" 
    schedule:
      interval: "weekly"
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
