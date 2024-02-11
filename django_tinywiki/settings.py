from django.conf import settings as django_settings
from django.contrib.auth.models import User as UserModel
from django.utils.translation import gettext_lazy as _, gettext_noop as N_
from django.utils.module_loading import import_string
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

import os

TINYWIKI_VERSION = "0.0.1"

TINYWIKI_IS_MAIN_APP = getattr(django_settings,"TINYWIKI_IS_MAIN_APP",False)

TINYWIKI_TITLE = getattr(django_settings,"TINYWIKI_TITLE",_("TinyWiki"))

TINYWIKI_INDEX = getattr(django_settings,
                         "TINYWIKI_INDEX",
                         _("en-tinywiki-index"))

TINYWIKI_HOME_URL = getattr(django_settings,
                            "TINYWIKI_HOME_URL",
                            reverse_lazy("tinywiki:index"))

TINYWIKI_BASE_TEMPLATE = getattr(django_settings,
                                 "TINYWIKI_BASE_TEMPLATE",
                                 "django_tinywiki/base.html")
TINYWIKI_PAGE_VIEW_TEMPLATE = getattr(django_settings,
                                      "TINYWIKI_PAGE_VIEW_TEMPLATE",
                                      "django_tinywiki/wiki/page.html")
TINYWIKI_PAGE_VIEW_URL = getattr(django_settings,"TINYWIKI_PAGE_VIEW_URL","tinywiki:page")
TINYWIKI_PAGE_EDIT_TEMPLATE = getattr(django_settings,
                                      "TINYWIKI_PAGE_EDIT_TEMPLATE",
                                      "django_tinywiki/wiki/edit.html")
TINYWIKI_PAGE_EDIT_URL = getattr(django_settings,"TINYWIKI_PAGE_EDIT_URL","tinywiki:page-edit")
TINYWIKI_PAGE_CREATE_TEMPLATE = getattr(django_settings,
                                        "TINYWIKI_PAGE_CREATE_TEMPLATE",
                                        "django_tinywiki/wiki/create.html")
TINYWIKI_PAGE_CREATE_URL = getattr(django_settings,"TINYWIKI_PAGE_CREATE_URL","tinywiki:page-create")
TINYWIKI_PAGE_NEW_TEMPLATE = getattr(django_settings,
                                     "TINYWIKI_PAGE_NEW_TEMPLATE",
                                     TINYWIKI_PAGE_CREATE_TEMPLATE)
TINYWIKI_PAGE_NEW_URL = getattr(django_settings,'TINYWIKI_PAGE_NEW_URL','tinywiki:page-new')
TINYWIKI_STYLE = getattr(django_settings,
                         "TINYWIKI_STYLE",
                         "default")
TINYWIKI_CSS = getattr(django_settings,
                       "TINYWIKI_CSS",
                       "{url}django_tinywiki/styles/{style}.css".format(
                            url=django_settings.STATIC_URL,
                            style=TINYWIKI_STYLE))
TINYWIKI_CODEHILITE_STYLE = getattr(django_settings,
                                    "TINYWIKI_CODEHILITE_STYLE",
                                    "github-dark")
TINYWIKI_CODEHILITE_CSS = getattr(django_settings,
                                  "TINYWIKI_CODEHILITE_CSS",
                                  "{url}django_tinywiki/styles/codehilite/{style}.css".format(
                                      url=django_settings.STATIC_URL,
                                      style=TINYWIKI_CODEHILITE_STYLE))

TINYWIKI_MARKDOWN_EXTENSIONS = getattr(django_settings,
                                       "TINYWIKI_MARKDOWN_EXTENSIONS",
                                       None)
TINYWIKI_CONTEXT_CALLBACK = getattr(django_settings,
                                    "TINYWIKI_CONTEXT_CALLBACK",
                                    None)

TINYWIKI_DEFAULT_LANGUAGE = getattr(django_settings,"TINYWIKI_DEFAULT_LANGUAGE","en")

if not hasattr(django_settings,"MEDIA_URL"):
    django_settings.MEDIA_URL = "/media"

TINYWIKI_MEDIA_ROOT = getattr(django_settings,
                              "TINYWIKI_MEDIA_ROOT",
                              django_settings.BASE_DIR / "media" / "wiki")
TINYWIKI_MEDIA_URL = getattr(django_settings,
                             "TINYWIKI_MEDIA_URL",
                             django_settings.MEDIA_URL + "wiki/")

TINYWIKI_UPLOAD_ROOT = getattr(django_settings,"TINYWIKI_UPLOAD_ROOT",django_settings.BASE_DIR / '.uploads')
TINYWIKI_IMAGE_UPLOAD_URL = getattr(django_settings,
                                    "TINYWIKI_IMAGE_UPLOAD_URL",
                                    'tinywiki:image-upload')
TINYWIKI_IMAGE_UPLOAD_TEMPLATE = getattr(django_settings,
                                         "TINYWIKI_IMAGE_UPLOAD_TEMPLATE",
                                         'django_tinywiki/wiki/image-upload.html')
TINYWIKI_IMAGE_UPLOAD_DIRECTORY = getattr(django_settings,
                                          "TINYWIKI_IMAGE_UPLOAD_DIRECTORY",
                                          os.path.join(TINYWIKI_UPLOAD_ROOT,'wiki-images'))

TINYWIKI_MEDIA_STORAGE = getattr(django_settings,
                                 "TINYWIKI_MEDIA_STORAGE",
                                 FileSystemStorage(location=TINYWIKI_MEDIA_ROOT,
                                                   base_url=TINYWIKI_MEDIA_URL))

TINYWIKI_IMAGE_WIKI_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_WIKI_WIDTH",860)
TINYWIKI_IMAGE_PREVIEW_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_PREVIEW_WIDTH",((860 - 30) // 4))
TINYWIKI_IMAGE_SIDEBAR_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_SIDEBAR_WIDTH",200)

TINYWIKI_AUTH_USER_MODEL = getattr(django_settings,
                                   "TINYWIKI_AUTH_USER_MODEL",
                                   getattr(django_settings,"AUTH_USER_MODEL","django.contrib.auth.models.User"))

if TINYWIKI_IS_MAIN_APP:
    TINYWIKI_LOGIN_URL = getattr(django_settings,
                                "TINYWIKI_LOGIN_URL",
                                reverse_lazy("tinywiki:auth-login"))
    TINYWIKI_SIGNUP_URL = getattr(django_settings,
                                  "TINYWIKI_SIGNUP_URL",
                                  getattr(django_settings,"SIGNUP_URL",reverse_lazy("tinywiki:auth-signup")))
    TINYWIKI_LOGOUT_URL = getattr(django_settings,
                                  "TINYWIKI_LOGOUT_URL",
                                  getattr(django_settings,"LOGOUT_URL",reverse_lazy("tinywiki:auth-logout")))
else:
    TINYWIKI_LOGIN_URL = getattr(django_settings,
                                 "TINYWIKI_LOGIN_URL",
                                 getattr(django_settings,"LOGIN_URL","/login/"))
    TINYWIKI_SIGNUP_URL = getattr(django_settings,
                                  "TINYWIKI_SIGNUP_URL",
                                  getattr(django_settings,"SIGNUP_URL","/logout"))
    TINYWIKI_LOGOUT_URL = getattr(django_settings,
                                  "TINYWIKI_LOGOUT_URL",
                                  getattr(django_settings,"LOGOUT_URL","/signup/"))

TINYWIKI_USER = getattr(django_settings,"TINYWIKI_USER",{"username":"TinyWiki Team","email":"tinywiki@cmoser.eu"})


TINYWIKI_GROUP_ADMIN = "tinywiki-admin"
TINYWIKI_GROUP_AUTHOR = "tinywiki-author"
TINYWIKI_GROUP_USER = "tinywiki-user"

TINYWIKI_PERM_CREATE_PAGE = "tinywiki-create-page"
TINYWIKI_PERM_DELETE_PAGE = "tinywiki-delete-page"
TINYWIKI_PERM_EDIT_PAGE = "tinywiki-edit-page"
TINYWIKI_PERM_EDIT_USER_PAGE = "tinywiki-edit-user-page"

TINYWIKI_APPNAME = "django_tinywiki"

TINYWIKI_LANGUAGES = [
    ("en",N_("English")),
    ("de",N_("German")),
]

TINYWIKI_STAFF_IS_WIKI_ADMIN = getattr(django_settings,"TINYWIKI_STAFF_IS_WIKI_ADMIN",False)
TINYWIKI_SUPERUSER_IS_WIKI_ADMIN = getattr(django_settings,"TINYWIKI_SUPERUSER_IS_WIKI_ADMIN",True)


# allow mulitple instances of tinywiki in one prjeoct by overriding app based settings
# !!!DO THIS ONLY WHEN YOU KNOW WHAT YOU ARE DOING!!!
if os.path.isfile(os.path.join(os.path.dirname(__file__),"tinywiki_settings.py")):
    from .tinywiki_settings import *

__mkperm = lambda x: "{}.{}".format(TINYWIKI_APPNAME,x)

TINYWIKI_GROUPS = [
    (TINYWIKI_GROUP_ADMIN,[TINYWIKI_PERM_CREATE_PAGE,
                           TINYWIKI_PERM_DELETE_PAGE,
                           TINYWIKI_PERM_EDIT_PAGE,
                           TINYWIKI_PERM_EDIT_USER_PAGE]),
    (TINYWIKI_GROUP_AUTHOR,[TINYWIKI_PERM_CREATE_PAGE,
                            TINYWIKI_PERM_EDIT_PAGE,
                            TINYWIKI_PERM_EDIT_USER_PAGE]),
    (TINYWIKI_GROUP_USER,[TINYWIKI_PERM_EDIT_USER_PAGE]),
]

BUILTIN_MARKDOWN_EXTENSIONS = [
    "toc",
    "codehilite",
    "fenced_code",
    "tables",
    "django_tinywiki.markdown_extensions:DjangoURLExtension",
    "django_tinywiki.markdown_extensions:TinywikiImageExtension",
    "django_tinywiki.markdown_extensions:TinywikiLinkedImagesExtension",
    "django_tinywiki.markdown_extensions:TinywikiLinkExtension",
    "django_tinywiki.markdown_extensions:DelExtension",
    "django_tinywiki.markdown_extensions:CopyrightExtension",
]

# snaitize context callback
if TINYWIKI_CONTEXT_CALLBACK is None:
    TINYWIKI_CONTEXT_CALLBACK = lambda self,x: {}
elif isinstance(TINYWIKI_CONTEXT_CALLBACK,str):
    TINYWIKI_CONTEXT_CALLBACK = import_string(TINYWIKI_CONTEXT_CALLBACK)

if not callable(TINYWIKI_CONTEXT_CALLBACK):
    raise ValueError("Option \"TINYWIKI_CONTEXT_CALLBACK\" does not result in a callable function!")

if TINYWIKI_MARKDOWN_EXTENSIONS is None:
    TINYWIKI_MARKDOWN_EXTENSIONS = BUILTIN_MARKDOWN_EXTENSIONS
else:
    TINYWIKI_MARKDOWN_EXTENSIONS = list(TINYWIKI_MARKDOWN_EXTENSIONS) + BUILTIN_MARKDOWN_EXTENSIONS
