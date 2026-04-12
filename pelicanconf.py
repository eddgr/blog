AUTHOR = "Edgar"
SITENAME = "edgar.nyc"
SITEURL = ""

PATH = "content"

TIMEZONE = "US/Eastern"

DEFAULT_LANG = "en"

# Clean URLs for Articles
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

# Clean URLs for Pages
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Disable generation of author pages
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# Disable generation of category pages
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

# Disable generation of tag pages
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Disable archives (optional, but often desired if you're cleaning up)
ARCHIVES_SAVE_AS = ""
YEAR_ARCHIVE_SAVE_AS = ""
MONTH_ARCHIVE_SAVE_AS = ""
DAY_ARCHIVE_SAVE_AS = ""

THEME = "themes/edo"

STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/CNAME": {"path": "CNAME"},
}
