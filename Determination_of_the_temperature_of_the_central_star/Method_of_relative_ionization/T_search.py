#  OHEA - (O/He)/A
OHEA = 1

# T_* value range and step
T_star_start = 10000
T_star_end = 250000
step = 1000

# The beginning of the cycle
best_T_star = None
closest_diff = float('inf')

for T_star in range(T_star_start, T_star_end+1, step):
    result = calculate_integral(x, T_star)
    diff = abs(result - OHEA)
    if diff < closest_diff:
        closest_diff = diff
        best_T_star = T_star

# Outputting the result
print("Найближче до A значення T_*:", best_T_star)