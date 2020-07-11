from django import template

register = template.Library()


@register.simple_tag
def background_image(file_url):
    if file_url:
        return 'background: url(' + file_url.url + ');background-repeat:\
            no-repeat;background-size: cover;'

    else:
        return ''
