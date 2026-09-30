import timeit
import numpy as np
from vec import Vec


# ==================================================
# BENCHMARK FUNCTION
# ==================================================

def benchmark(operation, number=10, repeat=3):
    """
    Benchmark an operation using timeit.
    Returns the best average execution time.
    """

    times = timeit.repeat(
        stmt=operation,
        number=number,
        repeat=repeat
    )

    return min(times) / number


# ==================================================
# VECTOR SIZES
# ==================================================

sizes = [2000, 4000, 8000, 16000, 32000, 64000]

scalar = 2.5

vec_results = []
numpy_results = []


print("VECTOR PERFORMANCE BENCHMARK")
print("=" * 120)


# ==================================================
# RUN BENCHMARKS
# ==================================================

for n in sizes:

    print(f"\nTesting vector size: {n}")

    # ----------------------------------------------
    # Create custom vectors
    # ----------------------------------------------

    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # ----------------------------------------------
    # Create NumPy arrays
    # ----------------------------------------------

    np_v1 = np.array(v1.elements)
    np_v2 = np.array(v2.elements)

    # ==================================================
    # CUSTOM VEC BENCHMARKS
    # ==================================================

    add_time = benchmark(
        lambda: v1 + v2
    )

    sub_time = benchmark(
        lambda: v1 - v2
    )

    mul_time = benchmark(
        lambda: scalar * v1
    )

    neg_time = benchmark(
        lambda: -v1
    )

    norm_time = benchmark(
        lambda: v1.norm()
    )

    imul_time = benchmark(
        lambda: Vec(v1.elements).__imul__(scalar)
    )

    iadd_time = benchmark(
        lambda: Vec(v1.elements).__iadd__(v2)
    )

    vec_results.append({
        "size": n,
        "addition": add_time,
        "subtraction": sub_time,
        "multiplication": mul_time,
        "negation": neg_time,
        "norm": norm_time,
        "inplace_multiplication": imul_time,
        "inplace_addition": iadd_time
    })


    # ==================================================
    # NUMPY BENCHMARKS
    # ==================================================

    np_add_time = benchmark(
        lambda: np_v1 + np_v2
    )

    np_sub_time = benchmark(
        lambda: np_v1 - np_v2
    )

    np_mul_time = benchmark(
        lambda: scalar * np_v1
    )

    np_neg_time = benchmark(
        lambda: -np_v1
    )

    np_norm_time = benchmark(
        lambda: np.linalg.norm(np_v1)
    )


    np_imul_time = benchmark(
        lambda: np_v1.copy().__imul__(scalar)
    )


    np_iadd_time = benchmark(
        lambda: np_v1.copy().__iadd__(np_v2)
    )

    numpy_results.append({
        "size": n,
        "addition": np_add_time,
        "subtraction": np_sub_time,
        "multiplication": np_mul_time,
        "negation": np_neg_time,
        "norm": np_norm_time,
        "inplace_multiplication": np_imul_time,
        "inplace_addition": np_iadd_time
    })


# ==================================================
# DISPLAY CUSTOM VEC RESULTS
# ==================================================

print("\n")
print("=" * 120)
print("CUSTOM VEC PERFORMANCE")
print("=" * 120)

print(
    f"{'Size':<10}"
    f"{'Add (s)':<15}"
    f"{'Sub (s)':<15}"
    f"{'Mul (s)':<15}"
    f"{'Neg (s)':<15}"
    f"{'Norm (s)':<15}"
    f"{'*= (s)':<15}"
    f"{'+= (s)':<15}"
)

print("=" * 120)


for result in vec_results:

    print(
        f"{result['size']:<10}"
        f"{result['addition']:<15.8f}"
        f"{result['subtraction']:<15.8f}"
        f"{result['multiplication']:<15.8f}"
        f"{result['negation']:<15.8f}"
        f"{result['norm']:<15.8f}"
        f"{result['inplace_multiplication']:<15.8f}"
        f"{result['inplace_addition']:<15.8f}"
    )


print("=" * 120)


# ==================================================
# DISPLAY NUMPY RESULTS
# ==================================================

print("\n")
print("=" * 120)
print("NUMPY PERFORMANCE")
print("=" * 120)

print(
    f"{'Size':<10}"
    f"{'Add (s)':<15}"
    f"{'Sub (s)':<15}"
    f"{'Mul (s)':<15}"
    f"{'Neg (s)':<15}"
    f"{'Norm (s)':<15}"
    f"{'*= (s)':<15}"
    f"{'+= (s)':<15}"
)

print("=" * 120)


for result in numpy_results:

    print(
        f"{result['size']:<10}"
        f"{result['addition']:<15.8f}"
        f"{result['subtraction']:<15.8f}"
        f"{result['multiplication']:<15.8f}"
        f"{result['negation']:<15.8f}"
        f"{result['norm']:<15.8f}"
        f"{result['inplace_multiplication']:<15.8f}"
        f"{result['inplace_addition']:<15.8f}"
    )


print("=" * 120)