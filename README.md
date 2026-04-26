# piccolo-scaffold

CLI tool that generates a server-rendered frontend (FastAPI router + Jinja2 templates)
from your [Piccolo](https://piccolo-orm.com/) table definitions.

Supports two styles:

| Style | Command | Description |
|-------|---------|-------------|
| Plain Jinja2 | `piccolo-scaffold` | Post/Redirect/Get — no JavaScript required |
| HTMX | `piccolo-scaffold-htmx` | Partial HTML swaps via [htmx](https://htmx.org/) |

Both commands share the same code; style is controlled by `--style plain|htmx`.

## Install

Until published to PyPI, install directly from GitHub:

```bash
pip install git+https://github.com/EduMake/scaffold-piccolo-htmx.git
```

Once available on PyPI:

```bash
pip install piccolo-scaffold
```

## Quick start

Run from your Piccolo project root (where `tables.py` lives):

```bash
# Plain Jinja2 (default)
piccolo-scaffold

# HTMX variant
piccolo-scaffold-htmx

# Or via python -m (note: underscores, not hyphens)
python -m piccolo_scaffold
python -m piccolo_scaffold --style htmx
```

Generated files:

| File | Purpose |
|------|---------|
| `app_routes.py` / `htmx_routes.py` | FastAPI router with CRUD endpoints |
| `templates/app/page.html` | Root page template |
| `templates/app/_login.html` | Login partial |
| `templates/app/_app.html` | Authenticated app shell |
| `templates/app/_<table>_table.html` | Per-table row listing |

Re-running will **not** overwrite existing files unless you pass `--force`.

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--style` | `plain` | `plain` or `htmx` |
| `--tables-mod` | `tables` | Python module to introspect |
| `--prefix` | `/app` or `/htmx` | URL prefix for the router |
| `--out-routes` | derived from prefix | Output path for routes file |
| `--out-templates` | derived from prefix | Output directory for templates |
| `--force` | off | Overwrite existing files |

## Wire up in app.py

```python
from app_routes import router as app_router
app.include_router(app_router)
```

## Development

```bash
git clone https://github.com/EduMake/scaffold-piccolo-htmx
cd scaffold-piccolo-htmx
pip install -e .
piccolo-scaffold --help
```

## License

MIT
