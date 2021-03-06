# Making rain fall in a field so as to estimate pi.

This repo contains some code that simulates rain fall in a square field and counts the number of drops that fall in an inscribed circle so as to estimate pi.

![animation gif](img/animation.gif)

## Python Library Installation 
- Install Python 3.7 or above 
- Run the command prompt with admin privilege and install the Python package Poetry as follow: 
```bash
pip install poetry
```
- Restart the command prompt and cd to the repo directory 
- Install the required libraries by invoking poetry 
```bash
poetry install 
``` 
- Install poetry following instruction from above, then invoke the poetry shell  
```bash
poetry shell 
``` 
## Usage

#### Start simulation

```bash
python src\Estimate_pi.py 500
``` 
This returns:

    ----------------------
    500 drops
    pi estimated as:
        3.112
    ----------------------
#### Start animation
```bash
python src\animation.py localhost 8000
``` 
- You could then open a browser and see the animation at localhost:8000

#### Start Jupyter Notebook
```bash
cd src && jupyter notebook
``` 
- A notebook will launch automatically, click on estimate_pi_notebook.ipynb 
- If you want to quickly interact with a pre-built Jupyter Notebook, you can 
click [here](https://mybinder.org/v2/gh/jonathancychow/Monte_Carlo_Simulation_for_Estimating_pi/master?filepath=src%2Festimate_pi_notebook.ipynb), I have set it all up in MyBinder. 

#### Jupyter Notebook for youngster
- A trim down notebook is set up for youngster to learn more about Python and simulation, 
see this [link](https://mybinder.org/v2/gh/jonathancychow/Monte_Carlo_Simulation_for_Estimating_pi/master?filepath=src%2Festimate_pi_notebook_edu.ipynb)

![500 drops](img/500_drops.png)

If we have 10,000 drops we get:

![100,000 drops](img/10000_drops.png)

If we have 1,000,000 drops we get:

![1,000,000 drops](img/1000000_drops.png)

# License Information

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/us/) license.  You are free to:

* Share: copy, distribute, and transmit the work,
* Remix: adapt the work

Under the following conditions:

* Attribution: You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
* Share Alike: If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.

When attributing this work, please include me (but don't feel obliged to: I'd just be happy to know if anyone made use of it :) ).
