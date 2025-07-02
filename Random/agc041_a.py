N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    dist_to_1 = B - 1
    dist_to_N = N - A
    move_edge = min(dist_to_1, dist_to_N)

    a_dist_to_1 = A - 1
    b_dist_to_N = N - B

    # Aが1まで動き、1回止まると、 B - Aが偶数になる
    a_move_edge_cost = a_dist_to_1 + 1
    a_move_edge_and_return_cost = a_move_edge_cost + (B - a_move_edge_cost) // 2

    b_move_edge_cost = b_dist_to_N + 1
    b_move_edge_and_return_cost = b_move_edge_cost + (N - (A + b_move_edge_cost)) // 2

    move_edge_and_return_cost = min(
        a_move_edge_and_return_cost, b_move_edge_and_return_cost
    )

    print(min(move_edge, move_edge_and_return_cost))
