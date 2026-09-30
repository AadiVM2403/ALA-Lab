from vec import Vec


def test_vector_operations():
    print("--- 1. Testing Instantiation & String Representation ---")
    v1 = Vec([0, 1, 1.03])
    print(f"v1 = {v1}")
    print(f"Length of v1: {len(v1)}")

    print("\n--- 2. Testing Factory Methods (@staticmethod) ---")
    z = Vec.zeros(4)
    o = Vec.ones(4)
    u = Vec.uniform(3)
    print(f"Vec.zeros(4)   : {z}")
    print(f"Vec.ones(4)    : {o}")
    print(f"Vec.uniform(3) : {u}")

    print("\n--- 3. Testing Scalar Operations ---")
    v_scaled = 2.2 * v1  # __rmul__
    print(f"2.2 * v1       = {v_scaled}")
    v_scaled *= 5  # __imul__
    print(f"v_scaled *= 5  = {v_scaled}")

    print("\n--- 4. Testing Addition & Subtraction ---")
    a = Vec([1.0, 2.0, 3.0])
    b = Vec([4.0, 5.0, 6.0])

    print(f"a + b = {a + b}")
    print(f"b - a = {b - a}")
    print(f"-a = {-a}")

    a += b  # __iadd__
    print(f"a after (a+=b) = {a}")

    print("\n--- 5. Testing radd  ---")
    vec_list = [Vec([1, 2]), Vec([3, 4]), Vec([5, 6])]
    total = sum(vec_list)
    print(f"sum([v1, v2, v3]) = {total}")

    print("\n--- 6. Testing Norm calculation ---")
    v_norm_test = Vec([3.0, 4.0])
    print(f"Norm of [3.0, 4.0] = {v_norm_test.norm()}")


if __name__ == "__main__":
    test_vector_operations()