import random
from test_harness_codeforces import run_tests

# ------------------------------------------------------------
# 1. ТВОЁ РЕШЕНИЕ (кандидат)
# ------------------------------------------------------------
def candidate_solve(stdin: str) -> str:
    it = iter(stdin.strip().split())
    t = int(next(it))
    res = []

    for _ in range(t):
        k = int(next(it))

        if k <= 9:
            res.append(str((1 + k) * k // 2))
            continue

        s = 9
        i = 1
        while s <= k:
            i += 1
            s += i * 9 * 10 ** (i - 1)

        s -= i * 9 * 10 ** (i - 1)
        ost = k - s
        i -= 1

        count = 0
        for j in range(1, 10):
            count += j * i * 10 ** (i - 1)

        dl = ost // (i + 1)
        last = ost % (i + 1)

        if last != 0:
            num = str(10 ** i + dl)
            for q in range(last):
                count += int(num[q])

        if dl == 0:
            res.append(str(count))
            continue

        last_num = str(dl + 10 ** i - 1)
        plus = sum(int(last_num[w]) for w in range(i))
        count += plus + int(last_num[-1])

        for x in range(i, -1, -1):
            start = 1 if x == 0 else 0
            for y in range(start, int(last_num[x])):
                if x != i:
                    count += (plus + y) * 10 ** (i - x) + 45 * (i - x) * 10 ** (i - x - 1)
                else:
                    count += (plus + y) * 10 ** (i - x)
            if x != 0:
                plus -= int(last_num[x - 1])

        res.append(str(count))

    return "\n".join(res)


# ------------------------------------------------------------
# 2. ЭТАЛОННОЕ РЕШЕНИЕ (прямое)
# ------------------------------------------------------------
def reference_solve(stdin: str) -> str:
    it = iter(stdin.strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        k = int(next(it))
        s = "".join(str(i) for i in range(1, 1000000))  # ограничим для тестов
        part = s[:k]
        out.append(str(sum(map(int, part))))
    return "\n".join(out)


# ------------------------------------------------------------
# 3. BRUTE (для малых k)
# ------------------------------------------------------------
def brute_solve(stdin: str) -> str:
    return reference_solve(stdin)


# ------------------------------------------------------------
# 4. ГЕНЕРАТОРЫ ТЕСТОВ
# ------------------------------------------------------------
def generate_input_small():
    return [
        "1\n1\n",
        "1\n5\n",
        "2\n1 10\n",
        "3\n1 2 3\n",
        "1\n15\n",
    ]

def generate_input_edges():
    return [
        "1\n9\n",       # до конца первой группы
        "1\n10\n",      # начало следующей
        "1\n11\n",
        "1\n20\n",
        "1\n100\n",
    ]

def generate_input_random(n: int):
    tests = []
    for _ in range(n):
        t = random.randint(1, 5)
        ks = [str(random.randint(1, 200)) for _ in range(t)]
        tests.append(str(t) + "\n" + "\n".join(ks) + "\n")
    return tests


# ------------------------------------------------------------
# 5. ЗАПУСК
# ------------------------------------------------------------
if __name__ == "__main__":
    summary = run_tests(
        candidate_solve,
        reference_solve,
        brute_solve=brute_solve,
        generate_input_small=generate_input_small,
        generate_input_edges=generate_input_edges,
        generate_input_random=generate_input_random,
        name="sum_digits_seq"
    )

    print("SUMMARY:", summary)
    print("Логи смотри в results.json и results.csv")
