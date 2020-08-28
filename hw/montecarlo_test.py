# 30 pts.
#
# DO NOT CHANGE THE CONTENTS OF THIS FILE.
# 
# Montecarlo integration performs the following steps.
# 1. Evaluate function N times for random values in 
#   the domain.
# 2. Average the function value.
# 3. Integral value is average function value times
#   domain length.


from montecarlo import Engine, 2DNumericalIntegration

import math

# implementing these objects is the assessment for the Python module.

if __name__ == "__main__":
    engine = Engine() # default value draws from a uniform distribution

    # integrator takes an engine object.
    # engine has one method - draw(lower_bound, upper_bound)
    # it returns a random number between the two.
    # use the random module for this class.
    numerical_integrator = 2DNumercalIntegration( engine )

   numerical_integrator.set_objective( math.sin) # set objective function as sin

    numerical_integrator.set_scenarios(1000) # use this many iterations

    lower_bound = 0.0
    upper_bound = 2 * math.pi
    print("first result", numerical_integrator.integrate( lower_bound, upper_bound))

    upper_bound = 1.0
    print("second result", numerical_integrator.integrate( lower_bound, upper_bound))



