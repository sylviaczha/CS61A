import json
from ubc import main
def search(query, ranking=lambda r: -r.stars):
    """A restaurant search engine."""
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=rankings)
    #sorted function gives back results from least to greatest according to the key function

def num_shared_reviewers(restaurant, other):
    return fast_overlap(restaurant.reviewers, other.reviewers)
    return len([r for r in restaurant.reviewers if r in other.reviewers])

def fast_overlap(s, t):
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

class Restaurant:
    all = []
    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=num_shared_reviewers):
        "Return the K most similar restaurants to SELF, using SIMILARITY for comparison."
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]

    def __repr__(self):
        return '<' + self.name + '>'

def load_reviews(reviews_file):
    reviewers_by_restaurant = {}
    for line in open(reviews_file):
        r = json.loads(line) #gives a dictionary
        business_id = r['business_id']
        if business_id not in reviewers_by_restaurant:
            reviewers_by_restaurant[business_id] = [r['user_id']] #没有business_id, 添加元素
        reviewers_by_restaurant[business_id].append(r['user_id']) #已有business_id, 添加元素
    return reviewers_by_restaurant

def load_restaurants(reviewers_by_restaurant, restaurants_file):
    for line in open(restaurants_file):
        b = json.loads(line)
        reviewers = reviewers_by_restaurant.get(b['business_id'], [])
        Restaurant(b['name'], b['stars'], sorted(reviewers))

load_restaurants(load_reviews('reviews.json'), 'restaurants.json')

@main
def run():
    search = SearchEngine()
    while True:
        print('>', end=' ')
        results = search.lookip(input().strip())
        for r in results:
            print(r.name, 'shares reviewers with', r.similar(3))
