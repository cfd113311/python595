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

from montecarlo import 2DNumericalIntegrator

import math

if __name__ == "__main__":
    numerical_integrator = 2DNumercalIntegrator()

   numerical_integrator.set_objective( math.sin) # set objective function to evaluate.

    numerical_integrator.set_scenarios(1000) # use this many draws.

    lower_bound = 0.0
    upper_bound = 2 * math.pi
    print("first result", numerical_integrator.integrate( lower_bound, upper_bound))

    upper_bound = 1.0
    print("second result", numerical_integrator.integrate( lower_bound, upper_bound))



