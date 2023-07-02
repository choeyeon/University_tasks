from scipy.integrate import quad

def integrand(x):
    return x**2 / (np.exp(x) - 1)

def compute_integral_ratio(a, b, T_star):
    def numerator_integrand(x):
        return integrand(x)

    def denominator_integrand(x):
        return integrand(x)

    numerator, _ = quad(numerator_integrand, b, np.inf)
    denominator, _ = quad(denominator_integrand, a, np.inf)

    return numerator / denominator

# Set value I
I4471 = 42.0

# Range of values ​​T_*
start_T_star = 10000
end_T_star = 250000
step_T_star = 1000

best_T_star = None
min_difference = float('inf')

# Calculation and finding of the nearest T_*
for T_star in range(start_T_star, end_T_star + 1, step_T_star):
    a = 15.8 * 10**4 / T_star
    b = 28.53 * 10**4 / T_star
	c = 63.15 * 10**4 / T_star
    result = compute_integral_ratio(a, b, T_star)
    difference = abs(result - I4471)

    if difference < min_difference:
        min_difference = difference
        best_T_star = T_star

print(f"Найближче значення T_* до I: {best_T_star}")

for T_star in range(start_T_star, end_T_star + 1, step_T_star):
    a = 15.8 * 10**4 / T_star
    b = 28.53 * 10**4 / T_star
	c = 63.15 * 10**4 / T_star
    result = compute_integral_ratio(a, b, T_star)
    difference = abs(result - I4471)

    if difference < min_difference:
        min_difference = difference
        best_T_star = T_star

print(f"Найближче значення T_* до I: {best_T_star}")


for T_star in range(start_T_star, end_T_star + 1, step_T_star):
    a = 15.8 * 10**4 / T_star
    b = 28.53 * 10**4 / T_star
	c = 63.15 * 10**4 / T_star
    result = compute_integral_ratio(a, b, T_star)
    difference = abs(result - I4471)

    if difference < min_difference:
        min_difference = difference
        best_T_star = T_star

print(f"Найближче значення T_* до I: {best_T_star}")