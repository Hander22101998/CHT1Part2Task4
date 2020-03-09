seconds = int(input()) 
minutes = int (input())
hour = int (input())

chas1 = int(input())
chas2 = int(input())
chas3 = int(input())

budilnik_n1 = minutes * 60 + 3600 * hour + seconds
budilnik_2 = chas2 * 60 + 3600 * chas1 + chas3

print (budilnik_2 - budilnik_n1)

