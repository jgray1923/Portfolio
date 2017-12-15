# Portfolio
ABM model created from GEOG5995 practicals

My ABM is a basic model showing the interaction of agents, in this case sheep, within their environment. 
All the sheep move randomly, grazing at the environment (grass), and sharing their store (food within their stomach)
with other sheep if they are within the same neighbourhood. If they are greedy and eat too much, they will be sick! Thus reducing the
their store, whilst increasing the environment again.  

The files required for running the ABM are portfoliomodel.py, agentframework.py, and also in.csv.
The other files within the repository are dataout.csv (the environment once the sheep have eaten (and been sick)), agentconsumption.csv, and consumption.csv. 
The consumption csv files are both empty, as the data failed to write out, due to the consumption variable only containing one value, and writing out requires rows. This is why I changed consumption into a method within the class in agentframework.py.
A license file is also included, alongside this ReadMe file. 



