from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FIR_Form ,SearchForm
from django.http import HttpResponseRedirect
from .models import FIR
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.core.mail import send_mail
import pandas as pd
from .utils import get_simple_plot
# Create your views here.
def get_FIR_view(request):
    form = FIR_Form(request.POST or None)
    sent = False
    if form.is_valid():
        form.save()
        cd = form.cleaned_data
        #FIR_url = request.build_absolute_uri(form.get_absolute_url())
        subject = "Reported FIR"
        message = f"FIR {FIR.id} \n\n" \
        f"PoliceStation :{cd['PoliceStation']}\'s \n Victim FirstName : : {cd['VicFN']} \n Victim LasttName : {cd['VicLN']} \n ComplaintType : {cd['ComplaintType']} \n Complaint FirstName : {cd['ComFN']} \n Registered Date : {cd['publish']} \n Description : {cd['Description']} \n"
        send_mail(subject, message, 'jayantk137@gmail.com',
        [cd['Email']])
        sent = True
    context = {'form':form ,'sent':sent}  

    return render(request,'FIR.html',context)         

def FIR_registerd(request):
    Fir = FIR.objects.all() 
    return render(request,'form/FIRInfo.html',{'FIR':Fir})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('ComplaintType', 'id')
            search_query = SearchQuery(query)
            results = FIR.objects.all().annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
    return render(request,'form/Search.html',{'form': form,'query': query,'results': results})


def chart_select_view(request):
    graph =None

    status_df = pd.DataFrame(FIR.objects.all().values())
    status_com = status_df['status']
    dic = {
        'Completed':0,
        'Not Updated':0,
    }
    for ele in status_com:
        dic[ele] += 1
    total = status_df['status'].count()
    chart_type = 'bar plot'
    graph = get_simple_plot(chart_type=chart_type,x=dic['Completed'],y=total,data=status_df['publish'])
    context ={
        'graph' : graph,
        'status' : status_df.to_html(),
    }
    return render(request,'form/graph.html',context)    