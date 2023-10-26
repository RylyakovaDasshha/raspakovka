#10
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)

print('-' * 50)

#11
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

print('-' * 50)

#12
*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

print('-' * 50)

#13
head, *middle, tail = [1, 2, 3, 4, 5]

print(head)
print(middle)
print(tail)

print('-' * 50)

#14
first, second, *other = [1, 2, 3, 4, 5]

print(first)
print(second)
print(other)

print('-' * 50)

#15
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]

print(first)
print(third)
print(last)

print('-' * 50)

#16
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}

print(red)
print(green)
print(other)

print('-' * 50)

#17
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)

nums3 = [*nums1, *nums2]
print(nums3)

print('-' * 50)

#18
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}

dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)

print('-' * 50)
