#!/usr/bin/python3
"""This module handles api actions for Place objects"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.place import Place
from models.user import User
from models.review import Review
from models import storage


@app_views.route(
    '/places/<place_id>/reviews', methods=["GET"], strict_slashes=False)
def get_reviews(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def find_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify([review.to_dict()])


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    else:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json(silent=True)
    if data is None:
        abort(400)
    if 'text' not in data:
        abort(400, description="Missing text")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    review_data = storage.get(Review, review_id)
    if not review_data:
        abort(404)
    found_review = request.get_json(silent=True)
    if not found_review:
        abort(400)
    for key, value in found_review.items():
        setattr(found_review, key, value)
    storage.save()
    return jsonify(review_data.to_dict()), 200
