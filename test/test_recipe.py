import pytest
try:
    import mock
except:
    import unittest.mock as mock

from .context import recipe_writer
from recipe_writer.models.Recipe import Recipe


def test_recipe_init():
    recipe = Recipe("Chocolate Cake")
    assert recipe.name == "Chocolate Cake"
    assert recipe.ingredients == []
    assert recipe.directions == []
    assert recipe.notes == []


@mock.patch("recipe_writer.models.Recipe.Recipe._fill_list")
def test_set_ingredients(mock_fill_list):
    recipe = Recipe("Chocolate Cake")
    recipe.set_ingredients()
    mock_fill_list.assert_has_calls([mock.call(recipe.ingredients, False)])


@mock.patch("recipe_writer.models.Recipe.Recipe._fill_list")
def test_set_directions(mock_fill_list):
    recipe = Recipe("Chocolate Cake")
    recipe.set_directions()
    mock_fill_list.assert_has_calls([mock.call(recipe.directions, True)])


@pytest.mark.parametrize("input_value", ["y", "n", "N", "d", "3"])
@mock.patch("recipe_writer.models.Recipe.Recipe._fill_list")
@mock.patch("builtins.input")
def test_set_notes(mock_input_func, mock_fill_list, input_value):
    mock_input_func.return_value = input_value
    recipe = Recipe("Chocolate Cake")
    recipe._fill_list = mock_fill_list
    recipe.set_notes()
    if input_value not in ["n", "N"]:
        assert mock_fill_list.call_count == 1
    else:
        assert mock_fill_list.call_count == 0


def test_recipe_create_filename():
    assert Recipe._create_filename(None, "Hello there") == "Hello_there.md"
    assert Recipe._create_filename(None, "Moist cake that's good") == "Moist_cake_thats_good.md"
    assert Recipe._create_filename(None, "a4~`!@#$%^&*()-_+f=") == "a4f.md"


@pytest.mark.parametrize("is_ordered", [True, False])
@mock.patch("builtins.input")
def test_fill_list(mock_input_func, is_ordered):
    mock_input_func.side_effect = ["potatoes", "carrots", "turkey", ""]
    recipe = Recipe("Chocolate Cake")
    a_list = []
    recipe._fill_list(a_list, is_ordered)
    assert mock_input_func.call_count == 4
    assert a_list == ["potatoes", "carrots", "turkey"]
    if is_ordered:
        mock_input_func.assert_has_calls([mock.call("  1. "), mock.call("  2. "), mock.call("  3. "), mock.call("  4. ")])
    else:
        mock_input_func.assert_has_calls([mock.call("  - ")] * 4)