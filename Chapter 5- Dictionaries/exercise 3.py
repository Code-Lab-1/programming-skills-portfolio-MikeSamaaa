glossary = {"Python" : " is a Language that supports the Object Oriented Programming paradigm.",
"Range()" : " function returns a list of integers, the sequence of which is defined by the arguments passed to it.",
"While Loops" : " A While loop permits code to execute repeatedly until a certain condition is met. ",
"Sets" : " are collections of unique but unordered items.",
"Tuples" : " A Python data type that holds an ordered collection of values, which can be of any type.",
"Variables" : " are assigned values using the = operator",
"String" : " store characters and have many built-in convenience methods that let you modify their content.",
"List" : " A collection of items in a particular order.",
"Float" : " A numerical value with a decimal component.",
"Boolean" : " Returns a value of true or false"}

for word, meaning in glossary.items():
    print("\n" + word.title() + ":" + meaning)
