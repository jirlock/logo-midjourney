import random
import pyperclip

# Word lists for each category
TYPE = [
    "Wordmark", "Letter mark", "Combination mark", "Letterform", "Pictorial mark",
    "Abstract mark", "Mascot", "Emblem", "Responsive", "Animated", "Shape-shifting",
    "Negative space", "Minimalist", "Vintage/retro", "Hand-drawn", "Geometric",
    "3D", "Flat design", "Gradient", "Tech", "Food and beverage", "Corporate",
    "Entertainment", "Sports", "Luxury", "Educational", "Circular", "Horizontal",
    "Vertical", "Grid-based", "Asymmetrical", "Modular", "Monochromatic",
    "Duotone", "Multi-colored", "Black and white", "Color-changing"
]

ARTISTIC_GENRE = [
    "Abstract", "Abstract Expressionism", "Academic Art", "Action Painting",
    "Art Deco", "Art Nouveau", "Avant-garde", "Baroque", "Bauhaus",
    "Biomechanical Art", "Byzantine Art", "Classicism", "Color Field",
    "Conceptual Art", "Constructivism", "Cubism", "Dada", "Dark Art",
    "De Stijl", "Digital Art", "Expressionism", "Fauvism", "Folk Art",
    "Futurism", "Gothic", "Graffiti", "Impressionism", "Installation Art",
    "Kinetic Art", "Land Art", "Mannerism", "Maximalism", "Minimalism",
    "Modern Art", "Naive Art", "Neo-classicism", "Neo-expressionism", "Op Art",
    "Performance Art", "Photo-realism", "Pop Art", "Post-impressionism",
    "Precisionism", "Primitive Art", "Realism", "Renaissance", "Rococo",
    "Romanticism", "Social Realism", "Street Art", "Suprematism", "Surrealism",
    "Symbolism", "Tachisme", "Traditional Art", "Urban Art", "Video Art",
    "Vorticism"
]

ARTISTIC_TECHNIQUE = [
    "Acrylic Pouring", "Airbrush", "Alla Prima", "Assemblage", "Batik",
    "Blending", "Block Printing", "Brush Hatching", "Burnishing", "Calligraphy",
    "Chiaroscuro", "Collage", "Color Blocking", "Color Washing", "Contour Drawing",
    "Cross-hatching", "Decalcomania", "Decoupage", "Doodling", "Dot Work",
    "Dripping", "Dry Brush", "Embossing", "Encaustic", "Engraving", "Etching",
    "Finger Painting", "Foreshortening", "Fresco", "Frottage", "Glazing",
    "Gouache", "Granulation", "Grattage", "Gridding", "Grisaille",
    "Hands-Off Painting", "Hatching", "Impasto", "Intaglio", "Layering",
    "Linocut", "Lithography", "Marbling", "Masking", "Mixed Media", "Modeling",
    "Monotype", "Mosaics", "Oil Painting", "Outline", "Palette Knife",
    "Paper Cutting", "Pastels", "Pencil Shading", "Perspective Drawing",
    "Pointillism", "Relief Printing", "Reverse Glass Painting", "Sanding",
    "Sgraffito", "Silk Screening", "Silverpoint", "Splattering", "Spray Painting",
    "Stamping", "Stippling", "Stenciling", "Subtractive Drawing", "Tempera",
    "Tenebrism", "Texture Mapping", "Trompe l'oeil", "Underpainting", "Wash",
    "Watercolor", "Wet-on-Wet", "Woodcut", "Zentangle"
]

DESIGNER = [
    "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet",
    "Salvador Dalí", "Frida Kahlo", "Georgia O'Keeffe", "Andy Warhol",
    "Rembrandt", "Michelangelo", "Gustav Klimt", "Henri Matisse",
    "Jackson Pollock", "Jean-Michel Basquiat", "Wassily Kandinsky",
    "Keith Haring", "Yayoi Kusama", "David Hockney", "Marina Abramović",
    "Paul Rand", "Saul Bass", "Milton Glaser", "Stefan Sagmeister",
    "Paula Scher", "Chip Kidd", "Massimo Vignelli", "David Carson",
    "Neville Brody", "Jessica Walsh", "Michael Bierut", "Peter Saville",
    "April Greiman", "Herb Lubalin", "Alan Fletcher"
]

EXCLUSION = [
    "shading detail", "photorealistic details", "text", "realistic details"
]

def generate_prompt():
    """Generate a random Midjourney logo prompt."""
    #prompt = "/imagine a {Type} logo of a {Name}, {ArtisticGenre}, {ArtisticTechnique} by {Designer} --no {Exclusion}"
    prompt = "a {type} logo of {name}, {artisticGenre}, {artisticTechnique}, designed by {designer} --no photorealistic details, text, shading details, realistic details --stylize {stylize} --weird {weirdness} --chaos {variety}"
    
    # Replace placeholders with random selections
    formatted_prompt = prompt.format(
        type=random.choice(TYPE),
        name="CMDX",
        artisticGenre=random.choice(ARTISTIC_GENRE),
        artisticTechnique=random.choice(ARTISTIC_TECHNIQUE),
        designer=random.choice(DESIGNER),
        #exclusion=random.choice(EXCLUSION),
        #stylize = random.randint(0, 1000),
        stylize = 0,
        #weirdness = random.randint(0, 3000),
        weirdness = 0,
        #variety = random.randint(0,100)
        variety = 0
    )
    
    return formatted_prompt

def count_var():
    return len(TYPE) * len(ARTISTIC_GENRE) * len(ARTISTIC_TECHNIQUE)* len(DESIGNER)

def main():
    # Generate and print a random prompt
    prompt = generate_prompt()
    #print("\nGenerated Midjourney Prompt:")
    print(prompt)
    pyperclip.copy(prompt)

if __name__ == "__main__":
    main()