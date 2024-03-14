from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .review import generate_summary_with_index

import pandas as pd
import numpy as np

import psycopg2

import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px


from .forms import SearchForm



cache = {}
df = {}
# Create your views here.
def notebook():
    global df
    df = pd.read_csv("zomato_cleaned.csv")


def home(request):
    notebook()
    df.head()
    data_dict={
        'fname':'aditya',
        'lname':'balki',
        'num_list':"asd"
    }
    return  render(request,'home.html',{'data_dict':data_dict})


def about(request):
    return  render(request,'about.html')


def dashboard(request):
    # train_data = pd.DataFrame(list(Restaurant.objects.all().values()))

    # tRestaurant = train_data.shape[0]
    # average_rating = train_data['rate'].mean()
    # average_rating = round(average_rating, 2)
    # most_voted_restaurant = train_data.loc[train_data['votes'].idxmax()]['name']
    # average_cost_for_two = train_data['cost2plates'].mean()
    # average_cost_for_two = round(average_cost_for_two, 2)
    # area_distribution = train_data['area'].value_counts()
    # online_order_counts = (train_data['online_order'] == True).sum()
    # table_booking_counts = train_data['book_table'].value_counts()
    # top_Restaurant_type = train_data['rest_type'].value_counts()
    # top_cuisines = train_data['cuisines'].value_counts()
    # top_listed_in_type = train_data['listed_in_type'].value_counts()


    # form = SearchForm(request.POST or None)
    # result = train_data.copy()

    # if request.method == 'POST' and form.is_valid():
    #     search_query = form.cleaned_data['search_query']
    #     rate = int(form.cleaned_data['rate'])
    #     online_order = int(form.cleaned_data.get('online_order'))
    #     book_table = int(form.cleaned_data.get('book_table'))
    #     listed_in_type = form.cleaned_data['listed_in_type']


    #     if search_query:
    #         result = result[result['location'] == search_query]

    #     if rate:
    #         result = result[(result['rate'] <= rate) & (result['rate'] > rate - 1)]

    #     if online_order == 1:
    #         result = result[result['online_order'] == 'Yes']
    #     elif online_order == 2:
    #         result = result[result['online_order'] == 'No']

    #     if book_table == 1:
    #         result = result[result['book_table'] == 'Yes']
    #     elif book_table == 2:
    #         result = result[result['book_table'] == 'No']


    #     if listed_in_type == "Buffet":
    #         result = result[result['listed_in_type'] == 'Buffet']
    #     elif listed_in_type == "Delivery":
    #         result = result[result['listed_in_type'] == 'Delivery']
    #     elif listed_in_type == "Dine-out":
    #         result = result[result['listed_in_type'] == 'Dine-out']
    #     elif listed_in_type == "Desserts":
    #         result = result[result['listed_in_type'] == 'Desserts']
    #     elif listed_in_type == "Cafes":
    #         result = result[result['listed_in_type'] == 'Cafes']
    #     elif listed_in_type == "Drinks & nightlife":
    #         result = result[result['listed_in_type'] == 'Drinks & nightlife']
    #     elif listed_in_type == "Pubs and bars":
    #         result = result[result['listed_in_type'] == 'Pubs and bars']
        
    # col = train_data.columns.tolist()
    # result_dict = result.to_dict(orient='records') if result is not None else []

    # train_data = result
    
    # listed_in_type_distribution = train_data['listed_in_type'].value_counts()

    # fig4 = px.bar(listed_in_type_distribution,
    #             x=listed_in_type_distribution.index, 
    #             y=listed_in_type_distribution.values,
    #             color=listed_in_type_distribution.index,
    #             color_discrete_sequence= px.colors.qualitative.Set2,)
    # fig4.update_xaxes(title_text='Type')
    # fig4.update_yaxes(title_text='Data')
    # graph4 = fig4.to_html(full_html=False)

    # fig3 = px.bar(top_Restaurant_type, 
    #             x=top_Restaurant_type.index, 
    #             y=top_Restaurant_type.values,
    #             color=top_Restaurant_type.index,
                
    #             color_discrete_sequence= px.colors.qualitative.Vivid,)
    
    # graph3 = fig3.to_html(full_html=False)

    # fig = px.scatter(train_data, x='cost2plates', y='rate', title='Scatter Plot of Cost vs. Rating')
    # graph = fig.to_html(full_html=False)

    # # fig2 = px.scatter(train_data, x='location', y='rate', title='Average Rating by Location')
    # # graph2 = fig2.to_html(full_html=False)

    # fig2 = px.bar(train_data, 
    #           x='location', 
    #           y='rate', 
    #           title='Average Rating by Location', 
    #           labels={'rate': 'Average Rating'},
    #           color='location',
    #           color_discrete_sequence= px.colors.qualitative.Dark24,
    #           opacity=1,)
    

    # # Convert the plot to HTML
    # graph2 = fig2.to_html(full_html=False)
    value={
        'tRestaurant' : 51466,
        'average_rating': 3.7,
        'most_voted_restaurant':"Byg Brewski Brewing Company",
        'average_cost_for_two':558.08,
        'topRestaurant':"BTM",
        'online_order_counts':30311,
        'table_booking_counts':6449,
        'top_Restaurant_type':"Quick Bytes",
        'top_cuisines':"North Indian",
        'top_listed_in_type':"Delivery",
    }

    # value={
    #     'tRestaurant' : tRestaurant,
    #     'average_rating': average_rating,
    #     'most_voted_restaurant':most_voted_restaurant,
    #     'average_cost_for_two':average_cost_for_two,
    #     'topRestaurant':area_distribution.index[0],
    #     'online_order_counts':online_order_counts["Yes"],
    #     'table_booking_counts':table_booking_counts["Yes"],
    #     'top_Restaurant_type':top_Restaurant_type.index[0],
    #     'top_cuisines':top_cuisines.index[0],
    #     'top_listed_in_type':top_listed_in_type.index[0],
    #     'graph':graph,
    #     'graph2':graph2,
    #     'graph3':graph3,
    #     'graph4':graph4,
    #     'result': result_dict, 
    #     'columns': col, 
    #     'form': form,
    # }
    return  render(request,'dashboard.html',{'value':value})

def testing(request):
    # conn = psycopg2.connect(
    #     dbname="restaurantlyy-database",
    #     user="admin_restaurantlyy",
    #     password="restaurantlyy@123",
    #     host="restaurantlyy-database-server.postgres.database.azure.com",
    #     port="5432"
    # )

    # # Fetch data from the database using a cursor
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM zomato_restaurant LIMIT 10")  # Adjust query as needed

    # # Fetch all rows from the result set
    # rows = cursor.fetchall()

    # # Close the cursor and connection
    # cursor.close()
    # conn.close()

    # # Create a DataFrame from the fetched rows
    # columns = ['url', 'name', 'online_order', 'book_table', 'rate', 'votes', 
    #        'location', 'rest_type', 'cuisines', 'cost2plates', 'listed_in_type', 
    #        'area', 'ratings', 'reviews', 'count', 'sentiments', 'summaries', 
    #        'sentiment_label', 'index','id'] # Update with your column names
    # train_data = pd.DataFrame(rows, columns=columns)
    df = Restaurant.objects.all()[:10]
    data = []  # List to store dictionaries representing each entry

    # Iterate over the queryset and create a dictionary for each entry
    for entry in df:
        entry_dict = {
            'url': entry.url,
            'name': entry.name,
            'online_order': entry.online_order,
            'book_table': entry.book_table,
            'rate': entry.rate,
            'votes': entry.votes,
            'location': entry.location,
            'rest_type': entry.rest_type,
            'cuisines': entry.cuisines,
            'cost2plates': entry.cost2plates,
            'listed_in_type': entry.listed_in_type,
            'area': entry.area,
            'ratings': entry.ratings,
            'reviews': entry.reviews,
            'count': entry.count,
            'sentiments': entry.sentiments,
            'summaries': entry.summaries,
            'sentiment_label': entry.sentiment_label,
            'index': entry.index_f,
            'id': entry.id
        }
        data.append(entry_dict)

    # Convert the list of dictionaries into a DataFrame
    train_data = pd.DataFrame(data)
    print(train_data)
    value = {'train_data': train_data}
    return render(request, 'testing.html', {'value':value})


def load_data(request):
    df = pd.read_csv("zomato_cleaned.csv")
    # print(df.head())
    
    for i in df.index:
    
        obj = Zomato(
                name=df['name'][i],
                online_order=df['online_order'][i],
                book_table=df['book_table'][i],
                rate=df['rate'][i],
                votes=df['votes'][i],
                location=df['location'][i],
                rest_type=df['rest_type'][i],
                cuisines=df['cuisines'][i],
                cost2plates=df['cost2plates'][i],
                listed_in_type=df['listed_in_type'][i],
                area=df['area'][i],
                url=df['url'][i],
        )
        obj.save()
    
    return HttpResponse("data loaded")


def get_info(request, ind):
    if ind in cache:
        response = cache[ind] 
        print("HIT")
    else:
        cache[ind] = generate_summary_with_index(ind)
        response = cache[ind]
        print("MISS")
    return JsonResponse({"review": response})


def filter_data(request):
    df = pd.read_csv("zomato_cleaned.csv")

    form = SearchForm(request.POST or None)
    result = df.copy()

    search_query = ""
    if request.method == 'POST' and form.is_valid():
        search_query = form.cleaned_data['search_query']
        rate = int(form.cleaned_data['rate'])
        online_order = int(form.cleaned_data.get('online_order'))
        book_table = int(form.cleaned_data.get('book_table'))
        listed_in_type = form.cleaned_data['listed_in_type']


        if search_query:
            result = result[result['location'].str.lower() == search_query.lower()]

        if rate:
            result = result[(result['rate'] <= rate) & (result['rate'] > rate - 1)]

        if online_order == 1:
            result = result[result['online_order'] == 'Yes']
        elif online_order == 2:
            result = result[result['online_order'] == 'No']

        if book_table == 1:
            result = result[result['book_table'] == 'Yes']
        elif book_table == 2:
            result = result[result['book_table'] == 'No']


        if listed_in_type == "Buffet":
            result = result[result['listed_in_type'] == 'Buffet']
        elif listed_in_type == "Delivery":
            result = result[result['listed_in_type'] == 'Delivery']
        elif listed_in_type == "Dine-out":
            result = result[result['listed_in_type'] == 'Dine-out']
        elif listed_in_type == "Desserts":
            result = result[result['listed_in_type'] == 'Desserts']
        elif listed_in_type == "Cafes":
            result = result[result['listed_in_type'] == 'Cafes']
        elif listed_in_type == "Drinks & nightlife":
            result = result[result['listed_in_type'] == 'Drinks & nightlife']
        elif listed_in_type == "Pubs and bars":
            result = result[result['listed_in_type'] == 'Pubs and bars']
            
        result = result.sort_values(by='rate', ascending=False)    
    else:
        result = df.head(6)
    # col = df.columns.tolist()
    # result_dict = result.to_dict(orient='records')
    col = df.columns.tolist()
    result_dict = result.to_dict(orient='records') if result is not None else []

    context = {'result': result_dict, 'columns': col, 'form': form, 'keyword': search_query}
    return render(request, 'filter.html', context)


def index(request):
    return render(request, 'index.html')


def heatmap(request):
    return render(request, "heatmap_map.html")

def Zomato(request):
    return render(request, "Zomato.html")


