from datetime import date

# APP Version
version = "1.1.8"
REPO_URL = "https://github.com/juandaherrera/personal_web"

# Personal
MAIN_PIC = "https://juandaherreraweb.blob.core.windows.net/web/juanda.webp"

# Páginas
META = [
    {"name": "og:type", "content": "website"},
]

INDEX_TILE = "Juan David Herrera | Web Personal"
INDEX_DESCRIPTION = (
    f"Portafolio persona de Juan David Herrera © {date.today().year}"
)
INDEX_PREVIEW = (
    "https://juandaherreraweb.blob.core.windows.net/web/preview_web.png"
)

INDEX_META = [
    {"name": "og:title", "content": INDEX_TILE},
    {"name": "og:description", "content": INDEX_DESCRIPTION},
    {"name": "og:image", "content": INDEX_PREVIEW},
]

INDEX_META.extend(META)

# Redes Sociales
GUTHUB_URL = "https://github.com/juandaherrera"
LINKEDIN_URL = "https://www.linkedin.com/in/juan-david-herrera/"
INSTAGRAM_URL = "https://www.instagram.com/juandaherrep/"

# Cargo actual
CURRENT_COMPANY_NAME = "Rappi"
CURRENT_COMPANY_URL = "https://www.rappi.com.co/"
CURRENT_COMPANY_LOGO = "icons/rappi.svg"
CURRENT_POSITION = [
    "Senior Data Analyst",
    3000,
    "Data Engineer",
    3000,
    "BI Specialist",
    3000,
]
