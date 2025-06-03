# Generate detailed recommendations and CSV output
def generate_personalized_recommendations(elemental_scores, detailed_breakdown, flow_progression):
    """
    Generates personalized recommendations based on elemental scores
    """
    recommendations = []
    
    # General recommendations based on consciousness level
    phase = flow_progression['phase']
    if phase == 5:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Focus on sharing wisdom and guiding others',
            'practices': 'Teaching, Mentoring, Creating spiritual content'
        })
    elif phase == 4:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Integrate all elements into daily practice',
            'practices': 'Daily meditation, Elemental balancing rituals'
        })
    elif phase == 3:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Deepen spiritual study and practice',
            'practices': 'Advanced meditation, Sacred geometry study'
        })
    elif phase == 2:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Establish consistent spiritual routine',
            'practices': 'Daily chakra meditation, Basic energy work'
        })
    else:
        recommendations.append({
            'type': 'General',
            'priority': 'High',
            'recommendation': 'Begin with fundamental chakra balancing',
            'practices': 'Root chakra grounding, Basic breathing exercises'
        })
    
    # Element-specific recommendations
    element_practices = {
        'Air': ['Pranayama breathing', 'Merkaba meditation', 'Mental clarity exercises'],
        'Earth': ['Grounding meditation', 'Crystal healing', 'Nature connection'],
        'Fire': ['Kundalini yoga', 'Transformation rituals', 'Solar meditation'],
        'Water': ['Emotional healing', 'Moon meditation', 'Flow practices'],
        'Spirit': ['Unity consciousness', 'Divine connection', 'Sacred geometry study']
    }
    
    # Find elements that need improvement (below average)
    average_score = flow_progression['average_score']
    for element, score in elemental_scores.items():
        if score < average_score:
            recommendations.append({
                'type': 'Elemental',
                'priority': 'Medium' if score > average_score * 0.8 else 'High',
                'recommendation': f'Strengthen {element} element energy',
                'practices': ', '.join(element_practices[element]),
                'current_score': score,
                'target_improvement': '15-20 points'
            })
    
    return recommendations

# Generate recommendations
recommendations = generate_personalized_recommendations(elemental_scores, detailed_breakdown, flow_progression)

# Create detailed data for CSV export
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

# Convert to DataFrame and save as CSV
df_detailed = pd.DataFrame(detailed_data)
df_recommendations = pd.DataFrame(recommendations)

# Save files
df_detailed.to_csv('awaken_consciousness_detailed_scores.csv', index=False)
df_recommendations.to_csv('awaken_consciousness_recommendations.csv', index=False)

print("📋 DETAILED BREAKDOWN")
print("=" * 30)
print(df_detailed.groupby('Element')['Weighted_Score'].sum().round(2))

print(f"\n🎯 PERSONALIZED RECOMMENDATIONS")
print("=" * 35)
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec['recommendation']}")
    print(f"   Priority: {rec['priority']}")
    print(f"   Practices: {rec['practices']}")
    if 'current_score' in rec:
        print(f"   Current score: {rec['current_score']:.1f}")
    print()

print("✅ CSV files generated:")
print("- awaken_consciousness_detailed_scores.csv")
print("- awaken_consciousness_recommendations.csv") 