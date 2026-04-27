

# HTMX server-rendered frontend (see htmx_routes.py + templates/htmx/)
from htmx_routes import router as htmx_router
# Plain Jinja2 server-rendered frontend (see app_routes.py + templates/app/)
from app_routes import router as app_router


# Keep server-rendered routes available, but hide them from /docs and /redoc.
app.include_router(htmx_router, include_in_schema=False)
app.include_router(app_router, include_in_schema=False)
# Serve static files (e.g. htmx.min.js) at /static
