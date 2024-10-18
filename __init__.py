import os
import sentry_sdk
from flask import Flask, render_template
from sentry_sdk.integrations.flask import FlaskIntegration

# Inicializa o Sentry com o DSN correto
sentry_sdk.init(
    dsn="https://dc0ebf02fd7083942671659182a50341@sentry.io/4508019434979328",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

def create_app(test_config=None):
    # Cria e configura o aplicativo Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Carrega a configuração da instância, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração de teste, se passada
        app.config.from_mapping(test_config)

    # Garante que a pasta da instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Define uma rota simples que renderiza o template index.html
    @app.route("/")
    def index():
        return render_template('index.html')

    return app