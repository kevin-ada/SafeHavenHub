from django import template

register = template.Library()


@register.filter
def truncate_words(value, arg):
    """Truncate A String to a Certain Number of Words"""

    words = value.split()

    if len(words) > arg:
        words = words[:arg]
    return ' '.join(words)
