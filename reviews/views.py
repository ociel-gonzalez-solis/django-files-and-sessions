from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/danke'


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/danke'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, req):
#         form = ReviewForm()
#         return render(req, 'reviews/review.html', {
#             "form": form,
#         })

#     def post(self, req):
#         form = ReviewForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/danke')
#         return render(req, 'reviews/review.html', {
#             "form": form,
#         })


# def review(req):
    # if req.method == 'POST':
    #     form = ReviewForm(req.POST)

    #     if form.is_valid():
    #         form.save()
    #         # review = Review(
    #         #     user_name=form.cleaned_data['user'],
    #         #     review_text=form.cleaned_data['review_text'],
    #         #     rating=form.cleaned_data['rating'])
    #         # review.save()
    #         return HttpResponseRedirect('/danke')
    # else:
    #     form = ReviewForm()
    # return render(req, 'reviews/review.html', {
    #     "form": form,
    # })


class DankeReview(TemplateView):
    template_name = 'reviews/danke.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# def danke(req):
#     return render(req, 'reviews/danke.html')

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_reviews = Review.objects.get(pk=review_id)
    #     context['review'] = selected_reviews
    #     return context
