"""Test my garden functions."""
__author__ = "730679888"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_new_kind():
    """Test adding a new plant kind to the dictionary."""
    by_kind = {}
    add_by_kind(by_kind, 'Flower', 'Rose')
    assert 'Flower' in by_kind
    assert 'Rose' in by_kind['Flower']


def test_add_by_kind_existing_kind():
    """Test adding a plant to an existing kind in the dictionary."""
    by_kind = {'Vegetable': ['Tomato']}
    add_by_kind(by_kind, 'Vegetable', 'Cucumber')
    assert 'Cucumber' in by_kind['Vegetable']


def test_add_by_date_new_month():
    """Test adding a new plant for a new month."""
    garden_by_date = {}
    add_by_date(garden_by_date, 'May', 'Sunflower')
    assert 'May' in garden_by_date
    assert 'Sunflower' in garden_by_date['May']


def test_add_by_date_existing_month():
    """Test adding a plant to an existing month."""
    garden_by_date = {'June': ['Lavender']}
    add_by_date(garden_by_date, 'June', 'Daisy')
    assert 'Daisy' in garden_by_date['June']


def test_lookup_by_kind_and_date_found():
    """Test the lookup function for a kind and month have at least one common plant."""
    plants_by_kinds = {'Herb': ['Mint', 'Basil']}
    plants_by_date = {'July': ['Basil']}
    result = lookup_by_kind_and_date(plants_by_kinds, plants_by_date, 'Herb', 'July')
    assert result == "Herbs to plant in July:['Basil']"


def test_lookup_by_kind_and_date_not_found():
    """Test the lookup function for a kind and month that exist but do not have a common plant."""
    plants_by_kinds = {'Herb': ['Mint', 'Cilantro']}
    plants_by_date = {'August': ['Rosemary']}
    result = lookup_by_kind_and_date(plants_by_kinds, plants_by_date, 'Herb', 'August')
    assert result == "No Herbs to plant in August."
