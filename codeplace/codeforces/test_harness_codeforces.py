"""
Universal test harness for Codeforces-style tasks.

You provide:
  - candidate_solve(stdin: str) -> str
  - reference_solve(stdin: str) -> str
  - (optional) brute_solve(stdin: str) -> str
  - generators: produce valid stdin strings

Harness will:
  - run small tests (compare to brute if available),
  - run edge tests,
  - run randomized stress tests,
  - log results to JSON/CSV.
"""

import random, time, json, csv
from typing import Callable, List, Dict, Any, Optional

# ------------------------------------------------------------
# Core runner
# ------------------------------------------------------------
def run_io(solve: Callable[[str], str], input_data: str) -> str:
    """Run solve() with given stdin string, capture stdout string."""
    return solve(input_data).strip()

def run_tests(
    candidate_solve: Callable[[str], str],
    reference_solve: Callable[[str], str],
    brute_solve: Optional[Callable[[str], str]] = None,
    generate_input_small: Callable[[], List[str]] = lambda: ["1\n5\n", "2\n10\n20\n"],
    generate_input_edges: Callable[[], List[str]] = lambda: ["1\n1\n", "1\n1000000\n"],
    generate_input_random: Callable[[int], List[str]] = lambda n: [f"1\n{random.randint(1, 10**6)}\n" for _ in range(n)],
    name: str = "candidate",
    random_tests: int = 50,
    log_json: str = "results.json",
    log_csv: str = "results.csv",
) -> Dict[str, Any]:
    results = {"name": name, "small": {}, "edges": {}, "random": {}}

    # Small tests
    mismatches_small = []
    if brute_solve is not None:
        small_inputs = generate_input_small()
        for inp in small_inputs:
            cand_out = run_io(candidate_solve, inp)
            brute_out = run_io(brute_solve, inp)
            if cand_out != brute_out:
                mismatches_small.append((inp, cand_out, brute_out))
        results["small"] = {"tested": len(small_inputs), "mismatches": mismatches_small}

    # Edge tests
    edge_inputs = generate_input_edges()
    mismatches_edges = []
    for inp in edge_inputs:
        cand_out = run_io(candidate_solve, inp)
        ref_out = run_io(reference_solve, inp)
        if cand_out != ref_out:
            mismatches_edges.append((inp, cand_out, ref_out))
    results["edges"] = {"count": len(edge_inputs), "mismatches": mismatches_edges}

    # Random tests
    rand_inputs = generate_input_random(random_tests)
    mismatches_random = []
    for inp in rand_inputs:
        cand_out = run_io(candidate_solve, inp)
        ref_out = run_io(reference_solve, inp)
        if cand_out != ref_out:
            mismatches_random.append((inp, cand_out, ref_out))
    results["random"] = {"tested": random_tests, "mismatches": mismatches_random}

    # Save logs
    with open(log_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open(log_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["phase", "input", "candidate", "expected"])
        for inp,u,ref in mismatches_small:
            writer.writerow(["small", inp.strip(), u, ref])
        for inp,u,ref in mismatches_edges:
            writer.writerow(["edge", inp.strip(), u, ref])
        for inp,u,ref in mismatches_random:
            writer.writerow(["random", inp.strip(), u, ref])

    return results

# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------
if __name__ == "__main__":
    # Example: задача "сумма чисел"
    # Input: t, затем t чисел
    # Output: сумма этих чисел

    def candidate_solve(stdin: str) -> str:
        it = iter(stdin.strip().split())
        t = int(next(it))
        nums = [int(next(it)) for _ in range(t)]
        # BUG: забыли один элемент
        return str(sum(nums[:-1]))

    def reference_solve(stdin: str) -> str:
        it = iter(stdin.strip().split())
        t = int(next(it))
        nums = [int(next(it)) for _ in range(t)]
        return str(sum(nums))

    def brute_solve(stdin: str) -> str:
        # в этой задаче brute совпадает с reference
        return reference_solve(stdin)

    def generate_input_small():
        return ["1\n5\n", "3\n1 2 3\n"]

    def generate_input_edges():
        return ["1\n0\n", "1\n1000000\n", "5\n0 0 0 0 0\n"]

    def generate_input_random(n: int):
        tests = []
        for _ in range(n):
            t = random.randint(1, 10)
            arr = [random.randint(0, 100) for _ in range(t)]
            tests.append(str(t) + "\n" + " ".join(map(str, arr)) + "\n")
        return tests

    summary = run_tests(
        candidate_solve,
        reference_solve,
        brute_solve=brute_solve,
        generate_input_small=generate_input_small,
        generate_input_edges=generate_input_edges,
        generate_input_random=generate_input_random,
        name="buggy_sum"
    )

    print("SUMMARY:", summary)
    print("Logs written to results.json and results.csv")
