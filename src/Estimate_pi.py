#!/usr/bin/env python
from __future__ import division
from random import random
from math import pi
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import argparse

"""
Script to simulate rain in a square field. Counting the number of rain drops in the inscribed circle of radius equal to the length of the field. The ratio of the number of drops in the circle to the total number of drops gives $\pi$.
"""


def rain_drop(length_of_field=1):
    """
    Simulate a random rain drop
    """
    return [(.5 - random()) * length_of_field, (.5 - random()) * length_of_field]


def is_point_in_circle(point, length_of_field=1):
    """
    Return True if point is in inscribed circle
    """
    return (point[0]) ** 2 + (point[1]) ** 2 <= (length_of_field / 2) ** 2


def plot_rain_drops_matplotlib(drops_in_circle, drops_out_of_circle, length_of_field=1, format='pdf'):
    """ Function to draw rain drops """
    number_of_drops_in_circle = len(drops_in_circle)
    number_of_drops_out_of_circle = len(drops_out_of_circle)
    number_of_drops = number_of_drops_in_circle + number_of_drops_out_of_circle
    plt.figure()
    plt.xlim(-length_of_field / 2, length_of_field / 2)
    plt.ylim(-length_of_field / 2, length_of_field / 2)
    plt.scatter([e[0] for e in drops_in_circle], [e[1] for e in drops_in_circle], color='blue', label="Drops in circle")
    plt.scatter([e[0] for e in drops_out_of_circle], [e[1] for e in drops_out_of_circle], color='black', label="Drops out of circle")
    plt.legend(loc="center")
    plt.title("%s drops: %s landed in circle, estimating $\pi$ as %.4f." % (number_of_drops, number_of_drops_in_circle, 4 * number_of_drops_in_circle / number_of_drops))
    plt.savefig("%s_drops.%s" % (number_of_drops, format))


def plot_rain_drops_plotly(drops_in_circle, drops_out_of_circle, pi_estimate):
    """ Function to draw rain drops """
    number_of_drops_in_circle = len(drops_in_circle)
    number_of_drops_out_of_circle = len(drops_out_of_circle)
    number_of_drops = number_of_drops_in_circle + number_of_drops_out_of_circle
    fig = make_subplots(rows=2,
                        cols=1,
                        subplot_titles=('Drops landed in circule', 'Pi Estimate over iternation')
                        )
    fig.add_trace(go.Scatter(x=[e[0] for e in drops_in_circle],
                             y=[e[1] for e in drops_in_circle],
                             mode='markers',
                             name="In Circule"
                             ),
                  row=1,
                  col=1
                  )
    fig.add_trace(go.Scatter(x=[e[0] for e in drops_out_of_circle],
                             y=[e[1] for e in drops_out_of_circle],
                             mode='markers',
                             name="Out of Circule"
                             ),
                  row=1,
                  col=1
                  )
    fig.add_trace(go.Scatter(y=pi_estimate,
                             x=np.arange(1, number_of_drops + 1),
                             mode='lines',
                             name="Pi Estimate"
                             ),
                  row=2,
                  col=1
                  )
    fig.add_shape(type="line",
                  x0=0, y0=np.pi, x1=number_of_drops + 1, y1=np.pi,
                  line=dict(color="Red", width=1),
                  row=2,
                  col=1
                  )
    fig.update_layout(template="plotly_dark",
                      width=800,
                      height=800,
                      title="%s drops: %s landed in circle, estimating pi as %.4f." % (
                      number_of_drops, number_of_drops_in_circle, 4 * number_of_drops_in_circle / number_of_drops)
                      )
    fig.show()

def rain(number_of_drops=1000, vis='Web',length_of_field=1, plot=True, format='pdf', dynamic=0):
    """
    Function to make rain drops.
    """
    number_of_drops_in_circle = 0
    drops_in_circle = []
    drops_out_of_circle = []
    pi_estimate = []
    for k in range(number_of_drops):
        d = (rain_drop(length_of_field))
        if is_point_in_circle(d, length_of_field):
            drops_in_circle.append(d)
            number_of_drops_in_circle += 1
        else:
            drops_out_of_circle.append(d)
        if dynamic:  # The dynamic option if set to True will plot every new drop (this can be used to create animations of the simulation)
            print ("Plotting drop number: %s" % (k + 1))
            plot_rain_drops_matplotlib(drops_in_circle, drops_out_of_circle, length_of_field, format)
        pi_estimate.append(4 * number_of_drops_in_circle / (k + 1))  # This updates the list with the newest estimate for pi.
    # Plot the pi estimates
    plt.figure()
    plt.scatter(range(1, number_of_drops + 1), pi_estimate)
    max_x = plt.xlim()[1]
    plt.hlines(pi, 0, max_x, color='black')
    plt.xlim(0, max_x)
    plt.title("$\pi$ estimate against number of rain drops")
    plt.xlabel("Number of rain drops")
    plt.ylabel("$\pi$")
    plt.savefig("Pi_estimate_for_%s_drops_thrown.pdf" % number_of_drops)

    if plot and not dynamic:
        if vis == 'Save As':
            plot_rain_drops_matplotlib(drops_in_circle, drops_out_of_circle, length_of_field, format)
        else:
            plot_rain_drops_plotly(drops_in_circle, drops_out_of_circle, pi_estimate)

    return [number_of_drops_in_circle, number_of_drops]


if __name__ == "__main__":
    # Run the script from cli
    parser = argparse.ArgumentParser(description='Number of Drops.')
    parser.add_argument('Drops', type=int,
                        nargs='?',
                        default=100,
                        help='Number of Drops')
    parser.add_argument('Visualisation',
                        default='plotly',
                        nargs='?',
                        help='Visualisation Method - Web / Save As')
    parser.add_argument('Dynamic',
                        type=int,
                        default=0,
                        nargs='?',
                        help='Save pic after each iternation?  - 1 / 0')
    args = parser.parse_args()
    number_of_drops = args.Drops
    visualisation = args.Visualisation

    print("Number of Drops = %s" % number_of_drops)
    print("Visualisation Method - %s"% visualisation)
    print("Dynamic Visualisation - %s" % args.Dynamic)

    r = rain(number_of_drops, vis=visualisation, plot=True, format='png', dynamic=args.Dynamic, )
    # Print to screen:
    print ("----------------------")
    print ("%s drops" % number_of_drops)
    print ("pi estimated as:")
    print ("\t%s" % (4 * r[0] / r[1]))
    print ("----------------------")
