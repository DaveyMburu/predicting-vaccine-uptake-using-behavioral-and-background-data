import pandas

def explore_dataset(path):
    df = pandas.read_csv(path)
    ribbon = '--------------------------------------------------------- \n \n'
    
    print('----------------Dataset Overview----------------  \n')
    print(df)
    print()
    print(ribbon)
    print('----------------Shape of the Dataset---------------- \n')
    print(df.shape)
    print()
    print(ribbon)
    print('----------------Features in the Dataset---------------- \n')
    print(df.columns)
    print()
    print(ribbon)
    print('----------------Summary Statistics of the Features---------------- \n')
    print(df.describe())
    print()
    print(ribbon)
    print('----------------Dataset Information---------------- \n')
    print(df.info())
    print()
    print(ribbon)
    
