from django.shortcuts import render, redirect, get_object_or_404
from .models import myBooks
from .forms import BookForm

# List all books, and handle create or update
def book_list(request):
    if request.method == "POST":
        book_id = request.POST.get("book-id")  # Get book ID from the form
        if book_id:
            book = get_object_or_404(myBooks, id=book_id)  # Update existing book
        else:
            book = None  # Creating a new book
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the book (either create or update)
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm()  # Empty form for creating a new book

    books = myBooks.objects.all()  # Fetch all books from the database
    return render(request, 'index.html', {'books': books, 'form': form})  # Render the page with book list

# Delete a book by ID
def book_delete(request, id):
    book = get_object_or_404(myBooks, id=id)  # Fetch the book by ID
    if request.method == "POST":
        book.delete()  # Delete the book
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'ebooks/book_confirm_delete.html', {'book': book})  # Confirmation page
