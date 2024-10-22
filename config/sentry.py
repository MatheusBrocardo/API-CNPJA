import sentry_sdk
from config import settings

def start_sentry():
    # Inicia o monitoramento
    sentry_sdk.init(
            dsn= settings.SentryDns,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            traces_sample_rate=1.0,
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate=1.0,
        )  

def gera_alerta(mensagem):
    sentry_sdk.capture_message(mensagem)