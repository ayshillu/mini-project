from django import template

register = template.Library()

@register.filter
def star_rating(rating):
    filled_stars = '★' * rating
    empty_stars = '☆' * (5 - rating)
    return filled_stars + empty_stars
