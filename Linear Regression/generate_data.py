import numpy as np
import pandas as pd

N_obs = 1000

# create the city variable
city = np.random.randint(low=1, high=10, size=N_obs)

# create a variable with m^2
mu_m2, sigma_m2 = 100, 25 # mean and standard deviation
m2 = np.random.normal(mu_m2, sigma_m2, N_obs)
m2 = m2.round()

# create the age variable
mu_age, sigma_age = 80, 20 # mean and standard deviation
age = np.random.normal(mu_age, sigma_age, N_obs)
age = age.round()

# create the dependent variable (price)
price = 3*(city + np.random.randint(low=-1, high=1)) + 3000*m2 - 800*(age + np.random.randint(low=-1, high=1))

# create the train set
train = np.stack((city, m2, age, price), axis=1)
df = pd.DataFrame(train, columns=['City','m2','Age', 'Price'])