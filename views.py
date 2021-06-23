from django.shortcuts import render
from BRMapp.froms import NewBookForm, SearchForm
from BRMapp import models
from BRMapp.models import Book
from django.http import HttpResponse, HttpResponseRedirect

def searchBook(request):
    form=SearchForm()
    res=render(request,'BRMapp/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    # return HttpResponse("hellow")
    books=models.Book.objects.filter(title=form.data['title'])
    return render(request,'BRMapp/search_book.html',{'form':form,'books':books})
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-books')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res
def newBook(request):
        form=NewBookForm()
        res=render(request,'BRMapp/new_book.html',{'form':form})
        return res
def edit(request):
    if request.mehtod=='POST':
        form=NewBookForm(request.POST)
        book.models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['Publisher']
        book.save()
        return HttpResponseRedirect('BRMapp/view_books')
def viewBooks(request):
    book=models.Book.objects.all()
    return render(request,'BRMapp/view_book.html',{'books':book})
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponse("Record Stored")
