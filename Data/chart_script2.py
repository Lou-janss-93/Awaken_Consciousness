import plotly.graph_objects as go
import json

# Load the data
data = {"elements": {"Air": 112.2, "Earth": 75.8, "Fire": 76.3, "Water": 106.6, "Spirit": 149.0}, "average_score": 104.0, "phase": "Phase 5: Mastery - Unified Consciousness", "max_scale": 150}

# Extract elements and scores
elements = list(data["elements"].keys())
scores = list(data["elements"].values())

# Add the first element at the end to close the radar chart
elements_closed = elements + [elements[0]]
scores_closed = scores + [scores[0]]

# Create the radar chart
fig = go.Figure()

# Add the main data trace
fig.add_trace(go.Scatterpolar(
    r=scores_closed,
    theta=elements_closed,
    fill='toself',
    name='Elements',
    line=dict(color='#1FB8CD', width=3),
    fillcolor='rgba(31, 184, 205, 0.3)',
    hovertemplate='%{theta}: %{r:.1f}<extra></extra>'
))

# Add average score reference line (circle)
avg_scores = [data["average_score"]] * len(elements_closed)
fig.add_trace(go.Scatterpolar(
    r=avg_scores,
    theta=elements_closed,
    mode='lines',
    name='Avg (104.0)',
    line=dict(color='#FFC185', width=2, dash='dash'),
    hovertemplate='Average: %{r:.1f}<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Phase 5: Mastery Elements',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 150],
            tickvals=[30, 60, 90, 120, 150],
            ticktext=['30', '60', '90', '120', '150'],
            gridcolor='rgba(128, 128, 128, 0.3)',
            linecolor='rgba(128, 128, 128, 0.5)'
        ),
        angularaxis=dict(
            gridcolor='rgba(128, 128, 128, 0.3)',
            linecolor='rgba(128, 128, 128, 0.5)'
        )
    ),
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    ),
    showlegend=True
)

# Save the chart
fig.write_image('elemental_radar_chart.png')