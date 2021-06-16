from django.shortcuts import render, get_object_or_404
from .models import Post, Member, Event, Order, PhotoView
from .forms import FeedbackForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'order/details.html', {'order': 'order'})


def members_list(request):
    members = Member.ordered.all()
    return render(request, 'members.html', {'members': members})


def history(request):
    return render(request, 'history.html', )


def schedule(request):
    events = Event.ordered.all()
    return render(request, 'schedule.html', {'events': events})


def orders(request):
    orders_list = Order.ordered.all()
    return render(request, 'orders.html', {'orders': orders_list})


def order_detail(request, n):
    order_text = get_object_or_404(Order, auto_increment_id=n)
    return render(request, 'order/details.html', {'order_text': order_text})


def news(request):
    news = Post.published.all()
    return render(request, 'news.html', {'news': news})


def map_view(request):
    return render(request, 'map.html', )


def photo_list(request):
    photos = PhotoView.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})


def photo_view(request, n):
    single_photo = get_object_or_404(PhotoView, id=n)
    return render(request, 'photo/photo_view.html', {'photo': single_photo})


def contacts(request):
    return render(request, 'contacts.html', )


def send_letter(request):
    if request.method == "POST":
        comment_form = FeedbackForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        new_comment.save()
        return render(request, 'letter_sent.html', {})
    else:
        form = FeedbackForm()
        return render(request, 'letter.html', {'form': form})

