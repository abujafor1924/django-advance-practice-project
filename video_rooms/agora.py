import time
from django.conf import settings


def generate_agora_token(channel_name, uid=0):
    try:
        from agora_token_builder import RtcTokenBuilder
    except Exception as exc:
        raise RuntimeError(
            "Missing dependency: install 'agora-token-builder' in your environment"
        ) from exc

    AGORA_APP_ID = getattr(settings, 'AGORA_APP_ID', 'YOUR_APP_ID')
    AGORA_APP_CERTIFICATE = getattr(settings, 'AGORA_APP_CERTIFICATE', 'YOUR_APP_CERTIFICATE')

    expire_time = 3600
    current_ts = int(time.time())
    privilege_expired_ts = current_ts + expire_time

    token = RtcTokenBuilder.buildTokenWithUid(
        AGORA_APP_ID,
        AGORA_APP_CERTIFICATE,
        channel_name,
        uid,
        1,
        privilege_expired_ts,
    )

    return token