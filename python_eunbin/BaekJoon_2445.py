star = int(input())
star_count = 1
print_star = ""
for i in range(0, star*2):
    for j in range(0, star*2):
        if (j < star_count or j >= (star * 2) - star_count):
            print_star += "*"
        else:
            print_star += " "
    print(print_star)
    if i < (star - 1):
        print_star = ""
        star_count += 1
    elif i >= (star-1):
        print_star = ""
        star_count -= 1
