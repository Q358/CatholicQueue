class SSLRedirect:
    """Redirect the URL to SSL if option enabled."""

    def process_request(self, request):
        """Process request."""
        if not request.is_secure() and settings.SSL_REDIRECT:

            if settings.DEBUG and request.method == 'POST':
                raise RuntimeError(
                    "Django can't perform a SSL redirect with POST data. "
                )

            return HttpResponsePermanentRedirect(
                u"https://{}{}".format(
                    request.get_host(),
                    request.get_full_path(),
                )
            )