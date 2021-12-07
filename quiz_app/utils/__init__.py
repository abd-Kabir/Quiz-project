def level_choices():
    from quiz_app.models import Level
    _ = []
    for level in Level.objects.all():
        _.append((level.code, level.name))
    return _


def category_choices():
    from quiz_app.models import Category
    _ = []
    for category in Category.objects.all():
        _.append((category.code, category.name))
    return _
