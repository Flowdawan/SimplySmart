from django import template
register = template.Library()

@register.simple_tag
def htmlspecialchars(text):
    return (
        text.replace("&", "&amp;").
        replace('"', "&quot;").
        replace("<", "&lt;").
        replace(">", "&gt;").
        replace("\\", "_").
        replace("/", "_").
        replace("%", "").
        replace(" ", "_")

    )