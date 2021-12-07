def choices():
    from language_app.models import Language
    _ = []
    for language in Language.objects.all():
        _.append((language.code, language.name))
    return _