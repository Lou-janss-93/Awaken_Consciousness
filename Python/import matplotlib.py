import matplotlib.pyplot as plt
import numpy as np
import json

# Load the project data
with open('awaken_consciousness_project_data.json', 'r', encoding='utf-8') as f:
    project_data = json.load(f)

# Create a consciousness development progression chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Awaken Consciousness Project: Spirituele Ontwikkeling Roadmap', fontsize=16, fontweight='bold')

# Chart 1: Phase and Color Progression
phases = ['Fase 1\n(Wit)', 'Fase 2\n(Subtiele hints)', 'Fase 3\n(Pastel)', 'Fase 4\n(Diepe tinten)', 'Fase 5\n(Felle kleuren)']
color_intensity = [0.1, 0.3, 0.5, 0.7, 1.0]
colors = ['#f0f0f0', '#e6e6fa', '#dda0dd', '#9370db', '#4b0082']

bars1 = ax1.bar(phases, color_intensity, color=colors, alpha=0.8, edgecolor='navy', linewidth=2)
ax1.set_title('Kleur Intensiteit Progressie per Fase', fontsize=14, fontweight='bold')
ax1.set_ylabel('Bewustzijns Intensiteit', fontsize=12)
ax1.set_ylim(0, 1.2)

# Add value labels on bars
for bar, intensity in zip(bars1, color_intensity):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.02,
             f'{intensity*100:.0f}%', ha='center', va='bottom', fontweight='bold')

# Chart 2: Element Distribution and Symbolism
elements = ['Air\n(Lucht)', 'Earth\n(Aarde)', 'Fire\n(Vuur)', 'Water', 'Universe\n(Universum)']
element_colors = ['#AEEFFF', '#2E7D32', '#FF6F00', '#1976D2', '#6C2EB6']
symbol_counts = [11, 10, 9, 8, 8]  # Approximate symbol counts per category

bars2 = ax2.bar(elements, symbol_counts, color=element_colors, alpha=0.8, edgecolor='darkgray', linewidth=2)
ax2.set_title('Elementen en Symboliek Verdeling', fontsize=14, fontweight='bold')
ax2.set_ylabel('Aantal Symbolen', fontsize=12)

# Add value labels on bars
for bar, count in zip(bars2, symbol_counts):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             str(count), ha='center', va='bottom', fontweight='bold')

# Style improvements
for ax in [ax1, ax2]:
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#fafafa')

plt.tight_layout()
plt.savefig('consciousness_development_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

# Create a symbol category progression table
print("\n=== SYMBOL CATEGORIEËN PROGRESSIE ===")
print("Van Simpel naar Complex Bewustzijn:\n")

categories = [
    ("1. Simple Universal", "Universele basis symbolen", "Dot, Circle, Triangle, Sun"),
    ("2. Natural Geometric", "Natuurlijke geometrie", "Spiral, Lotus, Tree of Life"),
    ("3. Complex Spiritual", "Spirituele complexiteit", "Yin Yang, Mandala, Hexagram"),
    ("4. Esoteric Advanced", "Esoterische diepte", "Merkaba, Ouroboros, Sri Yantra")
]

for i, (category, description, examples) in enumerate(categories, 1):
    print(f"{category}")
    print(f"   Beschrijving: {description}")
    print(f"   Voorbeelden: {examples}")
    print()

# Create technical implementation overview
print("=== TECHNISCHE IMPLEMENTATIE ===")
tech_stack = project_data['project_overview']['technology_stack']
print(f"Frontend: {', '.join(tech_stack['frontend'])}")
print(f"Features: {', '.join(tech_stack['features'])}")
print(f"Responsive: {'Ja' if tech_stack['responsive'] else 'Nee'}")
print(f"Accessibility: {tech_stack['accessibility']}")