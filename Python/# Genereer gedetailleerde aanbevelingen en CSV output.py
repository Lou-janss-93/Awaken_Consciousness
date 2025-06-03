# Genereer gedetailleerde aanbevelingen en CSV output
def generate_personalized_recommendations(elemental_scores, detailed_breakdown, flow_progression):
    """
    Genereert persoonlijke aanbevelingen gebaseerd op elementaire scores
    """
    recommendations = []
    
    # Algemene aanbevelingen gebaseerd op bewustzijnsniveau
    phase = flow_progression['phase']
    if phase == 5:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Focus op het delen van wijsheid en het begeleiden van anderen',
            'practices': 'Teaching, Mentoring, Creating spiritual content'
        })
    elif phase == 4:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Integreer alle elementen in dagelijkse praktijk',
            'practices': 'Daily meditation, Elemental balancing rituals'
        })
    elif phase == 3:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Verdiep spirituele studie en praktijk',
            'practices': 'Advanced meditation, Sacred geometry study'
        })
    elif phase == 2:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Vestig consistente spirituele routine',
            'practices': 'Daily chakra meditation, Basic energy work'
        })
    else:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Begin met fundamentele chakra balancing',
            'practices': 'Root chakra grounding, Basic breathing exercises'
        })
    
    # Elementaire specifieke aanbevelingen
    element_practices = {
        'Air': ['Pranayama breathing', 'Merkaba meditation', 'Mental clarity exercises'],
        'Earth': ['Grounding meditation', 'Crystal healing', 'Nature connection'],
        'Fire': ['Kundalini yoga', 'Transformation rituals', 'Solar meditation'],
        'Water': ['Emotional healing', 'Moon meditation', 'Flow practices'],
        'Spirit': ['Unity consciousness', 'Divine connection', 'Sacred geometry study']
    }
    
    # Vind elementen die verbetering nodig hebben (onder gemiddelde)
    average_score = flow_progression['average_score']
    for element, score in elemental_scores.items():
        if score < average_score:
            recommendations.append({
                'type': 'Elemental',
                'priority': 'Medium' if score > average_score * 0.8 else 'High',
                'recommendation': f'Versterk {element} element energie',
                'practices': ', '.join(element_practices[element]),
                'current_score': score,
                'target_improvement': '15-20 punten'
            })
    
    return recommendations

# Genereer aanbevelingen
recommendations = generate_personalized_recommendations(elemental_scores, detailed_breakdown, flow_progression)

# Maak gedetailleerde data voor CSV export
detailed_data = []
for element, breakdown in detailed_breakdown.items():
    for item in breakdown:
        detailed_data.append({
            'Element': element,
            'Category': item['category'],
            'Subcategory': item['subcategory'],
            'Raw_Score': item['raw_score'],
            'Normalized_Score': item['normalized'],
            'Weighted_Score': item['weighted'],
            'Element_Total': round(elemental_scores[element], 2)
        })

# Converteer naar DataFrame en save als CSV
df_detailed = pd.DataFrame(detailed_data)
df_recommendations = pd.DataFrame(recommendations)

# Save files
df_detailed.to_csv('awaken_consciousness_detailed_scores.csv', index=False)
df_recommendations.to_csv('awaken_consciousness_recommendations.csv', index=False)

print("📋 GEDETAILLEERDE BREAKDOWN")
print("=" * 30)
print(df_detailed.groupby('Element')['Weighted_Score'].sum().round(2))

print(f"\n🎯 PERSOONLIJKE AANBEVELINGEN")
print("=" * 35)
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec['recommendation']}")
    print(f"   Prioriteit: {rec['priority']}")
    print(f"   Praktijken: {rec['practices']}")
    if 'current_score' in rec:
        print(f"   Huidige score: {rec['current_score']:.1f}")
    print()

print("✅ CSV bestanden gegenereerd:")
print("- awaken_consciousness_detailed_scores.csv")
print("- awaken_consciousness_recommendations.csv")