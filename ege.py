# 3 задание
# r = 0
# for x1 in range(2):
#     for x2 in range(2):
#         for x3 in range(2):
#             for x4 in range(2):
#                 for x5 in range(2):
#                     for x6 in range(2):
#                         for x7 in range(2):
#                             for x8 in range(2):
#                                 for x9 in range(2):
#                                     if x1 == x2 or ((not x3 and x1) or (not x1 and x3)) == 0:
#                                         if x2 == x3 or ((not x4 and x2) or (not x2 and x4)) == 0:
#                                             if x3 == x4 or ((not x5 and x3) or (not x3 and x5)) == 0:
#                                                 if x4 == x5 or ((not x6 and x4) or (not x4 and x6)) == 0:
#                                                     if x5 == x6 or ((not x7 and x5) or (not x5 and x7)) == 0:
#                                                         if x6 == x7 or ((not x8 and x6) or (not x6 and x8)) == 0:
#                                                             if x7 == x8 or ((not x9 and x7) or (not x7 and x9)) == 0:
#                                                                 r += 1
# print(r)

# 2 задание
# r = 0
# for x1 in range(2):
#     for x2 in range(2):
#         for x3 in range(2):
#             for x4 in range(2):
#                 for x5 in range(2):
#                     for x6 in range(2):
#                         for x7 in range(2):
#                             for x8 in range(2):
#                                 if x1 == x2 or ((not x3 and x1) or (not x1 and x3)) == 0:
#                                     if x2 == x3 or ((not x4 and x2) or (not x2 and x4)) == 0:
#                                         if x3 == x4 or ((not x5 and x3) or (not x3 and x5)) == 0:
#                                             if x4 == x5 or ((not x6 and x4) or (not x4 and x6)) == 0:
#                                                 if x5 == x6 or ((not x7 and x5) or (not x5 and x7)) == 0:
#                                                     if x6 == x7 or ((not x8 and x6) or (not x6 and x8)) == 0:
#                                                         r += 1
# print(r)

r = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            for x8 in range(2):
                                for x9 in range(2):
                                    for x10 in range(2):
                                        if (x1 != x2) and (x1 or x3) and not(x1 and x3) == 0:
                                            if (x2 != x3) and (x2 or x4) and not (x2 and x4) == 0:
                                                if (x3 != x4) and (x3 or x5) and not (x3 and x5) == 0:
                                                    if (x4 != x5) and (x4 or x6) and not (x4 and x6) == 0:
                                                        if (x5 != x6) and (x5 or x7) and not (x5 and x7) == 0:
                                                            if (x6 != x7) and (x6 or x8) and not (x6 and x8) == 0:
                                                                if (x7 != x8) and (x7 or x9) and not (x7 and x9) == 0:
                                                                    if (x8 != x9) and (x8 or x10) and not (x8 and x10) == 0:
                                                                        r += 1
print(r)

