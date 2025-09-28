# # Importing built-in Module.
# Built-in modules can be directly imported using "import" keyword without any installtion.

import math

from math import pi

print("The value of pi: ", pi)

# Importing External Modules
# To use external modules, we need to install them first, we can easily install any external module using pip command in the terminal, for example:

# # pip install module_name.

import pandas

data = {
    "Name": ["Rafsan", "Arif", "Sanjay"],
    "Age": [25, 34, 33], 
}

df = pandas.DataFrame(data)
print(df)


# # Hanlde impritng error.

try:
    import math
    from math import p
    print(pi)
except:
    print("No data found")
