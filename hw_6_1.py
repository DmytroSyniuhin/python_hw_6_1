example_list = [{"name": "John", "age": 22},
                {"name": "Billy", "age": 15},
                {"name": "Daniel", "age": 15},
                {"name": "Jack", "age": 45}]

age_list = [example_list[i].get('age') for i in range(len(example_list))]
youngest_person = [example_list[i].get('name') for i in range(len(example_list))
                   if example_list[i].get('age') == min(age_list)]

name_length = [len(example_list[i].get('name')) for i in range(len(example_list))]
longest_name = [example_list[i].get('name') for i in range(len(example_list))
                if len(example_list[i].get('name')) == max(name_length)]

print(f"Ім'я наймолодшої людини - {youngest_person}")
print(f"Найдовше ім'я - {longest_name}")
print(f"Середній вік - {sum(age_list)/len(example_list)}")
