import matplotlib.pyplot as plt 
import seaborn as sns
from io import BytesIO
import base64

def get_image():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_simple_plot(chart_type,*args,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=[10,4])
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    labels = 'Completed' , 'In Progress'
    sizes = [x,y-x]
    explode =(0.1,0)
    fig1 ,ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    """
    if chart_type=='bar plot':
        title = "Progress"
        plt.title(title)
        plt.bar(x,y)
    if chart_type=='sns':
        title= "Progress"
        plt.title(title)
        sns.countplot('name',data=data)
    """    

    plt.tight_layout()
    graph = get_image()
    return graph


