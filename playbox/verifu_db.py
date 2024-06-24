from store.models import Category, Product

# Fetch a category and its products
category = Category.objects.get(slug='example-slug')
products = Product.objects.filter(category=category)
print(products)  # Ensure this returns a non-empty QuerySet
