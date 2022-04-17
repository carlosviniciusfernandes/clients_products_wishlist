import os
from fastapi import FastAPI

from routers.auth import set_auth_routers

app = FastAPI(title="Wishlist API")
set_auth_routers(app)


if os.environ["REMOTE_DEBUGGER"]:
    try:
        import ptvsd
        ptvsd.enable_attach(address=("0.0.0.0", 5678))
        print("\nAttached remote debugger on http://0.0.0.0:5678/")
    except Exception:
        raise Exception("Something went wrong - Could not attach the remote debugger")
