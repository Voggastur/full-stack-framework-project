from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import Category, Product, Review
from .forms import ProductForm, ReviewForm


# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual products and test against reviews """

    product = get_object_or_404(Product, pk=product_id)
    default_user_image = 'https://raw.githubusercontent.com/Voggastur/fsf-project/master/media/default_user.jpg'

    # If review matches product id I want to import the review to the template
    if Review.objects.filter(reviewed_product=product_id).exists():
        review = get_object_or_404(Review, reviewed_product=product_id)
    else:
        review = None

    context = {
        'product': product,
        'review': review,
        'default_user_image': default_user_image,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """ Handle POST form data to add review to database,
    else show the add review template with review form """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    related_review = Review.objects.filter(reviewed_product=product_id)
    reviewform = ReviewForm()

    if request.method == 'POST':
        reviewform = ReviewForm(request.POST, instance=product)
        form_data = {
            'header': request.POST['header'],
            'body': request.POST['body']
            }
        reviewform = ReviewForm(form_data)

        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.created_by = request.user
            review.reviewed_product = product
            review.save()
            messages.success(request,
                             f'Review for {product.name} has been posted!')
        else:
            messages.error(request,
                           'Sorry, an error has occured when posting your review, please try again!')
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        reviewform = ReviewForm(instance=user)

    context = {
        "product": product,
        "related_review": related_review,
        "reviewform": reviewform,
    }

    return render(request, 'products/add_review.html', context)


@login_required
def edit_review(request, review_id):
    """ View to edit an existing review """

    review = get_object_or_404(Review, created_by_id=request.user, pk=review_id)
    user = get_object_or_404(User, username=request.user)
    reviewform = ReviewForm(instance=review)

    if request.method == "POST":
        reviewform = ReviewForm(request.POST, instance=user)
        if reviewform.is_valid():
            reviewform.save()
            messages.success(request,
                             f'Review for {review.reviewed_product} has been updated!')
            return redirect('products')

        else:
            messages.error(request,
                           'An error has occured when updating the review, please try again')

    template = 'products/edit_review.html'
    context = {
        'review': review,
        'reviewform': reviewform,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """

    review = get_object_or_404(Review, created_by_id=request.user, pk=review_id)
    review.delete()
    messages.success(request, 'Review has been deleted.')

    return redirect('products')


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
