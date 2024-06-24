import os
import django
from django.utils.text import slugify
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playbox.settings')
django.setup()

from store.models import Category, Product

def create_product(name, description, price, stock, category, user):
    slug = slugify(name)
    product, created = Product.objects.get_or_create(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category=category,
        user=user,
        slug=slug
    )
    return product

def populate():
    # Fetch the first user in the database or create a new one
    user = User.objects.first()
    if not user:
        user = User.objects.create_user(username='vendor', password='password')

    # Fetch categories
    consoles = Category.objects.get(slug='consoles')
    current_gen = Category.objects.get(slug='current-generation')
    previous_gen = Category.objects.get(slug='previous-generation')
    handhelds = Category.objects.get(slug='handhelds')

    games = Category.objects.get(slug='games')
    action_games = Category.objects.get(slug='action')
    adventure_games = Category.objects.get(slug='adventure')
    rpg_games = Category.objects.get(slug='rpg')
    sports_games = Category.objects.get(slug='sports')
    racing_games = Category.objects.get(slug='racing')

    accessories = Category.objects.get(slug='accessories')
    controllers = Category.objects.get(slug='controllers')
    headsets = Category.objects.get(slug='headsets')
    memory = Category.objects.get(slug='memory')
    charging = Category.objects.get(slug='charging')

    # Create products
    create_product('PlayStation 5', 'Latest PlayStation console', 49999.99, 50, current_gen, user)
    create_product('Xbox Series X', 'Latest Xbox console', 49999.99, 30, current_gen, user)
    create_product('Nintendo Switch', 'Popular handheld console', 29999.99, 100, handhelds, user)

    create_product('The Last of Us Part II', 'Action-adventure game', 3999.99, 200, action_games, user)
    create_product('Cyberpunk 2077', 'Role-playing game', 3999.99, 150, rpg_games, user)
    create_product('FIFA 21', 'Sports game', 3499.99, 300, sports_games, user)
    create_product('Forza Horizon 4', 'Racing game', 3999.99, 120, racing_games, user)

    create_product('DualShock 4', 'PlayStation 4 controller', 3999.99, 400, controllers, user)
    create_product('Xbox Wireless Controller', 'Xbox controller', 3999.99, 350, controllers, user)
    create_product('Logitech G Pro X', 'Gaming headset', 9999.99, 80, headsets, user)
    create_product('SanDisk 256GB', 'Memory card for Nintendo Switch', 4999.99, 500, memory, user)
    create_product('PowerA Charging Station', 'Charging station for controllers', 1999.99, 250, charging, user)

if __name__ == '__main__':
    populate()
    print('Products populated successfully.')
