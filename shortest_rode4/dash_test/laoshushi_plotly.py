from plotly.offline import init_notebook_mode, plot

init_notebook_mode(connected='True')

# 需要连线的点
nyc_london = [dict(
    type='scattergeo',
    lat=[40.7127, 51.5072],
    lon=[-74.0059, 0.1275],
    mode='lines',
    line=dict(
        width=2,
        color='blue',
    ),
)]

# 布局
layout = dict(
    title='London to NYC Great Circle',
    showlegend=False,
    geo=dict(
        resolution=50,
        showland=True,
        showlakes=True,
        landcolor='rgb(204, 204, 204)',
        countrycolor='rgb(204, 204, 204)',
        lakecolor='rgb(255, 255, 255)',
        projection=dict(type="equirectangular"),
        coastlinewidth=2,
        lataxis=dict(
            range=[20, 60],
            showgrid=True,
            tickmode="linear",
            dtick=10
        ),
        lonaxis=dict(
            range=[-100, 20],
            showgrid=True,
            tickmode="linear",
            dtick=20
        ),
    )
)

fig = dict(data=nyc_london, layout=layout)
plot(fig, validate=False, filename='d3-great-circle')