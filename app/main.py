import os
from fastapi import FastAPI

from routers.auth import set_auth_routers
from routers.wishlist import set_wishlist_router

app = FastAPI(title="Wishlist API")
set_auth_routers(app)
set_wishlist_router(app)


if os.environ.get("REMOTE_DEBUGGER", False):
    try:
        import ptvsd
        ptvsd.enable_attach(address=("0.0.0.0", 5678))
        print("\nAttached remote debugger on http://0.0.0.0:5678/")
    except Exception:
        raise Exception("Something went wrong - Could not attach the remote debugger")
