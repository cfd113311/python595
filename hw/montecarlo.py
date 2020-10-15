import random

class NumericalIntegrator(object):

    def __init__(self):
        self.objective = None
        self.scenarios = None

    def set_objective(self, func):
        """
        Accepts a callable func, and stores it to
        be used as the integrand by the instance.

        func is checked to ensure that it accepts
        and returns floating point values.
        """
        if not callable(func):
            raise TypeError("The objective should be a callable" +
                            " that accepts and returns floats.")
        # This try block will catch any function that doesn't accept
        # and return floats. If it doesn't accept floats, then the
        # passing of a float will raise a TypeError. If it doesn't
        # return floats, then the conditional will raise an error
        try:
            if isinstance(func(random.random()), float):
                self.objective = func
            else:
                raise TypeError

        except TypeError:
            raise TypeError("The objective should be a callable" +
                            " that accepts and returns floats.")

    def set_scenarios(self, n):
        """
        Allows adjustment of the number of draws
        that will be evaluated when performing
        the integration.

        n must be an integer.
        """
        if isinstance(n, int):
            self.scenarios = n
        else:
            raise TypeError("Scenarios must be integer-valued.")

    def integrate(self, lower, upper):
        """
        Runs a Monte Carlo approximation to evaluate
        the integral of the objective function on
        the range [lower, upper), performing a total
        of `scenarios` draws.
        """
        avg = 0
        for n in range(self.scenarios):
            draw = random.uniform(lower, upper)
            val = self.objective(draw)
            avg = (val + n*avg)/(n+1)

        return avg * (upper-lower)
