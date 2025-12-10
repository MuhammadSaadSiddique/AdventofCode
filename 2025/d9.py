import sys

def solve_red_tilesPart2():
    # Example input from the prompt to use as fallback
    example_input = """97554,50097
97554,51315
98014,51315
98014,52516
97678,52516
97678,53720
97562,53720
97562,54924
97454,54924
97454,56141
97443,56141
97443,57433
97867,57433
97867,58643
97663,58643
97663,59793
97165,59793
97165,61046
97160,61046
97160,62114
96393,62114
96393,63195
95760,63195
95760,64472
95797,64472
95797,65677
95560,65677
95560,66660
94703,66660
94703,67866
94461,67866
94461,69151
94375,69151
94375,70112
93536,70112
93536,71354
93308,71354
93308,72523
92904,72523
92904,73346
91858,73346
91858,74674
91719,74674
91719,75562
90824,75562
90824,76484
90006,76484
90006,77372
89154,77372
89154,78225
88272,78225
88272,79400
87821,79400
87821,80572
87337,80572
87337,81102
86079,81102
86079,82070
85350,82070
85350,83377
84968,83377
84968,83848
83709,83848
83709,84872
83012,84872
83012,85506
81946,85506
81946,86280
81016,86280
81016,87071
80101,87071
80101,88296
79517,88296
79517,88974
78496,88974
78496,89787
77571,89787
77571,89907
76184,89907
76184,90672
75235,90672
75235,91328
74214,91328
74214,92452
73448,92452
73448,92967
72332,92967
72332,92998
70982,92998
70982,93802
70016,93802
70016,94188
68855,94188
68855,95017
67874,95017
67874,94789
66483,94789
66483,95209
65349,95209
65349,95513
64177,95513
64177,96629
63238,96629
63238,96077
61829,96077
61829,97183
60847,97183
60847,96805
59518,96805
59518,97644
58438,97644
58438,97281
57143,97281
57143,98074
56022,98074
56022,98014
54782,98014
54782,97822
53542,97822
53542,98029
52336,98029
52336,97710
51110,97710
51110,97772
49901,97772
49901,97810
48690,97810
48690,97778
47478,97778
47478,97982
46246,97982
46246,97836
45036,97836
45036,97966
43790,97966
43790,97134
42679,97134
42679,96886
41496,96886
41496,97245
40189,97245
40189,96899
39015,96899
39015,96391
37886,96391
37886,95981
36740,95981
36740,95415
35648,95415
35648,95453
34359,95453
34359,95388
33083,95388
33083,94436
32143,94436
32143,93943
31035,93943
31035,93861
29737,93861
29737,92960
28817,92960
28817,92308
27788,92308
27788,91659
26764,91659
26764,91091
25697,91091
25697,90770
24471,90770
24471,89993
23524,89993
23524,89445
22424,89445
22424,88292
21760,88292
21760,88028
20438,88028
20438,86932
19758,86932
19758,86697
18364,86697
18364,85527
17769,85527
17769,84637
16938,84637
16938,84037
15822,84037
15822,83289
14834,83289
14834,82355
14039,82355
14039,81370
13304,81370
13304,80141
12878,80141
12878,79366
11899,79366
11899,78188
11447,78188
11447,77518
10289,77518
10289,76071
10264,76071
10264,75346
9148,75346
9148,74272
8572,74272
8572,73252
7903,73252
7903,71993
7683,71993
7683,70973
7020,70973
7020,70099
6017,70099
6017,68658
6273,68658
6273,67811
5141,67811
5141,66686
4658,66686
4658,65554
4186,65554
4186,64280
4154,64280
4154,62980
4279,62980
4279,61865
3780,61865
3780,60837
2857,60837
2857,59526
3153,59526
3153,58362
2784,58362
2784,57122
2862,57122
2862,55976
2293,55976
2293,54744
2372,54744
2372,53555
2006,53555
2006,52309
2532,52309
2532,51107
2444,51107
2444,50092
94969,50092
94969,48695
2401,48695
2401,47472
2104,47472
2104,46252
2085,46252
2085,45003
1851,45003
1851,43782
1972,43782
1972,42619
2475,42619
2475,41499
3127,41499
3127,40291
3243,40291
3243,39002
3045,39002
3045,37965
3910,37965
3910,36635
3654,36635
3654,35484
4066,35484
4066,34375
4595,34375
4595,33191
4899,33191
4899,32088
5426,32088
5426,31024
6031,31024
6031,29902
6495,29902
6495,28970
7349,28970
7349,27865
7837,27865
7837,26540
7938,26540
7938,25396
8400,25396
8400,24455
9204,24455
9204,23410
9835,23410
9835,22302
10380,22302
10380,21288
11067,21288
11067,20614
12197,20614
12197,19773
13085,19773
13085,18432
13380,18432
13380,18035
14766,18035
14766,16934
15358,16934
15358,15640
15781,15640
15781,15007
16873,15007
16873,14377
17948,14377
17948,13406
18715,13406
18715,13059
20005,13059
20005,12026
20730,12026
20730,11146
21591,11146
21591,10877
22889,10877
22889,9597
23491,9597
23491,9204
24688,9204
24688,8511
25691,8511
25691,7961
26779,7961
26779,7620
27973,7620
27973,7094
29063,7094
29063,6213
29990,6213
29990,5806
31142,5806
31142,5524
32340,5524
32340,5390
33582,5390
33582,4535
34564,4535
34564,3850
35624,3850
35624,3701
36855,3701
36855,3240
37995,3240
37995,3213
39244,3213
39244,3179
40478,3179
40478,2611
41607,2611
41607,2772
42864,2772
42864,2453
44043,2453
44043,1887
45207,1887
45207,1722
46423,1722
46423,2230
47675,2230
47675,2048
48883,2048
48883,2246
50098,2246
50098,1571
51326,1571
51326,2506
52506,2506
52506,2131
53744,2131
53744,2091
54971,2091
54971,2492
56149,2492
56149,2240
57417,2240
57417,2780
58563,2780
58563,3252
59707,3252
59707,2784
61058,2784
61058,3616
62111,3616
62111,4174
63214,4174
63214,4505
64376,4505
64376,4881
65525,4881
65525,4805
66844,4805
66844,5390
67925,5390
67925,5871
69044,5871
69044,6508
70091,6508
70091,7082
71161,7082
71161,7383
72372,7383
72372,7768
73554,7768
73554,9102
74188,9102
74188,9667
75254,9667
75254,9797
76614,9797
76614,10885
77343,10885
77343,10986
78771,10986
78771,12172
79404,12172
79404,12916
80365,12916
80365,13813
81194,13813
81194,14486
82217,14486
82217,15240
83178,15240
83178,16006
84134,16006
84134,16700
85175,16700
85175,17847
85735,17847
85735,18583
86748,18583
86748,19883
87090,19883
87090,20735
87968,20735
87968,21578
88871,21578
88871,22661
89450,22661
89450,23904
89772,23904
89772,24673
90819,24673
90819,25505
91806,25505
91806,26583
92392,26583
92392,27997
92332,27997
92332,29143
92741,29143
92741,29843
94107,29843
94107,31349
93707,31349
93707,32466
94157,32466
94157,33386
95143,33386
95143,34684
95110,34684
95110,35786
95628,35786
95628,36908
96109,36908
96109,37966
96874,37966
96874,39340
96368,39340
96368,40395
97227,40395
97227,41701
96853,41701
96853,42896
97012,42896
97012,44034
97623,44034
97623,45212
98064,45212
98064,46468
97674,46468
97674,47665
97990,47665
97990,48888
97735,48888
97735,50097
"""

    coords = []
    
    # Read from file or use example
    lines = example_input.strip().split('\n')

    # Parse coordinates
    for line in lines:
        if ',' in line:
            parts = line.strip().split(',')
            try:
                x, y = int(parts[0]), int(parts[1])
                coords.append((x, y))
            except ValueError:
                continue

    if len(coords) < 2:
        print("Not enough coordinates.")
        return

    # --- Optimization: Coordinate Compression & Sweep Line ---

    # 1. Extract unique Sorted Coords
    xs = sorted(list(set(p[0] for p in coords)))
    ys = sorted(list(set(p[1] for p in coords)))

    # Map real coord -> index
    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}

    W = len(xs) - 1
    H = len(ys) - 1

    # 2. Build Compressed Grid of "Elementary Rectangles"
    # is_inside[j][i] is True if the open rectangle (xs[i], xs[i+1]) x (ys[j], ys[j+1]) is INSIDE
    is_inside = [[False] * W for _ in range(H)]

    # 3. Sweep-Line to determine interior
    # Identify vertical edges of the polygon
    v_edges = []
    num = len(coords)
    for k in range(num):
        p1 = coords[k]
        p2 = coords[(k+1)%num]
        
        # We only care about vertical edges for the sweep line (x-ray casting)
        if p1[0] == p2[0]: 
            # The edge is at x = p1[0]
            # It spans from y1 to y2
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            v_edges.append((p1[0], y_min, y_max))

    v_edges.sort(key=lambda x: x[0])

    # For each horizontal strip in the compressed grid (interval ys[j] to ys[j+1])
    for j in range(H):
        y_mid = (ys[j] + ys[j+1]) / 2.0 # Sample y-coordinate for this strip
        
        # Find which vertical edges intersect this y-strip
        row_crossings = []
        for x, edge_ymin, edge_ymax in v_edges:
            # Check intersection.
            # Since vertices are on grid lines, a strict intersection with y_mid works.
            if edge_ymin < y_mid < edge_ymax:
                row_crossings.append(x)
        
        row_crossings.sort()
        
        # Apply Even-Odd rule:
        # Regions between pairs (0-1), (2-3) are INSIDE.
        for k in range(0, len(row_crossings), 2):
            x_start = row_crossings[k]
            x_end = row_crossings[k+1]
            
            # Map back to grid indices
            idx_start = x_map[x_start]
            idx_end = x_map[x_end]
            
            # Fill the grid cells
            for i in range(idx_start, idx_end):
                is_inside[j][i] = True

    # 4. Build 2D Prefix Sum (Integral Image)
    # P[j][i] stores count of valid elementary cells in rect (0,0) to (i, j)
    P = [[0] * (W + 1) for _ in range(H + 1)]
    for j in range(H):
        for i in range(W):
            val = 1 if is_inside[j][i] else 0
            P[j+1][i+1] = P[j][i+1] + P[j+1][i] - P[j][i] + val

    def count_valid_cells(ix1, iy1, ix2, iy2):
        if ix1 >= ix2 or iy1 >= iy2: return 0
        return P[iy2][ix2] - P[iy1][ix2] - P[iy2][ix1] + P[iy1][ix1]
    
    # Helper for 1D/Edge cases (Ray Casting)
    def is_point_inside(px, py):
        # Cast ray to the right
        intersections = 0
        for k in range(num):
            p1 = coords[k]
            p2 = coords[(k+1)%num]
            # Check edge (p1, p2)
            # Only check non-horizontal edges for horizontal ray
            if p1[1] == p2[1]: continue
            
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            if y_min <= py < y_max: # Intersects y-level?
                # Compute x intersection
                x_int = p1[0] + (py - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                if px < x_int:
                    intersections += 1
        return (intersections % 2) == 1

    # 5. Solver Loop
    max_area = 0
    best_pair = (None, None)

    for i in range(num):
        for k in range(i+1, num):
            p1 = coords[i]
            p2 = coords[k]

            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            area = w * h

            if area <= max_area:
                continue

            # Check Validity
            valid = False
            
            # Case A: Aligned (1D Rectangle / Line)
            if p1[0] == p2[0] or p1[1] == p2[1]:
                # Verify the midpoint is inside or on boundary
                # Since vertices are boundary, a straight line between them is valid 
                # unless it crosses outside (U-shape case).
                mid_x = (p1[0] + p2[0]) / 2.0
                mid_y = (p1[1] + p2[1]) / 2.0
                
                # We can reuse is_point_inside. 
                # Note: is_point_inside returns true for strictly inside.
                # However, our boundary lines are usually valid. 
                # For this specific puzzle, boundary lines are valid.
                # Simple hack: perturb slightly or check explicitly? 
                # Actually, check if mid_point is inside.
                # Since grid lines are integer, mid point of integers is X.5
                # The ray caster handles non-integer coords perfectly.
                if is_point_inside(mid_x, mid_y):
                    valid = True
                else:
                    # It might be ON a boundary edge.
                    # Brute force check if midpoint is on any edge.
                    on_boundary = False
                    for e_idx in range(num):
                        ep1 = coords[e_idx]
                        ep2 = coords[(e_idx+1)%num]
                        # Check if mid is on segment ep1-ep2
                        # Horizontal segment
                        if ep1[1] == ep2[1] == mid_y:
                            if min(ep1[0], ep2[0]) <= mid_x <= max(ep1[0], ep2[0]):
                                on_boundary = True; break
                        # Vertical segment
                        elif ep1[0] == ep2[0] == mid_x:
                            if min(ep1[1], ep2[1]) <= mid_y <= max(ep1[1], ep2[1]):
                                on_boundary = True; break
                    if on_boundary: valid = True

            # Case B: 2D Rectangle
            else:
                idx_x1, idx_x2 = sorted((x_map[p1[0]], x_map[p2[0]]))
                idx_y1, idx_y2 = sorted((y_map[p1[1]], y_map[p2[1]]))
                
                # Check if all elementary cells in this range are valid
                expected_cells = (idx_x2 - idx_x1) * (idx_y2 - idx_y1)
                actual_cells = count_valid_cells(idx_x1, idx_y1, idx_x2, idx_y2)
                
                if actual_cells == expected_cells:
                    valid = True

            if valid:
                max_area = area
                best_pair = (p1, p2)

    print("-" * 30)
    print(f"Processed {len(coords)} red tiles.")
    print(f"Largest Valid Rectangle Area: {max_area}")
    if best_pair[0]:
        print(f"Corners: {best_pair[0]} and {best_pair[1]}")
    print("-" * 30)

if __name__ == "__main__":
    solve_red_tilesPart2()
