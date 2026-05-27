"""
automotive_visualizations.py
=============================
Critical Data Visualizations for the Automotive Industry
Author: Mahesh Mandalapu | Senior Data Engineer
Dataset: Synthetic example data (mirrors real-world patterns)

Charts included:
  1. EV vs ICE Vehicle Sales Trends (2015-2024) - Line/Area Chart
  2. Top 10 Manufacturers by Market Share - Horizontal Bar Chart
  3. Fuel Efficiency by Vehicle Segment - Box Plot
  4. Vehicle Recall Frequency Heatmap - Heatmap
  5. EV Adoption Rate by State - Choropleth Map
  6. Production Volume vs Supply Chain Disruptions - Dual-axis Line
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ─── Color palette ────────────────────────────────────────────────────────────
COLORS = {
    'ev':      '#00C896',
    'ice':     '#FF6B6B',
    'hybrid':  '#FFD93D',
    'primary': '#2C3E50',
    'accent':  '#3498DB',
    'bg':      '#F8F9FA',
}
sns.set_theme(style='whitegrid', palette='muted')

# ─── 1. GENERATE DATASETS ─────────────────────────────────────────────────────

def generate_ev_sales_data():
    """EV vs ICE vehicle sales 2015–2024 (US market, in thousands)"""
    years = list(range(2015, 2025))
    np.random.seed(42)
    ev_sales    = [71, 159, 199, 362, 326, 296, 652, 918, 1189, 1560]
    ice_sales   = [17200, 17500, 17100, 17200, 16900, 14500, 15400, 13700, 14200, 15100]
    hybrid_sales = [450, 520, 610, 740, 860, 890, 1100, 1350, 1620, 1870]
    return pd.DataFrame({'year': years, 'EV': ev_sales, 'ICE': ice_sales, 'Hybrid': hybrid_sales})

def generate_manufacturer_data():
    """Market share by top 10 manufacturers"""
    makers = ['Toyota', 'Ford', 'GM', 'Stellantis', 'Honda', 'Tesla', 'Hyundai', 'Volkswagen', 'Nissan', 'Subaru']
    shares = [14.2, 13.1, 12.7, 11.4, 8.6, 7.2, 6.8, 5.1, 4.9, 3.8]
    evs    = [1.1, 2.3, 3.8, 0.9, 1.2, 100.0, 8.4, 12.1, 2.7, 0.3]
    return pd.DataFrame({'manufacturer': makers, 'market_share': shares, 'ev_pct': evs})

def generate_fuel_efficiency_data():
    """MPG by vehicle segment"""
    np.random.seed(0)
    segments = ['Compact', 'Midsize', 'SUV', 'Truck', 'Luxury', 'Sports', 'Minivan']
    data = []
    params = {'Compact':   (32, 4), 'Midsize':  (28, 3.5), 'SUV':     (24, 4.5),
              'Truck':     (19, 3),  'Luxury':   (25, 5),   'Sports':  (22, 6), 'Minivan': (23, 3)}
    for seg, (mu, sd) in params.items():
        mpg = np.random.normal(mu, sd, 120)
        data.extend([{'segment': seg, 'mpg': m} for m in mpg])
    return pd.DataFrame(data)

def generate_recall_data():
    """Vehicle recalls by make and category"""
    makes    = ['Ford', 'GM', 'Toyota', 'Honda', 'Chrysler', 'Nissan', 'BMW', 'Mercedes']
    categories = ['Airbag', 'Brakes', 'Engine', 'Electrical', 'Steering', 'Fuel System']
    np.random.seed(7)
    matrix = np.random.randint(5, 80, size=(len(makes), len(categories)))
    matrix[0, 0] = 95; matrix[1, 2] = 88; matrix[2, 1] = 72
    return pd.DataFrame(matrix, index=makes, columns=categories)

def generate_production_data():
    """Monthly production volume vs supply chain disruption index"""
    months = pd.date_range('2019-01', '2024-12', freq='MS')
    np.random.seed(3)
    base = 1400 + np.random.normal(0, 50, len(months))
    covid_dip   = np.exp(-0.5 * ((np.arange(len(months)) - 14) / 4) ** 2) * -600
    chip_dip    = np.exp(-0.5 * ((np.arange(len(months)) - 28) / 8) ** 2) * -380
    recovery    = np.linspace(0, 180, len(months))
    production  = np.clip(base + covid_dip + chip_dip + recovery, 600, 1800)
    disruption  = np.clip(20 + np.abs(covid_dip + chip_dip) / 30 + np.random.normal(0, 5, len(months)), 5, 95)
    return pd.DataFrame({'month': months, 'production_k': production, 'disruption_idx': disruption})

def generate_ev_state_data():
    """EV adoption rate (%) by US state"""
    states = {
        'California': 22.4, 'Washington': 14.1, 'Oregon': 11.8, 'New York': 9.2,
        'New Jersey': 8.7,  'Massachusetts': 8.4, 'Colorado': 7.9, 'Nevada': 7.1,
        'Florida': 5.8, 'Texas': 5.2, 'Illinois': 4.9, 'Georgia': 4.6,
        'Virginia': 4.4, 'Maryland': 4.1, 'Minnesota': 3.8, 'Arizona': 3.5,
        'Michigan': 3.1, 'Ohio': 2.8, 'Pennsylvania': 2.6, 'North Carolina': 2.4,
        'Wisconsin': 2.1, 'Missouri': 1.8, 'Indiana': 1.6, 'Tennessee': 1.5,
        'Alabama': 1.2, 'Mississippi': 0.9, 'Wyoming': 0.7, 'West Virginia': 0.6,
    }
    return pd.DataFrame({'state': list(states.keys()), 'ev_adoption_pct': list(states.values())})

# ─── 2. CHART 1: EV vs ICE Sales Trends ──────────────────────────────────────

def plot_ev_vs_ice_sales():
    df = generate_ev_sales_data()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.fill_between(df['year'], df['ICE'],  alpha=0.25, color=COLORS['ice'],    label='ICE (Internal Combustion)')
    ax.fill_between(df['year'], df['EV'],   alpha=0.55, color=COLORS['ev'],     label='Electric Vehicles (EV)')
    ax.fill_between(df['year'], df['Hybrid'], alpha=0.35, color=COLORS['hybrid'], label='Hybrid')
    ax.plot(df['year'], df['ICE'],   color=COLORS['ice'],    linewidth=2.5, marker='o', markersize=6)
    ax.plot(df['year'], df['EV'],    color=COLORS['ev'],     linewidth=2.5, marker='s', markersize=7)
    ax.plot(df['year'], df['Hybrid'], color=COLORS['hybrid'], linewidth=2.5, marker='^', markersize=6)
    ax.set_title('🚗  US Vehicle Sales Trends: EV vs ICE vs Hybrid (2015–2024)', fontsize=15, fontweight='bold', pad=15)
    ax.set_xlabel('Year', fontsize=12); ax.set_ylabel('Sales Volume (thousands)', fontsize=12)
    ax.set_xticks(df['year']); ax.legend(fontsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}k'))
    # Annotate EV growth
    ax.annotate('EV: 8× growth\n(2015→2024)', xy=(2024, 1560), xytext=(2021, 1200),
                arrowprops=dict(arrowstyle='->', color='green'), fontsize=10, color='green', fontweight='bold')
    plt.tight_layout()
    plt.savefig('automotive/ev_vs_ice_sales.png', dpi=150, bbox_inches='tight')
    print("✅  Chart 1 saved: automotive/ev_vs_ice_sales.png")
    plt.show()

# ─── 3. CHART 2: Manufacturer Market Share ───────────────────────────────────

def plot_manufacturer_market_share():
    df = generate_manufacturer_data().sort_values('market_share')
    colors = [COLORS['ev'] if ev > 50 else COLORS['accent'] for ev in df['ev_pct']]
    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(df['manufacturer'], df['market_share'], color=colors, edgecolor='white', linewidth=0.8, height=0.65)
    for bar, val, ev in zip(bars, df['market_share'], df['ev_pct']):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f'{val}%  (EV: {ev:.0f}%)', va='center', fontsize=10)
    ax.set_title('🏭  Top 10 Auto Manufacturers — US Market Share (2024)', fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Market Share (%)', fontsize=12); ax.set_xlim(0, 19)
    ax.axvline(df['market_share'].mean(), color='red', linestyle='--', alpha=0.6, label=f'Avg: {df["market_share"].mean():.1f}%')
    ax.legend(fontsize=10)
    from matplotlib.patches import Patch
    legend_els = [Patch(facecolor=COLORS['ev'], label='EV-dominant'), Patch(facecolor=COLORS['accent'], label='Traditional')]
    ax.legend(handles=legend_els, loc='lower right', fontsize=10)
    plt.tight_layout()
    plt.savefig('automotive/manufacturer_market_share.png', dpi=150, bbox_inches='tight')
    print("✅  Chart 2 saved: automotive/manufacturer_market_share.png")
    plt.show()

# ─── 4. CHART 3: Fuel Efficiency Box Plot ────────────────────────────────────

def plot_fuel_efficiency():
    df = generate_fuel_efficiency_data()
    order = df.groupby('segment')['mpg'].median().sort_values(ascending=False).index
    fig, ax = plt.subplots(figsize=(13, 7))
    palette = sns.color_palette('Set2', n_colors=len(order))
    sns.boxplot(data=df, x='segment', y='mpg', order=order, palette=palette,
                width=0.55, flierprops=dict(marker='o', markersize=4, alpha=0.5), ax=ax)
    sns.stripplot(data=df, x='segment', y='mpg', order=order,
                  color='black', alpha=0.12, size=3, jitter=True, ax=ax)
    medians = df.groupby('segment')['mpg'].median()
    for i, seg in enumerate(order):
        ax.text(i, medians[seg] + 0.8, f'{medians[seg]:.1f}', ha='center', fontsize=9, fontweight='bold', color='darkred')
    ax.axhline(df['mpg'].mean(), color='red', linestyle='--', alpha=0.7, label=f'Overall avg: {df["mpg"].mean():.1f} MPG')
    ax.set_title('⛽  Fuel Efficiency (MPG) Distribution by Vehicle Segment', fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Vehicle Segment', fontsize=12); ax.set_ylabel('Fuel Efficiency (MPG)', fontsize=12)
    ax.legend(fontsize=11); plt.tight_layout()
    plt.savefig('automotive/fuel_efficiency_boxplot.png', dpi=150, bbox_inches='tight')
    print("✅  Chart 3 saved: automotive/fuel_efficiency_boxplot.png")
    plt.show()

# ─── 5. CHART 4: Recall Heatmap ──────────────────────────────────────────────

def plot_recall_heatmap():
    df = generate_recall_data()
    fig, ax = plt.subplots(figsize=(11, 7))
    sns.heatmap(df, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5,
                linecolor='white', cbar_kws={'label': 'Recall Count'}, ax=ax)
    ax.set_title('🔧  Vehicle Recall Frequency by Make & Component Category', fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Recall Category', fontsize=12); ax.set_ylabel('Manufacturer', fontsize=12)
    ax.tick_params(axis='x', rotation=30); ax.tick_params(axis='y', rotation=0)
    plt.tight_layout()
    plt.savefig('automotive/recall_heatmap.png', dpi=150, bbox_inches='tight')
    print("✅  Chart 4 saved: automotive/recall_heatmap.png")
    plt.show()

# ─── 6. CHART 5: Production vs Supply Chain (Interactive Plotly) ──────────────

def plot_production_supply_chain():
    df = generate_production_data()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['month'], y=df['production_k'], name='Production Volume (k units)',
                             fill='tozeroy', fillcolor='rgba(52,152,219,0.15)',
                             line=dict(color='#3498DB', width=2.5)), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['month'], y=df['disruption_idx'], name='Supply Chain Disruption Index',
                             line=dict(color='#E74C3C', width=2, dash='dot'),
                             mode='lines+markers', marker=dict(size=4)), secondary_y=True)
    # Annotations
    fig.add_vrect(x0='2020-03', x1='2020-12', fillcolor='red', opacity=0.07, annotation_text='COVID-19 Shutdown')
    fig.add_vrect(x0='2021-06', x1='2022-06', fillcolor='orange', opacity=0.07, annotation_text='Chip Shortage')
    fig.update_layout(title='🏭  Auto Production Volume vs Supply Chain Disruption Index (2019–2024)',
                      xaxis_title='Month', hovermode='x unified',
                      legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                      template='plotly_white', height=500)
    fig.update_yaxes(title_text='Production Volume (thousands)', secondary_y=False)
    fig.update_yaxes(title_text='Disruption Index (0–100)', secondary_y=True)
    fig.write_html('automotive/production_supply_chain.html')
    print("✅  Chart 5 saved: automotive/production_supply_chain.html  (Interactive)")
    fig.show()

# ─── 7. CHART 6: EV Adoption Choropleth ─────────────────────────────────────

def plot_ev_adoption_map():
    df = generate_ev_state_data()
    state_abbrev = {
        'California':'CA','Washington':'WA','Oregon':'OR','New York':'NY','New Jersey':'NJ',
        'Massachusetts':'MA','Colorado':'CO','Nevada':'NV','Florida':'FL','Texas':'TX',
        'Illinois':'IL','Georgia':'GA','Virginia':'VA','Maryland':'MD','Minnesota':'MN',
        'Arizona':'AZ','Michigan':'MI','Ohio':'OH','Pennsylvania':'PA','North Carolina':'NC',
        'Wisconsin':'WI','Missouri':'MO','Indiana':'IN','Tennessee':'TN','Alabama':'AL',
        'Mississippi':'MS','Wyoming':'WY','West Virginia':'WV',
    }
    df['code'] = df['state'].map(state_abbrev)
    fig = px.choropleth(df, locations='code', locationmode='USA-states',
                        color='ev_adoption_pct', scope='usa',
                        color_continuous_scale='Teal',
                        labels={'ev_adoption_pct': 'EV Adoption (%)'},
                        title='🗺️  EV Adoption Rate by US State (2024)',
                        hover_name='state', hover_data={'ev_adoption_pct': ':.1f'})
    fig.update_layout(template='plotly_white', coloraxis_colorbar=dict(title='EV Adoption %'))
    fig.write_html('automotive/ev_adoption_map.html')
    print("✅  Chart 6 saved: automotive/ev_adoption_map.html  (Interactive)")
    fig.show()

# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('automotive', exist_ok=True)
    print("\n🚗  AUTOMOTIVE INDUSTRY — DATA VISUALIZATIONS")
    print("=" * 55)
    plot_ev_vs_ice_sales()
    plot_manufacturer_market_share()
    plot_fuel_efficiency()
    plot_recall_heatmap()
    plot_production_supply_chain()
    plot_ev_adoption_map()
    print("\n✅  All automotive visualizations generated successfully!")
