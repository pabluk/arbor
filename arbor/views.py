from django.db.models import F
from django.shortcuts import render_to_response, get_object_or_404

from trees.models import Tree, Name

def home(request):
    show_splash = request.session.get('show_splash', True)
    if show_splash:
        request.session['show_splash'] = False

    trees = Tree.objects.all()
    return render_to_response('index.html', {'trees': trees, 'show_splash': show_splash})

def about(request):
    return render_to_response('about.html')

def help(request):
    return render_to_response('help.html')

def tree(request, id):
    allow_vote = request.session.get('allow_vote_%s' % id, True)
    if allow_vote:
        request.session['allow_vote_%s' % id] = False

    tree = get_object_or_404(Tree, pk=id) 
    return render_to_response('infowindow_main.html', {'tree': tree, 'allow_vote': allow_vote})


def vote(request, id):
    tree = get_object_or_404(Tree, pk=id) 
    return render_to_response('infowindow_vote.html', {'tree': tree})

def results(request, tree_id, name_id):
    tree = get_object_or_404(Tree, pk=tree_id) 
    name = get_object_or_404(Name, pk=name_id) 
    tree.name_set.get(id=name_id)
    Name.objects.filter(pk=name_id).update(vote=F('vote') + 1)
    return render_to_response('infowindow_results.html', {'tree': tree, 'name': name})
