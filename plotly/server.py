from flask import Flask, make_response, render_template, request, jsonify

import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot')
def plot():
    fig = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with the 'svg' Renderer"
    )

    svg = fig.to_image(format="svg", engine="kaleido")

    # render as svg image, and set headers accoridingly
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response

@app.route('/plot2')
def plot2():
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    svg = fig.to_image(format="svg", engine="kaleido")

    # render as svg image, and set headers accoridingly
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


@app.route('/plot3')
def plot3():
    df = px.data.gapminder()

    fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
    
    svg = fig.to_image(format="svg", engine="kaleido")

    # render as svg image, and set headers accoridingly
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


if __name__ == '__main__':
    app.run(debug=True)