import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playbox.settings')
django.setup()

from store.models import Category

def populate_categories():
    print("populating")
    # Clear existing categories to avoid duplicates
    Category.objects.all().delete()
    
    # Gaming Consoles
    gaming_consoles = Category.objects.create(name="Gaming Consoles")
    
    current_gen = Category.objects.create(name="Current Generation", parent=gaming_consoles)
    Category.objects.create(name="PlayStation 5", parent=current_gen, description="Experience the latest in gaming with the PlayStation 5, featuring lightning-fast load times, stunning graphics, and an immersive gaming experience.")
    Category.objects.create(name="Xbox Series X/S", parent=current_gen, description="The Xbox Series X and Series S offer powerful performance, quick resume, and access to a vast library of games through Xbox Game Pass.")
    Category.objects.create(name="Nintendo Switch", parent=current_gen, description="The Nintendo Switch combines the power of a home console with the flexibility of a handheld, allowing you to play your favorite games anywhere.")

    previous_gen = Category.objects.create(name="Previous Generation", parent=gaming_consoles)
    Category.objects.create(name="PlayStation 4", parent=previous_gen, description="The PlayStation 4 delivers an incredible gaming experience with a vast library of exclusive titles and multimedia capabilities.")
    Category.objects.create(name="Xbox One", parent=previous_gen, description="The Xbox One offers a diverse range of games, multimedia integration, and seamless online gaming through Xbox Live.")
    Category.objects.create(name="Nintendo Wii U", parent=previous_gen, description="The Wii U offers unique gameplay experiences with its innovative GamePad controller and a library of beloved Nintendo titles.")

    retro_consoles = Category.objects.create(name="Retro Consoles", parent=gaming_consoles)
    Category.objects.create(name="NES/SNES", parent=retro_consoles, description="Relive the golden age of gaming with the NES and SNES, featuring classic titles that defined a generation.")
    Category.objects.create(name="Sega Genesis", parent=retro_consoles, description="Experience the 16-bit era with the Sega Genesis, home to iconic games and unforgettable adventures.")
    Category.objects.create(name="GameCube", parent=retro_consoles, description="The Nintendo GameCube offers a diverse library of beloved games with unique gameplay experiences and multiplayer fun.")
    Category.objects.create(name="PlayStation 1/2/3", parent=retro_consoles, description="Rediscover classic PlayStation titles across three generations, from groundbreaking PS1 games to the powerful PS3 era.")
    Category.objects.create(name="Xbox 360", parent=retro_consoles, description="The Xbox 360 revolutionized gaming with its online capabilities, diverse game library, and multimedia features.")

    # Video Games
    video_games = Category.objects.create(name="Video Games")

    new_releases = Category.objects.create(name="New Releases", parent=video_games, description="Stay up-to-date with the latest video game releases, featuring the newest titles across all platforms.")
    top_sellers = Category.objects.create(name="Top Sellers", parent=video_games, description="Discover the best-selling games that everyone is talking about, from blockbuster hits to timeless classics.")
    pre_orders = Category.objects.create(name="Pre-Orders", parent=video_games, description="Secure your copy of upcoming games and be among the first to play the most anticipated titles.")
    
    genres = Category.objects.create(name="Genres", parent=video_games)
    Category.objects.create(name="Action", parent=genres, description="Fast-paced games that emphasize physical challenges, including hand-eye coordination and reaction-time.")
    Category.objects.create(name="Adventure", parent=genres, description="Immerse yourself in story-driven games that take you on epic journeys and thrilling quests.")
    Category.objects.create(name="RPG (Role-Playing Games)", parent=genres, description="Experience deep narratives, character development, and strategic gameplay in these immersive role-playing games.")
    Category.objects.create(name="Sports", parent=genres, description="Compete in your favorite sports with realistic simulations and exciting gameplay.")
    Category.objects.create(name="Racing", parent=genres, description="Get behind the wheel and experience the thrill of high-speed racing in various styles and environments.")
    Category.objects.create(name="Strategy", parent=genres, description="Test your tactical skills and strategic thinking in games that challenge your decision-making abilities.")
    Category.objects.create(name="Simulation", parent=genres, description="Experience detailed and realistic simulations that let you manage, build, or explore different worlds.")
    Category.objects.create(name="Puzzle", parent=genres, description="Challenge your mind with games that require logic, pattern recognition, and problem-solving skills.")
    Category.objects.create(name="Fighting", parent=genres, description="Engage in intense one-on-one combat with a variety of characters and fighting styles.")
    Category.objects.create(name="Horror", parent=genres, description="Experience the thrill of fear with games that offer suspenseful, terrifying, and atmospheric experiences.")

    platforms = Category.objects.create(name="Platforms", parent=video_games)
    Category.objects.create(name="PlayStation", parent=platforms, description="Explore the extensive library of games available for PlayStation consoles, from the latest hits to timeless classics.")
    Category.objects.create(name="Xbox", parent=platforms, description="Discover the best games for Xbox consoles, including exclusives, multi-platform titles, and Game Pass favorites.")
    Category.objects.create(name="Nintendo", parent=platforms, description="Dive into the world of Nintendo with games for the Switch, Wii U, and classic consoles.")
    Category.objects.create(name="PC", parent=platforms, description="Find a wide range of PC games, from indie gems to AAA titles, compatible with various gaming setups.")
    Category.objects.create(name="Mobile", parent=platforms, description="Enjoy gaming on the go with popular titles and innovative games designed for mobile devices.")

    # Accessories
    accessories = Category.objects.create(name="Accessories")

    controllers = Category.objects.create(name="Controllers", parent=accessories)
    Category.objects.create(name="Wireless Controllers", parent=controllers, description="Experience the freedom of wireless gaming with high-quality controllers designed for comfort and precision.")
    Category.objects.create(name="Wired Controllers", parent=controllers, description="Reliable and responsive wired controllers that ensure uninterrupted gameplay.")
    Category.objects.create(name="Custom Controllers", parent=controllers, description="Personalize your gaming experience with custom controllers that offer unique designs and features.")

    headsets = Category.objects.create(name="Headsets", parent=accessories)
    Category.objects.create(name="Wired Headsets", parent=headsets, description="Immerse yourself in the game with high-quality wired headsets that deliver crystal-clear audio.")
    Category.objects.create(name="Wireless Headsets", parent=headsets, description="Enjoy the convenience of wireless headsets with superior sound quality and comfort.")
    Category.objects.create(name="Gaming Earbuds", parent=headsets, description="Compact and lightweight gaming earbuds for on-the-go audio without compromising on quality.")

    storage = Category.objects.create(name="Storage", parent=accessories)
    Category.objects.create(name="External Hard Drives", parent=storage, description="Expand your storage capacity with reliable external hard drives for all your gaming needs.")
    Category.objects.create(name="Memory Cards", parent=storage, description="Increase your storage space with high-speed memory cards compatible with various gaming devices.")
    Category.objects.create(name="SSDs", parent=storage, description="Boost your system's performance with fast and efficient solid-state drives.")

    chargers_and_cables = Category.objects.create(name="Chargers and Cables", parent=accessories)
    Category.objects.create(name="Charging Docks", parent=chargers_and_cables, description="Keep your controllers charged and ready with convenient charging docks.")
    Category.objects.create(name="USB Cables", parent=chargers_and_cables, description="High-quality USB cables for charging and data transfer, compatible with a wide range of devices.")
    Category.objects.create(name="HDMI Cables", parent=chargers_and_cables, description="Experience high-definition gaming with durable and reliable HDMI cables.")

    stands_and_mounts = Category.objects.create(name="Stands and Mounts", parent=accessories)
    Category.objects.create(name="Console Stands", parent=stands_and_mounts, description="Organize and display your consoles with sturdy and stylish stands.")
    Category.objects.create(name="Wall Mounts", parent=stands_and_mounts, description="Save space and enhance your setup with secure wall mounts for your gaming devices.")

    vr_accessories = Category.objects.create(name="VR Accessories", parent=accessories)
    Category.objects.create(name="VR Headsets", parent=vr_accessories, description="Dive into virtual reality with cutting-edge VR headsets that offer immersive experiences.")
    Category.objects.create(name="VR Controllers", parent=vr_accessories, description="Enhance your VR gameplay with precise and responsive VR controllers.")

if __name__ == '__main__':
    populate_categories()
