from flask import Flask, make_response, render_template

# import für plotly
import plotly.graph_objects as go

# import für Matplotlib
import matplotlib.pyplot as plt
import io

app = Flask('chartapp')

@app.route('/')
def index():
    return render_template('index.html')

#
@app.route('/plot')
def plot():
    """
    Create a plot with Plotly.
    """
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    fig = go.Figure(data=go.Scatter(x=x, y=y))
    svg = fig.to_image(format='svg', engine='kaleido')
    
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response

@app.route('/plot2')
def plot2():
    """
    Create a plot with matplotlib.
    """
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    fig = plt.Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x,y)

    output = io.BytesIO()
    fig.savefig(output, format='png')

    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


app.run(debug=True)