grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
from statistics import fmean
values = fmean(grades[0]), fmean(grades[1]), fmean(grades[2]), fmean(grades[3]), fmean(grades[4])
keys = sorted(students)
res = {keys[i]: values[i] for i in range(len(keys))}
print(res)
