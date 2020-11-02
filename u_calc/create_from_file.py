from . import measurement as m

def read(filename, headerline = False, col = 0, totalcol = 1):
    #Reads the data from the file.
    #The file MUST have only the raw data
    with open(filename, 'r') as f:
        s = f.read()
        if headerline:
            s = s.split('\n', 1)[1]
        #For European/Brazilian number notation
        s = s.replace(",", ".")
        data = [float(val) for i, val in enumerate(s.split()) if i%totalcol == col]
    return data

#The standard deviation of the mean
def sigma_m(data, unc = 0):
    #Data must be number array, for use with unc, or
    l = len(data)
    av = sum(data)/l
    #deviation for the distribution
    dist_sigma = (sum([(x-av)**2 for x in data])/(l-1)) ** 0.5
    #compounding measurement uncertainty with distribution uncertainty
    total_sigma = m.norm(dist_sigma, unc)
    return total_sigma/(l) ** 0.5

def create(filename, headerline = False, col = 0, totalcol = 1, unc = 0):
    data = read(filename, headerline, col, totalcol)
    return m.Measurement( sum(data)/len(data), sigma_m(data, unc) )
