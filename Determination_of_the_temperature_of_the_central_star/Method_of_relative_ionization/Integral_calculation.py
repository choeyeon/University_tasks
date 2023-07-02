from scipy import integrate
import numpy as np

def calculate_integral(T_star):
    def integrand(x, T):
        numerator = 2.45 * x**0 - (2.45 - 1) * x**(-1)
        denominator = np.exp(35.146 / (k * T) * x) - 1
        return numerator / denominator

    def denominator_integrand(x, T):
        return x**(-3+2) / (np.exp(54.403 / (k * T) * x) - 1)

    def integral(T):
        return integrate.quad(integrand, 1, np.inf, args=(T,))[0]

    def denominator_integral(T):
        return integrate.quad(denominator_integrand, 1, np.inf, args=(T,))[0]

    # The value of constant Boltzmann k 
    k = 1.380649e-23

    result = integral(T_star) / denominator_integral(T_star)
    return result