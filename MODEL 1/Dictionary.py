student_data = {
    "id_1":{"name":"affton","age":"27","city":"new york","country":"USA"},
    "id_2":{"name":"cassidy","age":"14","city":"banglore","country":"india"}
}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)

#activity_2
test_dict = {"codingal": 1,"is": 2,"best": 3,"for": 4,"learning": 5}
print("The original dictionary is",test_dict)

k = 2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res +1

print("number of keys",k)

#activity_3
country_code = {"india":"+91","USA":"+1","China":25}
print("The original dictionary is",country_code)
print("the country code for india is",country_code["india"])
print("the country code for USA is",country_code["USA"])
print("The country code for China is",country_code["China"])
