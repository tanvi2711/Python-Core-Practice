# Problem-13` Using filter() and list() functions and .lower() method filter all the vowels in a given string


st='CampusX is an Online Mentorship Program fOr EnginEering studentS.'



nst1=filter(lambda x: x in ['a','e','i','o','u','A','E','I','O','U'],st)

print(list(nst1))