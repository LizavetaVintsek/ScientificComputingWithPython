import pandas as pd
import numpy as np
D = {'Name': ["Hydrogen", "Helium", "Lithium", "Berrylium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"],
     'Symbol': ["H", "He","Li", "Be", "B", "C", "N", "O", "F", "Ne"],
     'Weight': np.arange( 1, 11, 1)}

df1 = pd.DataFrame(D)
df1.index = np.arange( 1, 11, 1)
print(df1)
