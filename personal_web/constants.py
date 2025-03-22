from datetime import date

from personal_web.utils import get_version_from_toml

# APP Version
version = get_version_from_toml()
REPO_URL = "https://github.com/juandaherrera/personal_web"

# Personal
MAIN_PIC = "img/juanda.webp"

# Páginas
META = [
    {"name": "og:type", "content": "website"},
]

INDEX_TILE = "Juan David Herrera | Web Personal"
INDEX_DESCRIPTION = f"Portafolio personal de Juan David Herrera © {date.today().year}"
INDEX_PREVIEW = "img/web_preview.webp"

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
    "Python Developer",
    3000,
    "Data Engineer",
    3000,
]
