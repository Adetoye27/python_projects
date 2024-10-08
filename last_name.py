# Print out the last name of the second employee. Please search through the dictionary below: 
#d = {"employees": [{"'firstName": "John", "lastName": "Doe"},
#{"firstName": "Anna", "lastName": "Smith"}, {"firstName": "Peter", "lastName": "Jones"}],
#"owners": [{"firstName": "Jack", "lastName": "Petter"},
#{"firstName": "Jessy", "lastName": "Petter"}]}


d = {"employees": [{"'firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"}, {"firstName": "Peter", "lastName": "Jones"}],
"owners": [{"firstName": "Jack", "lastName": "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]}



second_employee = d["employees"][1]["lastName"]

print(second_employee)
